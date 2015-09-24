"""Base.py holds common functionality for future classes.

"""
import string
import random

from tfpipe.utils import logger
from tfpipe.utils import InvalidInput, InvalidObjectCall, InvalidType

class Job(object):
    """Generic Job Interface functionality. 

    """
    dep_options = ('done', 'ended', 'exit', 'external',
                   'post_done', 'post_err', 'started')
    init_options = ('cmd', 'args', 'name', 'dep_str')
    def __init__(self, **inputs):
        """Initialize Job.

        Objects that inherit this class receive Job methods and attributes.
        Those parent objects can also override the cmd attribute.

        Parameters:
        cmd, args, pos_args, name, dep, dep_str

        """
        message = "Illegal input argument pass during init."
        self._check_valid_input_options(self.init_options, 
                                        inputs.keys(),
                                        message)
        if not hasattr(self, '_cmd'):
            raise InvalidObjectCall, "This object cannot be called directly."
        self.cmd = inputs.get('cmd', self._cmd)
        self.args = inputs.get('args', {}) 
        self.pos_args = inputs.get('pos_args', [])
        self.name = self._initialize_name(inputs)
        self.dep_str = inputs.get('dep_str', '')
        self.dep_str_at_init = bool(self.dep_str)
        self.dep = self._initialize_dependencies(inputs)
        self.bsub_args = inputs.get('bsub_args', {})
        self.redirect_output_file = ''
        self.redirect_error_file = ''
        self.input_file = None
        self.output_file = None
        self.error_file = None
        self.io_flag_handler = {'input': self._io_flag_input,
                                'output': self._io_flag_output,
                                None: None}
        logger.info("%s: initialized with '%s' arguments and command: %s " % 
                    (self.name, self._parse_args(), self.cmd))

    def __repr__(self):
        """Command Line representation.

        """
        return "%s(%r)" % (self.__class__, self.args)

    def __str__(self):
        """Represent object as string.

        """
        redirect_output_str, redirect_error_str = '', ''
        if self.redirect_output_file:
            redirect_output_str = "%s %s" % (">", self.redirect_output_file)
        if self.redirect_error_file:
            redirect_error_str = "%s %s" % ("2>", self.redirect_error_file)
        return " ".join((self.cmd,
                         self._parse_args(),
                         redirect_output_str,
                         redirect_error_str))

    def _initialize_dependencies(self, inputs):
        """Method to initialize job dependencies.

        Initializes dictionary of LSF Dependency Condition keys with empty list
        values.

        """
        tmp = dict((depopt, []) for depopt in self.dep_options)
        for key, value in inputs.get('dep', ''):
            tmp[key].append(value)
        return tmp

    def _check_valid_input_options(self, options, input_keys, message):
        """Hidden method checks input values.

        """
        if sum([args not in options for args in input_keys]):
            raise InvalidInput, message

    def _parse_args(self):
        """Parse arguments and positional arguments.

        """
        kw = " ".join("%s %s" % (str(k), str(v)) for k,v in self.args.items())
        pos = " ".join(self.pos_args) if self.pos_args else ''
        return " ".join([kw, pos])
                         
    def _initialize_name(self, inputs):
        """Assign job name.

        Check valid characters in proposed name.  Replace with random strings.

        """
        return self._drop_invalid_ascii(inputs.get('name',self._make_jobname()))

    def _drop_invalid_ascii(self, name):
        """

        """
        allowed = string.digits + string.ascii_letters + '_'
        return "".join([i for i in name if i in allowed])
        
    def _make_jobname(self, size=10, chars=string.ascii_letters):
        """Return random string.

        """
        return "".join(random.choice(chars) for x in range(size))

    def _build_dep_str(self):
        """Build LSF dependency string.

        """
        str_tmp = " ".join([(k + " ") * len(v) for k, v in self.dep.items() 
                            if len(v) > 0])
        self.dep_str = "&&".join(str_tmp.split())

    def _io_flag_input(self, value):
        """Get job's input file from previous job output.

        """
        self.input_file = value
        logger.info("%s: input_file attribute '%s' set for %s" % 
                    (self.name, value, self.cmd))
        
    def _io_flag_output(self, value):
        """Set output_file attribute.

        """
        self.output_file = value
        logger.info("%s: output_file attribute '%s' set for %s" % 
                    (self.name, value, self.cmd))
        
    def add_argument(self, arg, value=None, io_flag=None):
        """Method adds command line arguments to object.

        Argument value should be either a string or some Job instance. io_flag
        can only be 'input' or 'output' and will set the respective file
        attributes.
        
        """
        handler = self.io_flag_handler.get(io_flag)
        if handler:
            handler(value)
        self.args[arg] = True and value or ''
        logger.info("%s: argument '%s %s' added to %s" % 
                    (self.name, arg, self.args[arg], self.cmd))

    def add_bsub_argument(self, arg, value=None):
        """Method adds command line arguments to future bsub command.

        """
        self.bsub_args[arg] = True and value or ''
        logger.info("%s: argument '%s %s' added to %s" %
                    (self.name, arg, self.bsub_args[arg], self.cmd))

    def add_positional_argument(self, arg):
        """Method adds positional arguments to object.

        """
        self.pos_args.append(arg)
        logger.info("%s: argument '%s' added to %s" %
                    (self.name, arg, self.cmd))

    def add_jobname(self, jobname):
        """Add name to current job.

        """
        tmp = self.name
        self.name = str(jobname)
        logger.info("%s: replacing jobname with '%s'" %
                    (tmp, self.name))

    # make it so list does not have to be specified
    def add_dependencies(self, **kwargs):
        """Add job dependencies to object.

        Method allows user to add dependency arguments to current job.  User 
        specifies under what dependency condition each job is located, and has 
        ability to specify the dependency string.  Dependency conditions must be
        of type list.

        If user does not specify a dependency string, tfpipe will make a best 
        guess based on keys from the dependency dictionary.  

        """
        self.dep_str = kwargs.pop('dep_str', self.dep_str)
        message = "Illegal input argument in add_dependency."
        self._check_valid_input_options(self.dep_options, 
                                        kwargs.keys(), 
                                        message)
        for key, value in kwargs.iteritems():
            if isinstance(value, list):
                try:
                    self.dep[key] += list(value)
                except KeyError:
                    self.dep[key] = list(value)
            else:
                raise InvalidInput, "Operand of dependency must be of type list."

    def show_as_list(self):
        """Output command as list.

        """
        l = [self.cmd, ]
        return l + list(reduce(lambda x, y: x + y, self.args.items()))

    def show(self):
        """Display job shell representation at current state.

        """
        print str(self)

    def get_command(self):
        """Display job shell representation at current state.

        """
        return str(self)

    def redirect_output(self, outputfile, io_flag=None):
        """Method to redirect output in the Unix sense.

        Has ability to set output as output file to be referenced.

        """
        handler = self.io_flag_handler.get(io_flag)
        if handler:
            handler(outputfile)
        self.redirect_output_file = outputfile
        logger.info("%s: output_file attribute '%s' set for %s" % 
                    (self.name, self.output_file, self.cmd))

    def redirect_error(self, errorfile, io_flag=None):
        """Method to redirect error in the Unix sense.

        Has ability to set error file as file to be referenced.

        """
        handler = self.io_flag_handler.get(io_flag)
        if handler:
            handler(errorfile)
        self.redirect_error_file = errorfile
        logger.info("%s: error_file attribute '%s' set for %s" % 
                    (self.name, self.error_file, self.cmd))

    def set_output_file(self, value):
        """Set output_file attribute.

        """
        self._io_flag_output(value)

    def get_output_file(self,):
        """

        """
        return self.output_file


