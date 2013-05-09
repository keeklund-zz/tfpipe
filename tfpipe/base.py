"""Base.py holds common functionality for future classes.

"""
import string
import random

from tfpipe.utils import logger

# check how arguments are passed to object
# how will they know what arguments can be passed?
class Job(object):
    """Generic Job Interace functionality. 

    """
    dep_options = ('done', 'ended', 'exit', 'external',
                   'post_done', 'post_err', 'started')
    def __init__(self, **inputs):
        """Initialize Job.

        Objects that inherit this class receive Job methods and attributes. 
        Those parent objects can also override the cmd attribute.

        Parameters:
        cmd, args, name, dep

        """
        super(Job, self).__init__()
        self.cmd = inputs.get('cmd', None)
        self.args = inputs.get('args', {}) # needs to be dictionary of lists
        self.name = inputs.get('name', self._make_jobname())
        self.dep_str = inputs.get('dep_str', '')
        self.dep = self._initialize_dependencies(inputs)
        if self.cmd is None:
            self.cmd = self._cmd
        logger.info("%s: initialized with '%s' arguments and command: %s " % 
                    (self.name, self._parse_args(), self.cmd))

    def _initialize_dependencies(self, inputs):
        """Method to initialize job dependencies.

        Initializes dictionary of LSF Dependency Condition keys with empty list
        values.

        """
        tmp = {depopt:[] for depopt in self.dep_options}
        for key, value in inputs.get('dep', ''):
            tmp[key].append(value)
        return tmp

    def __repr__(self):
        """Command Line representation."""
        return "%s(%r)" % (self.__class__, self.args)

    def __str__(self):
        """Represent object as string."""
        return " ".join((self.cmd, self._parse_args()))

    def _parse_args(self):
        return " ".join([" ".join((k, v)) for k, v in self.args.iteritems()])

    def _make_jobname(self, size=8, chars=string.ascii_letters):
        """Return random string."""
        return "".join(random.choice(chars) for x in range(size))

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
    def add_dependency(self, **kwargs):
        """Add dependencies to object.

        Method allows user to add dependency arguments to current job.  User 
        specifies under what dependency condition each job is located, and has 
        ability to specify the dependency string.  Dependency conditions must be
        of type list.

        If user does not specify a dependency string, tfpipe will make a best 
        guess based on keys from the dependency dictionary.  

        """
        self.dep_str = kwargs.pop('dep_str', self.dep_str)
        if len(self.dep_str) == 0:
            self.dep_str = "&&".join(kwargs.keys())
        for key, value in kwargs.iteritems():
            if isinstance(value, list):
                try:
                    self.dep[key] += list(value)
                except KeyError:
                    self.dep[key] = list(value)
            else:
                exit("Operand of dependency must be of type list.")
                logger.warn("Operand of dependency must be of type list.")

        self.dep = kwargs

    def show_as_list(self):
        """Output command as list.

        """
        l = [self.cmd, ]
        return l + list(reduce(lambda x, y: x + y, self.args.items()))

    def show(self):
        print str(self)

    def get_command(self):
        return str(self)


