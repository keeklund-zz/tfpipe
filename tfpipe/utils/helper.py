"""Simple, but common functions typically used in pipelines.                   

"""
from mimetypes import guess_type
from os.path import dirname
from os.path import basename as bname
from os.path import join as path_join

def get_file_location_info(some_file):
    """Return path, filename, basename tuple.                                      
                                                                                   
    """
    try:
        path = dirname(some_file)
        filename = bname(some_file)
    except ValueError:
        path, filename = ('.', some_file)
    basename = '.'.join(filename.split('.')[:-1])
    if guess_type(some_file)[1] is 'gzip':
        basename = '.'.join(basename.split('.')[:-1])
    return (path, filename, basename)

def build_output(out_dir, prepend, basename, ext):
    """Return simple path join of required input.                                  
                                                                                   
    """
    return path_join(out_dir, ''.join([prepend, basename, ext]))






