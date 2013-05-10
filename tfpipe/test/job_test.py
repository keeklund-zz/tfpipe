"""Unittest tests for tfpipe Job class.

"""
import unittest
from tfpipe.base import Job
from tfpipe.modules.galaxy import FastqToFasta
from tfpipe.utils import InvalidInput, InvalidObjectCall
from tfpipe.utils import logger

class JobBadInput(unittest.TestCase):
    """Most of Job testing in following Test Class.

    Important to note that Job was written to be inheritted, not called 
    directly.

    """
    def test_job_input(self):
        """Job cannot be called directly."""
        self.assertRaises(InvalidObjectCall, Job)


class ModuleEmptyInit(unittest.TestCase):
    """Test initialization of module when key-word input arguments are empty.

    """
    def setUp(self):
        """Set up a job initialized with out input parameters.

        Job used in class test cases.

        """
        self.fq2a_job = FastqToFasta()

    def test_job_init_cmd(self):
        """Module should inherit job and initialize cmd."""
        self.assertEqual(self.fq2a_job.cmd, 'fastq_to_fasta')

    def test_job_init_args(self):
        """Module initialized without args, args should be empty dictionary."""
        self.assertDictEqual(self.fq2a_job.args, {})

    def test_job_init_name(self):
        """Module init without name, name should be random string, 8 letters."""
        self.assertTrue(len(self.fq2a_job.name) == 8)
        self.assertIsInstance(self.fq2a_job.name, str)

    def test_job_init_dep_str(self):
        """Module dependency string should be empty."""
        self.assertEqual(self.fq2a_job.dep_str, '')

    def test_job_init_dep_at_init(self):
        """Module if dep_string is empty, attribute False."""
        self.assertFalse(self.fq2a_job.dep_str_at_init)

    def test_job_init_dep(self):
        """Dependencies are empty, nested lists in a dictionary."""
        self.assertIsInstance(self.fq2a_job.dep, dict)
        for k in self.fq2a_job.dep.keys():
            self.assertIsInstance(self.fq2a_job.dep[k], list)
            self.assertEqual(self.fq2a_job.dep[k], [])

