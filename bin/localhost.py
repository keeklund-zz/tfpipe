"""Example for pipeline on localhost.

Assumes jobs will run serially.

"""
# import modules needed to construct jobs
import tfpipe.modules.galaxy as galaxy
from tfpipe.pipeline import WorkFlow


# data init
data_dir = '/home/karl/data/tfpipe/'


# build first job
job1 = galaxy.FastqToFasta(args={'-i':data_dir + 'rep2.fastq',
                                 '-o': data_dir + 'rep2.fasta',
                                 '-Q': '33'}, 
                           name='myfastq2a')

# build second job
job2 = galaxy.FastxClipper()
job2.add_argument('-i', data_dir + 'rep2.fasta')
job2.add_argument('-o', data_dir + 'newoutfile.fa')
job2.add_argument('-C')
job2.add_jobname("mySecondJob")
job2.add_dependency([job1,])

# add jobs to workflow
wf = WorkFlow([job1, job2], lsf=False)
wf.run()

