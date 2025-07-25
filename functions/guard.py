from os.path import join
from os.path import abspath
from os.path import isdir
from os.path import exists

def guard(working_directory, directory):
    try:
        abs_working_dir = abspath(working_directory)
        abs_file_path = abspath(join(working_directory, directory))
        if not abs_file_path.startswith(abs_working_dir):
            return 1
        if not exists(abs_file_path):
            return 2
        if not abs_file_path.endswith(".py"):
            return 3

    except Exception as e:
        print(f"Error: {e}")
        return 2
    return 0
