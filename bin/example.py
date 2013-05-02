"""FastqToFasta example script."""

import tfpipe.modules.galaxy as galaxy

fq2a = galaxy.FastqToFasta()
fq2a.add_argument('-i', 'myfile.fq')
fq2a.add_argument('-o', 'myoutfile.fa')
fq2a.run()

fxc = galaxy.FastxClipper()
fxc.add_argument('-i', 'someinfile.fq')
fxc.add_argument('-o', 'someoutfile.fq')
fxc.add_argument('-c')
fxc.run()

