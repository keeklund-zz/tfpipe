"""Base.py holds common functionality for future classes.

"""
import string
import random

from tfpipe.utils import logger
from tfpipe.utils import InvalidInput, InvalidObjectCall, InvalidType
class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class jobid:
    def __init__(self):
        self.jobid = 0
    def getjobid(self):
        jobstring = "JOB%04d" % self.jobid
        self.jobid += 1
        return jobstring

class Job(object):
    """Generic Job Interface functionality. 

    """
    dep_options = ('done', 'ended', 'exit', 'external',
                   'post_done', 'post_err', 'started')
    init_options = ('cmd', 'args', 'name', 'module')
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
        if hasattr(self,'_memory_req_slurm'):
            self._memory_req_slurm = inputs.get('_memory_req_slurm', self._memory_req_slurm)
        else:
            self._memory_req_slurm = None
        if hasattr(self,'_memory_req_lsf'):
            self._memory_req_lsf = inputs.get('_memory_req_lsf', self._memory_req_lsf)
        else:
            self._memory_req_lsf = None

        self.cmd = inputs.get('cmd', self._cmd)
        self.args = inputs.get('args', {}) 
        self.pos_args = inputs.get('pos_args', [])
        self.name = self._initialize_name(inputs)

        # These store values in the string form of the job control system in question
        self._dep_str_lsf = None
        self._dep_str_slurm = None
        self._time_str_slurm = '"02:00:00"'
        # TODO REFACTOR - This is old code when you could pass dependencies at initialization.
        self.dep = {}
        self.redirect_output_file = ''
        self.append_output_file = ''
        self.redirect_error_file = ''
        self.input_file = None
        self.output_file = None
        self.error_file = None
        self.queue = None
        self.hoststospan = 1
        self.numberofprocesses = 1
        self.job_output_file = "%s.out" % (self.name)
        self.io_flag_handler = {'input': self._io_flag_input,
                                'output': self._io_flag_output,
                                None: None}
        jobobj = jobid.Instance()
        self._jobid = jobobj.getjobid()
        #Deal with the memory requirements for seperate job controllers

        if inputs.get('module'):
            self._module = inputs.get('module')
        if inputs.get('module_slurm'):
            self._module_slurm = inputs.get('module_slurm')
        logger.info("%s: initialized with '%s' arguments and command: %s " % 
                    (self.name, self._parse_args(), self.cmd))
    @property
    def module(self):
        return self._module

    @property
    def module_slurm(self):
        return self._module_slurm

    @property
    def dep_str_lsf(self):
        return self._dep_str_lsf

    @dep_str_lsf.getter
    def get_dep_str(self):
        if not self._dep_str_lsf:
            self._build_dep_str_lsf()
        return self._dep_str_lsf

    @property
    def dep_str_slurm(self):
        return self._dep_str_slurm

    @dep_str_slurm.getter
    def get_dep_str_slurm(self):
        if not self._dep_str_slurm:
            self._build_dep_str_slurm()
        return self._dep_str_slurm

    @property
    def jobid(self):
        return self._jobid

    @jobid.getter
    def get_jobid(self):
        return self._jobid

    #@TODO REFACTOR - I Imagine that there is a better way to combine the slurm and LSF memory requirements
    @property
    def memory_req_slurm(self):
        return self._memory_req_slurm
    @memory_req_slurm.setter
    def memory_req_slurm(self, value):
        self._memory_req_slurm = value

    @property
    def memory_req_lsf(self):
        return self._memory_req_lsf
    @memory_req_lsf.setter
    def memory_req_lsf(self, value):
        self._memory_req_lsf = value

    @property
    def time_str_slurm(self):
        return self._time_str_slurm
    @time_str_slurm.setter
    def time_str_slurm(self, value):
        self._time_str_slurm = value



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
        elif self.append_output_file:
            redirect_output_str = "%s %s" % (">>", self.append_output_file)
        if self.redirect_error_file:
            redirect_error_str = "%s %s" % ("2>", self.redirect_error_file)
        return " ".join((self.cmd,
                         self._parse_args(),
                         redirect_output_str,
                         redirect_error_str))

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
        allowed = string.digits + string.ascii_letters + '_-'
        return "".join([i for i in name if i in allowed])
        
    def _make_jobname(self, size=10, chars=string.ascii_letters):
        """Return random string.

        """
        return "".join(random.choice(chars) for x in range(size))

    def _build_dep_str_lsf(self):
        """Build LSF dependency string.

        """
        if len(self.dep.items()) == 0:
            self._dep_str_lsf = ""
        else:
            str_tmp = '-w "'
            for k, v in self.dep.items():
                str_tmp += "%s(%s)&&"%(k,v[0].name)
            if len(str_tmp) > 0:
                str_tmp = str_tmp[0:-2]
            str_tmp += '"'
            self._dep_str_lsf = str_tmp

    def _build_dep_str_slurm(self):
        """Build the SLURM dependency string.
        """
        if len(self.dep.items()) == 0 :
            self._dep_str_slurm  = ""
            return
        str_tmp = '--dependency='
        for k, v in self.dep.items():
            #TODO at somepoint allow for other dependency types besides afterok
            str_tmp +="afterok:$%s," % v[0].jobid
        #Delete the extra comma
        self._dep_str_slurm = str_tmp[0:-1]

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

    def add_positional_argument(self, arg, io_flag=None):
        """Method adds positional arguments to object.

        """
        handler = self.io_flag_handler.get(io_flag)
        if handler:
            handler(arg)
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
        if self.append_output_file:
            error = "Cannot redirect and append output"
            logger.error(error)
            exit(error)
        handler = self.io_flag_handler.get(io_flag)
        if handler:
            handler(outputfile)
        self.redirect_output_file = outputfile
        logger.info("%s: output_file attribute '%s' set for %s" % 
                    (self.name, self.output_file, self.cmd))

    def append_output(self, outputfile, io_flag=None):
        """Method to append output in the Unix sense.

        Has ability to set output as output file to be referenced.

        """
        if self.redirect_output_file:
            error = "Cannot redirect and append output"
            logger.error(error)
            exit(error)
        handler = self.io_flag_handler.get(io_flag)
        if handler:
            handler(outputfile)
        self.append_output_file = outputfile
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

