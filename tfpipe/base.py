"""Base.py holds common functionality for future classes.

"""
import string
import random
from subprocess import Popen

from tfpipe.utils import logger
from tfpipe.utils import InvalidInput, InvalidObjectCall

class Job(object):
    """Generic Job Interace functionality. 

    """
    # best place to put these?
    dep_options = ('done', 'ended', 'exit', 'external',
                   'post_done', 'post_err', 'started')
    init_options = ('cmd', 'args', 'name', 'dep_str')
    def __init__(self, **inputs):
        """Initialize Job.

        Objects that inherit this class receive Job methods and attributes. 
        Those parent objects can also override the cmd attribute.

        Parameters:
        cmd, args, name, dep, dep_str

        """
        # initialize with deps too
        message = "Illegal input argument pass during init."
        self._check_valid_input_options(self.init_options, 
                                        inputs.keys(),
                                        message)
        if not hasattr(self, '_cmd'):
            raise InvalidObjectCall, "This object cannot be called directly."
        if hasattr(self, '_module'):
            try:
                p = Popen("module add %s" % self._module)
                p.wait()
                logger.info("module '%s' added" % self._module)
            except OSError:
                pass
#        super(Job, self).__init__()
        self.cmd = inputs.get('cmd', self._cmd)
        self.args = inputs.get('args', {}) 
        self.name = inputs.get('name', self._make_jobname())
        self.dep_str = inputs.get('dep_str', '')
        self.dep_str_at_init = bool(self.dep_str)
        self.dep = self._initialize_dependencies(inputs)
        logger.info("%s: initialized with '%s' arguments and command: %s " % 
                    (self.name, self._parse_args(), self.cmd))

    def __repr__(self):
        """Command Line representation."""
        return "%s(%r)" % (self.__class__, self.args)

    def __str__(self):
        """Represent object as string."""
        return " ".join((self.cmd, self._parse_args()))

    def _initialize_dependencies(self, inputs):
        """Method to initialize job dependencies.

        Initializes dictionary of LSF Dependency Condition keys with empty list
        values.

        """
        # initialize deps here too
        tmp = dict((depopt, []) for depopt in self.dep_options)
        for key, value in inputs.get('dep', ''):
            tmp[key].append(value)
        return tmp

    def _check_valid_input_options(self, options, input_keys, message):
        """Hidden method checks input values."""
        if sum([args not in options for args in input_keys]):
            raise InvalidInput, message

    def _parse_args(self):
        return " ".join([" ".join((k, v)) for k, v in self.args.iteritems()])

    def _make_jobname(self, size=8, chars=string.ascii_letters):
        """Return random string."""
        return "".join(random.choice(chars) for x in range(size))

    def _build_dep_str(self):
        """Build LSF dependency string."""
        str_tmp = " ".join([(k + " ") * len(v) for k, v in self.dep.items() 
                            if len(v) > 0])
        self.dep_str = "&&".join(str_tmp.split())

    def add_argument(self, arg, value=None):
        """Method adds command line arguments to object.

        """
        self.args[arg] = True and value or ''
        logger.info("%s: argument '%s %s' added to %s" % 
                    (self.name, arg, self.args[arg], self.cmd))

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
        print str(self)

    def get_command(self):
        return str(self)


