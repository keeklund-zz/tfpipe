"""FastqToFasta example script.

"""

import tfpipe.modules.galaxy as galaxy

job1 = galaxy.FastqToFasta(cmd='new', 
                           args={'-i':'otherinputfile.fastq'}, 
                           name='myfastq2a')
job1.add_argument('-o', 'myoutfile.fa')
job1.show()

job2 = galaxy.FastxClipper()
job2.add_argument('-i', 'someinfile.fq')
job2.add_argument('-o', 'someoutfile.fq')
job2.add_argument('-c')
job2.add_jobname('mySecondJob')
job2.show()

