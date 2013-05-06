"""Base.py holds common functionality for future classes.

"""
import string
import random

from tfpipe.utils import logger

# check how arguments are passed to object
# how will they know what arguments can be passed?
class CommandLine(object):
    """Generic Comand Line Interace functionality. 

    """
    def __init__(self, **inputs):
        """Initialize CommandLine.

        Objects that inherit this class receive CommandLine 
        methods and attributes.  Those parent objects can 
        also override the cmd attribute.

        """
        super(CommandLine, self).__init__()
        self.cmd = inputs.get('cmd', None)
        self.args = inputs.get('args', {})
        self.name = inputs.get('name', self._make_jobname())
        if self.cmd is None:
            self.cmd = self._cmd
        logger.info("%s: initialized with '%s' arguments and command: %s " % 
                    (self.name, self._parse_args(), self.cmd))

    def _parse_args(self):
        return " ".join([" ".join((k, v)) for k, v in self.args.iteritems()])

    def __repr__(self):
        """Command Line representation."""
        return "%s(%r)" % (self.__class__, self.args)

    # should this be used in this way?
    # imagine there is a better way 
    def __str__(self):
        """Represent object as string."""
        return " ".join((self.cmd, self._parse_args()))

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

    def show(self):
        print str(self)

    def get_command(self):
        return str(self)

    def _make_jobname(self, size=8, chars=string.ascii_letters):
        """Return random string."""
        return "".join(random.choice(chars) for x in range(size))
