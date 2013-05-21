"""Test workflow on Kure.

"""
from tfpipe.modules.galaxy import FastqQualityFilter, FastqToFasta
from tfpipe.modules.gmap import Gsnap
from tfpipe.modules.cli import CLI
from tfpipe.pipeline import WorkFlow

data_dir = '/proj/fureylab/data/Duke_DNasel_HS/GM12878/'
out_dir = '/proj/fureylab/karl/test/'

job1 = FastqQualityFilter(name='kure_fastqqualityfilter',
                          args={'-i': data_dir + 'wgEncodeOpenChromDnaseGm12878RawDataRep2.fastq',
                                '-Q': '33',
                                '-q': '20',
                                '-p': '100',
                                },)
job1.redirect_output(out_dir + 'test.fastq')

job2 = FastqToFasta(name='kure_fastq_to_fasta')
job2.add_argument('-i', out_dir + 'test.fastq')
job2.add_argument('-o', out_dir + 'test.fasta')
job2.add_dependencies(done=[job1,])

job_list = [job1, job2]

for i in range(1, 60):
    gsnap_args = {'--terminal-threshold=10': '',
                  '-n': '1',
                  '--genome-unk-mismatch=1': '',
                  '--query-unk-mismatch=1': '',
                  '-D': '/proj/fureylab/karl/pipeline_files/gmapdb/hg19_female_all/',
                  '-d': 'hg19_female',
                  '-v': 'CD_FAIRE.snps.gsnap',
                  '--trim-mismatch-score=0': '',
                  '-m': '1',
                  '-A': 'sam', 
                  '-i': '3',
                  '-k': '15',
                  '--basesize=12': '',
                  '--sampling=1': '',
                  '-q': '%s/60' % i,
                  '%s/test.fastq' % out_dir : ''}
    exec("gsnap_job%s = Gsnap(name='kure_gsnap%s', args=gsnap_args)" % (i, i))
    exec("gsnap_job%s.add_dependencies(done=[job1,])" % i)
    exec("gsnap_job%s.redirect_output('gsnap_out%s.sam')" % (i, i))
    job_list.append(eval("gsnap_job%s" % i))
         

merge_job = CLI(cmd="python /proj/fureylab/bin/merge_sam_files.py all.sam *.sam",
                dep_str='done("kure_gsnap*")')



job_list.append(merge_job)
wf = WorkFlow(job_list)
wf.run()

