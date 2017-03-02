"""Defines functionality for pipeline.

"""
from re import findall
from os import system
from sys import exit
from datetime import datetime
from tfpipe.utils import logger, DuplicateJobNames

class WorkFlow(object):
    """WorkFlow creates and executes job submission statements.

    """
    def __init__(self, job_list=[], lsf=True, slurm=False, name=None, additionalmodules={}):
        """Initialize WorkFlow.

        Method sets job lists and environment.  Depending on the environment, 
        job names are checked before submission.

        """
        if not((not slurm and lsf) or (slurm and not lsf)):
            raise RuntimeError('You can only choose LSF or SLURM',
                                 'Can not process a workflow as only LSF or SLURM may be invoked')
        self.jobs = job_list
        #LSF for the moment overides SLURM
        if lsf and not slurm:
            self.lsf = True
            self.slurm = False
        elif not lsf and slurm:
            self.lsf = False
            self.slurm = True
        else:
            assert False
        self._check_jobnames()
        self.additionalmodules = additionalmodules
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
        if (len(set(job_names)) == len(job_names)) and (self.lsf or self.slurm):
            logger.info("WorkFlow job names are unique.")
        elif (self.lsf or self.slurm):
            DuplicateJobNames("WARNING: WorkFlow job names are NOT unique.")

    def _create_submit_str(self, job):
        """Build submission string.

        Use lsf scheduler, bsub, if self.lsf is True.

        """
        if self.lsf:
            jobsched_str = self._build_bsub(job) or ''
        elif self.slurm:
            jobsched_str = self._build_sbatch_pre(job) or ''
        else:
            assert False
        if job.redirect_output or job.redirect_error:
            job_str = '"' + str(job) + '"'
        else:
            job_str = str(job)
        if self.slurm:
            self.current_submit_str = jobsched_str + job_str + self._build_sbatch_post(job) + "\n"
        else:
            self.current_submit_str = jobsched_str + job_str + "\n"
        return self.current_submit_str

    #TODO Check to make sure comment below is NOT valid now?
    # need to check # of individual dep conds in dep_options equals number 
    # of jobs passed to each dep condition
    def _update_dep_str(self, job):
        """Updates lsf dependency string.

        Build dependency string using dep_str heuristic and the dependency condition variables
        specified in the add_dependency method.

        """
        dep_options = findall(r"[\w']+", job.dep_str)
        for depopt in set(dep_options):
            tmp_dep_str = job.dep_str.replace(depopt, depopt + "(%s)")
        job_deps = tuple([job.dep.get(jdo).pop(0).name for jdo in dep_options])
        return '-w \"%s\"' % (tmp_dep_str % job_deps)

    def _build_sbatch_pre(self, job):
        """Create the sbatch (SLURM) command submission string for the first part.

        """
        sbatch = "%s=$(sbatch -J %s %s -o %s " % (job.jobid, job.name,
                                             job.get_dep_str_slurm,
                                                job.job_output_file)
        if job.memory_req_slurm and len(job.memory_req_slurm)>0:
            sbatch += "--mem=%s " % (job.memory_req_slurm)
        if job.numberofprocesses > 1:
            sbatch += "-n %s " % str(job.numberofprocesses)
        sbatch += "--wrap="
        return sbatch

    def _build_sbatch_post(self, job):
        """Create the sbatch (SLURM) command submission string.

        """
        return ")\n%s=$(echo $%s | cut -d ' ' -f4)" % (job.jobid,job.jobid)

    def _build_bsub(self, job):
        """Create bsub (LSF) command submission string.

        """
        bsub = "bsub -J %s %s -o %s " % (job.name,
                                         job.get_dep_str,
                                                job.job_output_file)
        if job.memory_req_lsf:
            bsub += "-M %s " % (job.memory_req_lsf)
        if job.numberofprocesses > 1:
            bsub += '-n %d -R "span[hosts=1]" ' % (job.numberofprocesses)
        return bsub

    def add_job(self, newjob):
        """Add job to list.

        """
        self.jobs.append(newjob)
        logger.info("WorkFlow ADD: %s" % newjob)

    def _build_shell_script_to_text(self):
        """Builds and returns a shell script as a string.

        :return: A string composed of the executable shell script.
        """
        mods = []
        output = "#!/bin/bash\n"
        output += ". /nas02/apps/Modules/default/init/bash\n"
        for job in self.jobs:
            try:
                if self.slurm:
                    if hasattr(job,'module_slurm'):
                        if job.module_slurm not in mods:
                            output += "module load %s\n" % job.module_slurm
                            mods.append(job.module_slurm)
                    else:
                        # If you can't find a slurm specific module, then use the default (LSF)
                        if job.module not in mods:
                            output += "module load %s\n" % job.module
                            mods.append(job.module)
                elif self.lsf:
                    if job.module not in mods:
                        output += "module load %s\n" % job.module
                        mods.append(job.module)
                elif not self.lsf and not self.slurm:
                    assert False
            except AttributeError:
                # If there is no module then do nothing.
                pass
        for module in self.additionalmodules:
            try:
                if module not in mods:
                    output += "module load %s\n" % module
                    mods.append(module)
            except AttributeError:
                pass
        for job in self.jobs:
            output += self._create_submit_str(job)
        return output

    def show(self):
        """Method prints out the shell script to stdout

        """
        submit_str = self._build_shell_script_to_text()
        print submit_str
        logger.info("WorkFlow SHOW: %s" % submit_str)
            
    def run(self):
        """Method submits command list to shell.

        """
        with open(self._shell_script, 'w') as f:
            f.write(self._build_shell_script_to_text())
        system("bash %s" % self._shell_script)
        logger.info("WorkFlow SUBMIT: %s" % self._shell_script)
