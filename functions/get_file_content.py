from os.path import isfile
from os.path import abspath
from os.path import join
from functions.working_directory_guard import guard
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        if guard(working_directory, file_path) != 0:
            return f'Error: Cannot read "{file_path}" ' + \
            'as it is outside the permitted working directory'

        file_abs_path = abspath(join(working_directory, file_path))
        if not isfile(file_abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_abs_path, "r") as f:
            if f.closed:
                raise Exception(f"...File {file_path} not opened.")
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == 10000:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return str(file_content_string)
    except Exception as e:
        print(f"Error: {e}")
