from os.path import abspath
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import isfile

from functions.guard import guard

def write_file(working_directory, file_path, content):
    if guard(working_directory, file_path) != 0:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        abs_path = abspath(join(working_directory, file_path))
        if isdir(abs_path):
            return f'Error: {file_path} is a directory'
        if exists(abs_path) and isfile(abs_path):
            with open(abs_path, "w") as f:
                f.write(content)
        elif exists(abs_path):
            with open(abs_path, "w") as f:
                f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f'Error: {e}')

