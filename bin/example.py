"""FastqToFasta example script."""

from tfpipe.modules.galaxy import FastqToFasta

fq2a = FastqToFasta()
fq2a.add_argument('-i', 'myfile.fq')
fq2a.add_argument('-o', 'myoutfile.fa')
fq2a.run()

fq2a = FastqToFasta(cmd='fastqToFasta.1')
fq2a.add_argument('-i', 'myfile.fq')
fq2a.add_argument('-o', 'myoutfile.fa')
fq2a.run()
