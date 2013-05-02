"""Base.py holds common functionality for future classes.

"""

class CommandLine(object):
    """Generic Comand Line Interace functionality. 

    """
    def __init__(self, **inputs):
        """ 

        """
        self.cmd = self._init_arg(inputs, 'cmd')
        self.input_file = self._init_arg(inputs, 'input')
        self.output_file = self._init_arg(inputs, 'output')
        self.args = {}#self._init_arg(inputs, 'args')

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
        self.args[arg] = value

    def run(self):
        print str(self)
