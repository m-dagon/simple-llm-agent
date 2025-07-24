from os.path import join
from os.path import abspath
from os.path import isdir
from os.path import getsize
from os import listdir

from functions.working_directory_guard import guard

def get_files_info(working_directory, directory="."):
    try:
        if guard(working_directory, directory) != 0:
            return f'Error: Cannot list "{directory}" ' + \
            'as it is outside the permitted working directory'
        if not isdir(join(working_directory, directory)):
            return f'Error: "{directory}" is not a directory'
        files = []
        dir_abs_path = abspath(join(working_directory, directory))
        for item in listdir(dir_abs_path):
            is_dir = isdir(join(dir_abs_path, item))
            file_size = getsize(join(dir_abs_path, item))
            files.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            get_files_info(dir_abs_path, item)
        return "\n".join(files)
    except Exception as e:
        print(f"Error: {e}")


