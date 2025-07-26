from os.path import abspath
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import isfile

from functions.guard import guard
from google.genai import types

def write_file(working_directory, file_path, content):
    if guard(working_directory, file_path) != 0:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        abs_path = abspath(join(working_directory, file_path))
        if isdir(abs_path):
            return f'Error: {file_path} is a directory'
        with open(abs_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f'Error: {e}')

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to file at file_path, restricted by path of working directory. Overwrites file is it already exists.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to write to, relative to the working directory. If not provided, error string is returned.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that is a string that will be written to the file.",
            ),
        },
    ),
)
