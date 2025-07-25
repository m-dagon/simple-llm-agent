from config import *
from functions.guard import guard
from subprocess import run
from os.path import join
from os.path import abspath
from os.path import exists
from os.path import isfile
from os.path import basename

def run_python_file(working_directory, file_path, args=[]):
    guard_result = guard(working_directory, file_path)
    if guard_result == 1:
        return f'Error: Cannot execute "{basename(file_path)}" as it is outside the permitted working directory'
    elif guard_result == 2:
        return f'Error: File "{basename(file_path)}" not found.'
    elif guard_result == 3:
        return f'Error: "{basename(file_path)}" is not a Python file.'
    elif guard_result != 0:
        return f'Error: "Working directory guard failure.'
    try:
        new_args = ["python"]
        new_args.append(file_path)
        new_args += args
        result = run(
            args=new_args,
            cwd=abspath(working_directory),
            shell=SUBPROCESS_USE_SHELL,
            capture_output=SUBPROCESS_CAPTURE_OUTPUT,
            timeout=SUBPROCESS_TIMEOUT,
            text=SUBPROCESS_TEXT
        )
        output = ""
        if result.stdout:
            output += f'STDOUT:\n{result.stdout}'
        if result.stderr:
            output += f'STDERR:\n{result.stderr}'
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}'
        if output == "":
            output += "No output produced."
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
