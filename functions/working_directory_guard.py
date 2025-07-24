from os.path import join
from os.path import abspath
from os.path import isdir

def guard(working_directory, directory):
    try:
        working_abs_path = abspath(working_directory)
        current_abs_path = abspath(join(working_directory, directory))
        if working_directory == None or \
        working_directory == "" or \
        not current_abs_path.startswith(working_abs_path):
            return 1

    except Exception as e:
        print(f"Error: {e}")
        return 2
    return 0
