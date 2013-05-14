"""Test workflow on Kure.

"""
from tfpipe.modules.galaxy import FastqQualityFilter, FastqToFasta
from tfpipe.modules.gmap import Gsnap
from tfpipe.pipeline import WorkFlow

data_dir = '/proj/fureylab/data/Duke_DNasel_HS/GM12878/'
out_dir = '/proj/fureylab/karl/test/'

job1 = FastqQualityFilter(name='kure_fastqqualityfilter',
                          args={'-i': data_dir + 'wgEncodeOpenChromDnaseGm12878RawDataRep2.fastq',
                                '-o': out_dir + 'test.fastq',
                                '-Q': '33',
                                '-q': '20',
                                '-p': '100',
                                },)

job2 = FastqToFasta(name='kure_fastq_to_fasta')
job2.add_argument('-i', out_dir + 'test.fastq')
job2.add_argument('-o', out_dir + 'test.fasta')
job2.add_dependencies(done=[job1,])

#job2 = Gsnap(name='kure_gsnap')
#job2.show()

wf = WorkFlow([job1, job2])
wf.run()
