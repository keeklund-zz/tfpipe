
tfpipe

    tfpipe is short for Terry Furey Pipeline.  It is a simple framework for 
    initializing and running workflows.  It generates pipeline workflows 
    using the LSF scheduler on Kure.


Typical usage:

    #!/usr/bin/env python
    
    from tfpipe.modules.galaxy import FastqToFasta
    from tfpipe.pipeline import engine

    extend example....


Installation:
    
    Initial install:
        
	sudo pip install /path/to/dist/tfpipe-X.X.X.tar.gz

    Upgrade:

	?? need to double check this
	sudo pip install -U /path/to/dist/tfpipe-X.X.X.tar.gz



