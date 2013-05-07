"""FastqToFasta example script.

"""
# import modules needed to construct jobs
import tfpipe.modules.galaxy as galaxy
from tfpipe.pipeline import WorkFlow

# build first job
job1 = galaxy.FastqToFasta(cmd='new', 
                           args={'-i':'inputfile.fastq',
                                 '-o': 'outfile.fa'}, 
                           name='myfastq2a')
print job1.make_list()

# build second job
job2 = galaxy.FastxClipper()
job2.add_argument('-i', 'outfile.fa')
job2.add_argument('-o', 'newoutfile.fa')
job2.add_argument('-c')
job2.add_jobname("mySecondJob")
job2.add_dependency([job1,])

# add jobs to workflow
wf = WorkFlow([job1, job2])
wf.show()


"""
wf = WorkFlow()
wf.add_job(job1)
wf.add_job(job2, dep=job1)
"""
# will need to add dependencies to job once inside workflow
