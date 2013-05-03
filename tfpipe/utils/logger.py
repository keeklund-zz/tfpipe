""" 

"""
import logging
import sys

# can have configuration file or object that can pull from to extend this

class Log(object):

    fmt = ('%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
    datefmt = '%y%m%d-%H:%M:%S'
    filename = '/tmp/tfpipe.log'

    def __init__(self, level='INFO'):
        logging.basicConfig(format=self.fmt, 
                            datefmt=self.datefmt,
                            filename=self.filename)
