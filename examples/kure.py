#!/usr/bin/env python 
"""Example pipeline using LSF on Kure.

"""
from os.path import basename as bname
from tfpipe.modules.galaxy import FastxTrimmer, FastqQualityFilter
from tfpipe.pipeline import WorkFlow

def main(args):
    
    job_list = []

    for input_file in args.files:

        filename = bname(input_file)

        trimmer = FastxTrimmer(name='%s_trim' % filename)
        trimmer.add_argument('-Q', '33')
        trimmer.add_argument('-l', args.num_bp)
        trimmer.add_argument('-o', 
                             pjoin(args.out_dir, ''.join(['t', filename])),
                             'output')
        job_list.append(trimmer)

        quality = FastqQualityFilter(name='%s_quality' % filename)
        quality.add_argument('-Q', '33')
        quality.add_argument('-i', trimmer.get_output_file(), 'input')
        quality.add_argument('-o', 
                             pjoin(args.out_dir, 
                                   ''.join(['q', trimmer.get_output_file()])),
                             'output')
        quality.add_argument('-q', args.quality)
        quality.add_argument('-p', args.percent)
        quality.add_dependencies(done=[trimmer,])
        job_list.append(quality)

    wf = WorkFlow(job_list)
    wf.run() if args.run else wf.show()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(prog='kure', usage='%(prog)s [options]')

    parser.add_argument('--num-bp', 
                        required=True,
                        help='Number of base pairs to keep.')
    parser.add_argument('--quality',
                        required=True,
                        help='Quality value used in filtering.')
    parser.add_argument('--percent',
                        required=True,
                        help='Percent value used in filtering.')
    parser.add_argument('--out-dir',
                        required=True,
                        help='Output directory.')
    parser.add_argument('files', 
                        nargs='+', 
                        help='Files to filter.')
    parser.add_argument('--run',
                        action='store_true',
                        default=False,
                        help='Boolean: run or show pipeline - default: False.')
    args = parser.parse_args()
    
    main(args)
