==================
TerryFureyPipeLine
==================

tfpipe is short for Terry Furey Pipeline.  It is a simple framework for 
initializing and running workflows.  It generates pipeline workflows using the 
LSF scheduler on Kure.


Typical usage:
==============

#!/usr/bin/env python
    
from tfpipe.modules.galaxy import FastqToFasta
from tfpipe.pipeline import WorkFlow

extend example....


Installation:
=============

Initial install:
----------------

With root:
    pip:
        sudo pip install /path/to/dist/tfpipe-X.X.X.tar.gz

    No pip:
        tar zxf tfpipe-X.X.X.tar.gz
	cd tfpipe-X.X.X
	sudo python setup.py install

Without root:
    pip:
        pip install --user /path/to/dist/tfpipe-X.X.X.tar.gz

    no pip:
        tar zxf tfpipe-X.X.X.tar.gz
	cd tfpipe-X.X.X
	python setup.py install --user


Upgrade:
--------
    
?? need to double check this
sudo pip install -U /path/to/dist/tfpipe-X.X.X.tar.gz

