"""Unittest tests for tfpipe Job class.

"""
import unittest
from tfpipe.base import Job
from tfpipe.utils import InvalidInput

class JobBadInput(unittest.TestCase):
    def test_jobInit(self):
        """Job class must have a cmd associated with it."""
        self.assertRaises(AttributeError, Job)

    # is this even possible?
    def test_job_input(self):
        """Raise InvalidInput Exception when initialized with invalid input."""
        inputs = {'name':['stuff', 'goes', 'here'],
                  'cmd':'ls'}
        self.assertRaises(InvalidInput, Job, **inputs)
        
