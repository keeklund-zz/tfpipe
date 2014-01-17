"""tfpipe setup script. """

from distutils.core import setup

setup(
    name='tfpipe',
    version='0.1.5',
    author='Karl Eklund',
    author_email='keklund@email.unc.edu',
    packages=['tfpipe', 
              'tfpipe.utils',
              'tfpipe.modules', 
              'tfpipe.modules.cli',
              'tfpipe.modules.gmap',
              'tfpipe.modules.mach',
              'tfpipe.modules.plink',
              'tfpipe.modules.galaxy',
              'tfpipe.modules.picard',
              'tfpipe.modules.tophat',
              'tfpipe.modules.dfilter',
              'tfpipe.modules.tagdust',
              'tfpipe.modules.bedtools',
              'tfpipe.modules.samtools',
              'tfpipe.modules.cufflinks',
              'tfpipe.pipeline',],
    scripts=['bin/tfpipe_run',
             'examples/localhost.py',
             'examples/kure.py'],
    url='http://fureylab.web.unc.edu',
    license='LICENSE.txt',
    description='Terry Furey Lab Pipeline',
    long_description=open('README.txt', 'r').read(),
)

#    install_requires=[],
