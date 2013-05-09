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

# build second job
job2 = galaxy.FastxClipper()
job2.add_argument('-i', 'outfile.fa')
job2.add_argument('-o', 'newoutfile.fa')
job2.add_argument('-C')
job2.add_jobname("mySecondJob")
job2.add_dependency(done=[job1,])

# build third job
job3 = galaxy.FastxClipper()
job3.add_argument('-c')
job3.add_dependency(done=[job1, job2], dep_str="done||done")

# build fourth job
job4 = galaxy.FastxClipper()
job4.add_argument('','')
job4.add_dependency(done=[job1,])

# add jobs to workflow
wf = WorkFlow([job1, job2, job3, job4])
wf.show()

