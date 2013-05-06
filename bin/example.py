"""FastqToFasta example script.

"""

import tfpipe.modules.galaxy as galaxy

fq2a = galaxy.FastqToFasta(cmd='new', 
                           args={'-i':'otherinputfile.fastq'}, 
                           name='myfastq2a')
fq2a.add_argument('-o', 'myoutfile.fa')
fq2a.show()

fxc = galaxy.FastxClipper()
fxc.add_argument('-i', 'someinfile.fq')
fxc.add_argument('-o', 'someoutfile.fq')
fxc.add_argument('-c')
fxc.add_jobname("mySecondJob")
#fxc.add_dependency(fq2a)
fxc.show()

