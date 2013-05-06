"""Defines functionality for pipeline.

"""

class WorkFlow(object):
    """

    """
    bsub = "bsub "
    def __init__(self, job_list=[]):
        self.jobs = job_list
        

    def add_job(self, newjob):
        """ """
        pass

    # check order of jobs
    def show(self):
        for job in self.jobs:
            print job
    

# possible to add attributes to job from within workflow?
# need ability to specify how dependency should work, whether 
# it's done, exited, ended, etc.

