""" 

"""
from os import path
import logging
import logging.config

conffile = path.join(path.dirname(path.abspath(__file__)), 'log.conf')
logging.config.fileConfig(conffile)
    

# create logger
logger = logging.getLogger("testing")
