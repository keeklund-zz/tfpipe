"""WorkFlow unittests.

"""
import unittest
from tfpipe.modules.galaxy import FastqToFasta, FastqQualityFilter
from tfpipe.modules.gmap import Gsnap
from tfpipe.pipeline import WorkFlow
from tfpipe.utils import DuplicateJobNames

# to unittest:
# ['_build_bsub', '_build_shell_script', '_create_submit_list', '_create_submit_str', '_shell_script', '_update_dep_str', 'add_job', 'jobs', 'lsf', 'run', 'show']

class WorkFlowTest(unittest.TestCase):
    """Test functionality of workflow with sample jobs.

    """
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
    
    def test_check_jobnames(self):
        """Method makes sure job names are unique.

        Raises DuplicateJobNames exception if jobnames are not unique.

        """
        qf = FastqQualityFilter(name="job")
        qa = FastqToFasta(name="job")
        self.assertRaises(DuplicateJobNames, wf = WorkFlow([qf, qa]))
        
# need to test job that doesn't have any dependencies
# add dependency condition, specify dep_str
# need way to validate dep_str
# check dep_str is built correctly
