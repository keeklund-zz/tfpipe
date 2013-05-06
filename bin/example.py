"""FastqToFasta example script.

"""
# import modules needed to construct jobs
import tfpipe.modules.galaxy as galaxy
from tfpipe.pipeline import WorkFlow

# build first job
job1 = galaxy.FastqToFasta(cmd='new', 
                           args={'-i':'otherinputfile.fastq',
                                 '-o': 'myoutfile.fa'}, 
                           name='myfastq2a')

# build second job
job2 = galaxy.FastxClipper()
job2.add_argument('-i', 'someinfile.fq')
job2.add_argument('-o', 'someoutfile.fq')
job2.add_argument('-c')
job2.add_jobname("mySecondJob")
job2.add_dependency([job1,])

# add jobs to workflow
wf = WorkFlow([job1, job2])
wf.show()
