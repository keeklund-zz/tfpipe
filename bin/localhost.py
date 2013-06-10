"""Example for pipeline on localhost.

Assumes jobs will run serially.

"""
# import modules needed to construct jobs
import tfpipe.modules.galaxy as galaxy
import tfpipe.modules.gmap as gmap
from tfpipe.modules.cli import CLI
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
job2.add_jobname("myFastxClipper")
job2.add_adapter_file('/home/karl/data/tfpipe/adapters')
job2.add_dependencies(done=[job1,])


job3 = CLI(cmd="ls -l")


# add jobs to workflow
wf = WorkFlow([job1, job2, job3], lsf=False)
wf.show()

