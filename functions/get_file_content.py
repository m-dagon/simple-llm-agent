from os.path import isfile
from os.path import abspath
from os.path import join
from os.path import basename
from functions.guard import guard
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        guard_result = guard(working_directory, file_path)
        if guard_result == 1:
            return f'Error: Cannot read "{basename(file_path)}" ' + \
            'as it is outside the permitted working directory'
        elif guard_result == 2:
            return f'Error: File not found or is not a regular file: "{basename(file_path)}"'

        file_abs_path = abspath(join(working_directory, file_path))
        with open(file_abs_path, "r") as f:
            if f.closed:
                raise Exception(f"...File {file_path} not opened.")
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == 10000:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        return str(file_content_string)
    except Exception as e:
        print(f"Error: {e}")


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads content of file specified by file_path, but limited to working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read from, relative to the working directory. If not provided, error string is returned.",
            ),
        },
    ),
)

