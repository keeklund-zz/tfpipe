"""FastqToFasta example script."""

import tfpipe.modules.galaxy as galaxy

fq2a = galaxy.FastqToFasta()
fq2a.add_argument('-i', 'myfile.fq')
fq2a.add_argument('-o', 'myoutfile.fa')
fq2a.run()

fq2a = galaxy.FastqToFasta(cmd='fastqToFasta.1')
fq2a.add_argument('-i', 'myfile.fq')
fq2a.add_argument('-o', 'myoutfile.fa')
fq2a.run()

