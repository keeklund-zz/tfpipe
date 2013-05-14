"""Test workflow on Kure.

"""
from tfpipe.modules.galaxy import FastqQualityFilter
from tfpipe.modules.gmap import Gsnap
from tfpipe.pipeline import WorkFlow

data_dir = '/proj/fureylab/data/Duke_DNasel_HS/GM12878/'
out_dir = '/proj/fureylab/karl/test/'

job1 = FastqQualityFilter(name='kure_fastxqualityfilter',
                          args={'-i': data_dir + 'wgEncodeOpenChromDnaseGm12878RawDataRep2.fastq',
                                '-o': out_dir + 'test.fastq',
                                '-Q': 33,
                                '-q': 20,
                                '-p': 100,
                                '-a': 'AAAAAAAAAA',
                                },)
job1.show()

#job2 = Gsnap(name='kure_gsnap')
#job2.show()

wf = WorkFlow([job1,])
wf.show()
