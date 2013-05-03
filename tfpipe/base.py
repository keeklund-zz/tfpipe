"""Base.py holds common functionality for future classes.

"""
from os import path
import logging
import logging.config

conffile = path.join(path.dirname(path.abspath(__file__)), 'log.conf')
logging.config.fileConfig(conffile)
logger = logging

# check how arguments are passed to object
class CommandLine(object):
    """Generic Comand Line Interace functionality. 

    """
    def __init__(self, **inputs):
        """Initialize CommandLine.

        Objects that inherit this class receive CommandLine 
        methods and attributes.  Those parent objects can 
        also override the cmd attribute.

        """
        super(CommandLine, self).__init__(**inputs)
        self.cmd = self._init_arg(inputs, 'cmd')
        self.input_file = self._init_arg(inputs, 'input')
        self.output_file = self._init_arg(inputs, 'output')
        self.args = {} # self._init_arg(inputs, 'args')
        if self.cmd is None:
            self.cmd = self._cmd
        logger.info("%s initialized with '%s' input, '%s' output" % 
                    (self.cmd, self.input_file, self.output_file))

    def _init_arg(self, inputs, arg_key):
        """Initialize arguments passed to class.

        """
        try:
            return inputs[arg_key]
        except KeyError:
            return None

    def __repr__(self):
        """Command Line representation."""
        return "%s(%r)" % (self.__class__, self.args)

    # should this be used in this way?
    # imagine there is a better way 
    def __str__(self):
        """Represent object as string."""
        tmp = " ".join([" ".join((k, v)) for k, v in self.args.iteritems()])
        return " ".join((self.cmd, tmp))

    def add_argument(self, arg, value=None):
        """Method adds command line arguments to object.

        """
        self.args[arg] = True and value or ''
        logger.info("argument '%s %s' added to %s" % 
                    (arg, self.args[arg], self.cmd))

    def show(self):
        print str(self)

    def get_command(self):
        return str(self)

