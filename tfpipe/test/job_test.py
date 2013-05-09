"""Unittest tests for tfpipe Job class.

"""
import unittest
from tfpipe.base import Job

class KnownValues(unittest.TestCase):
    def test_jobInit(self):
        """Job class must have a cmd associated with it."""
        self.assertRaises(AttributeError, Job)

    # another testcase showing cmd working?
    
    def test_job_input(self):
        pass
        
