from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.call_function import call_function

from google import genai
from google.genai import types

from pydantic import BaseModel

def get_files_info_test():
    print(f'Test 1: \n{get_files_info("calculator", ".")}')
    print(f'Test 2: \n{get_files_info("calculator", "pkg")}')
    print(f'Test 3: \n{get_files_info("calculator", "/bin")}')
    print(f'Test 4: \n{get_files_info("calculator", "../")}')

def get_file_content_test():
    print(f'Test 1: \n{get_file_content("calculator", "main.py")}')
    print(f'Test 2: \n{get_file_content("calculator", "pkg/calculator.py")}')
    print(f'Test 3: \n{get_file_content("calculator", "bin/cat")}')
    print(f'Test 4: \n{get_file_content("calculator", "pkg/does_not_exist.py")}')

def write_file_test():
    write_file
    print(f'''Test 1: \n{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}''')

    print(f'Test 2: \n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
    print(f'Test 3: \n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')

def run_python_test():
    print(f'Test 1: \n{run_python_file("calculator", "main.py")}')
    print(f'Test 2: \n{run_python_file("calculator", "main.py", ["3 + 5"])}')
    print(f'Test 3: \n{run_python_file("calculator", "tests.py")}')
    print(f'Test 4: \n{run_python_file("calculator", "../main.py")}')
    print(f'Test 5: \n{run_python_file("calculator", "nonexistent.py")}')

def call_function_test():
    #call_function(types.FunctionCall(function_data), True)
    pass

get_file_content_test()
