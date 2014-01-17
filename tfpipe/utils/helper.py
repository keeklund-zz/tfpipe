"""Simple, but common functions typically used in pipelines.

"""
def get_file_location_info(some_file):
    """Return path, filename, basename tuple.

    """
    try:
        path,filename = some_file.split('/')
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

