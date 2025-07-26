import copy

# os paths
from os.path import abspath
from os.path import join
from os.path import exists
from os.path import isdir
from os.path import isfile

# config
from config import WORKING_DIRECTORY

# genai
from google.genai import types

# functions
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    cwd=WORKING_DIRECTORY
    function_name=function_call_part.name
    function_id=function_call_part.id
    new_args=copy.deepcopy(function_call_part.args)
    new_args["working_directory"]=cwd
    print(new_args)
    match function_name:
        case 'get_files_info':
            function_result = get_files_info(**new_args)
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                    )
                ],
            )
        case 'get_file_content':
            function_result = get_file_content(**new_args)
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                    )
                ],
            )
        case 'write_file':
            function_result = write_file(**new_args)
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                    )
                ],
            )

        case 'run_python_file':
            function_result = run_python_file(**new_args)
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"result": function_result},
                    )
                ],
            )

        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )


