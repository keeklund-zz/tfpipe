"""WorkFlow unittests.

"""
import unittest
from tfpipe.modules.galaxy import FastqToFasta, FastqQualityFilter
from tfpipe.modules.gmap import Gsnap
from tfpipe.pipeline import WorkFlow

class WorkFlowTest(unittest.TestCase):

    def setUp(self):
        """Set up a workflow.

        """
        fqqf = FastqQualityFilter(name='quality_filter',
                                  args={'-i': 'fastq.fq',
                                        '-o': 'qfastq.fq',
                                        '-Q': '33',
                                        '-q': '20',
                                        '-p': '90'})
        fq2a = FastqToFasta(name='fastq_to_fasta',
                            args={'-i': 'qfastq.fq',
                                  '-o': 'qfasta.fa'})
        fq2a.add_dependencies(done=[fqqf,])

        self.wf = WorkFlow([fqqf, fq2a])

    def test_workflow_create_submit_str(self):
        """Display workflow submission commands.

        """
        job_list = ["bsub -J quality_filter  -o quality_filter.out  fastq_quality_filter -Q 33 -o qfastq.fq -i fastq.fq -p 90 -q 20 ",
                    'bsub -J fastq_to_fasta -w "done(quality_filter)"  -o fastq_to_fasta.out  fastq_to_fasta -o qfasta.fa -i qfastq.fq ']
        for job, jl in zip(self.wf.jobs, job_list):
            self.assertEqual(self.wf._create_submit_str(job), jl)

# need to test job that doesn't have any dependencies
# add dependency condition, specify dep_str
# need way to validate dep_str
# check dep_str is built correctly
