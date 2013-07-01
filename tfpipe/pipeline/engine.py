"""Defines functionality for pipeline.

"""
from re import findall
from os import system, environ, path
from sys import exit
from datetime import datetime
from tfpipe.utils import logger, DuplicateJobNames

class WorkFlow(object):
    """WorkFlow creates and executes job submission statements.

    """
    def __init__(self, job_list=[], lsf=True, name=None):
        """Initialize WorkFlow.

        Method sets job lists and environment.  Depending on the environment, 
        job names are checked before submission.

        """
        self.jobs = job_list
        self.lsf = lsf
        self._check_jobnames()
        now = datetime.now()
        if not name:
            self._shell_script = '%s_tfpipe_workflow.sh' % \
                now.strftime("%Y%m%d%H%M%S")
        else:
            self._shell_script = name
        logger.info("WorkFlow created")

    def _check_jobnames(self):
        """Method to check job names for duplicates.

        WorkFlow terminates if duplicate is found in LSF mode.

        """
        job_names = [job.name for job in self.jobs]
        if (len(set(job_names)) == len(job_names)) and self.lsf:
            logger.info("WorkFlow job names are unique.")
        elif self.lsf:
            DuplicateJobNames("WARNING: WorkFlow job names are NOT unique.")

    def _create_submit_str(self, job):
        """Build submission string.

        Use lsf scheduler, bsub, if self.lsf is True.

        """
        bsub_str = self._build_bsub(job) if self.lsf else ''
        job_str = job.redirect and '"' + str(job) + '"' or str(job)
        self.current_submit_str = bsub_str + job_str
        return self.current_submit_str

    def _create_submit_list(self, job):
        """Build list of submission command.
        
        Use lsf scheduler, bsub, if self.lsf is True.

        """
        bsub = self._build_bsub(job).split() if self.lsf else []
        submission_list = bsub + ['"',] + job.show_as_list() + ['"',]
        self.current_submit_str = " ".join(submission_list)
        return submission_list
        
    # need to check # of individual dep conds in dep_options equals number 
    # of jobs passed to each dep condition
    def _update_dep_str(self, job):
        """Updates lsf dependency string.

        If dependency string was set explicitly during initialization, return 
        the dependency specified at initialization.  Otherwise, build dependency
        string using dep_str heuristic and the dependency condition variables 
        specified in the add_dependency method.

        """
        if job.dep_str_at_init:
            return '-w \"%s\" ' % job.dep_str
        dep_options = findall(r"[\w']+", job.dep_str) 
        for depopt in set(dep_options):
            tmp_dep_str = job.dep_str.replace(depopt, depopt + "(%s)")
        job_deps = tuple([job.dep.get(jdo).pop(0).name for jdo in dep_options])
        return '-w \"%s\" ' % (tmp_dep_str % job_deps)

    def _build_bsub(self, job):
        """Create bsub command submission string.

        """
        if len(job.dep_str) == 0:
            job._build_dep_str()
        bargs = ' '.join(["%s %s" % (k, v) for k, v in job.bsub_args.items()])
        bdep = self._update_dep_str(job) if job.dep_str else ''
        bsub = "bsub -J %s %s -o %s.out %s " % (job.name, 
                                                bdep,
                                                job.name, 
                                                bargs)
        job_str = str(job)
        if job_str.count('|'):
            if (job_str.count('|')+1) > 8:
                exit("Too many threads.  Adapter file must be eight or less.")
            bsub += '-n %d -R "span[hosts=1]" ' % (job_str.count('|') + 1)
        return bsub

    def _build_shell_script(self):
        """ """
        mods = []
        with open(self._shell_script, 'w') as f:
            f.write("#!/bin/bash\n")
            if self.lsf:
                f.write(". /nas02/apps/Modules/default/init/bash\n")
                for job in self.jobs:
                    try:
                        if job._module not in mods:
                            f.write("module load %s\n" % job._module)
                            mods.append(job._module)
                    except AttributeError:
                        pass
            for job in self.jobs:
                f.write("%s\n" % self._create_submit_str(job))
        logger.info("WorkFlow Submission Script Created")

    def add_job(self, newjob):
        """ """
        pass

    def show(self):
        """Method shows all job submission strings and lists in WorkFlow.

        """
        for job in self.jobs:
            submit_str = self._create_submit_str(job)
            print submit_str
            logger.info("WorkFlow SHOW: %s" % submit_str)
            
    def run(self):
        """Method submits command list to shell.

        """
        self._build_shell_script()
        system("bash %s" % self._shell_script)
        logger.info("WorkFlow SUBMIT: %s" % self._shell_script)


