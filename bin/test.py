"""Test workflow on Kure.

"""
from tfpipe.modules.galaxy import FastqQualityFilter
from tfpipe.modules.gmap import Gsnap
from tfpipe.pipeline import WorkFlow

job1 = FastxClipper(name='kure_fastxqualityfilter',
                    args={'-i': '',
                          '-o': '',
                          '-Q': '33',
                          },)
job1.add_dependencies(done=[job1,])

job2 = Gsnap(name='kure_gsnap')
                    
