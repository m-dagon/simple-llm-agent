from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def get_files_infor_test():
    print(f'Test 1: \n{get_files_info("calculator", ".")}')
    print(f'Test 2: \n{get_files_info("calculator", "pkg")}')
    print(f'Test 3: \n{get_files_info("calculator", "/bin")}')
    print(f'Test 4: \n{get_files_info("calculator", "../")}')

def get_file_content_test():
    print(f'Test 1: \n{get_file_content("calculator", "main.py")}')
    print(f'Test 2: \n{get_file_content("calculator", "pkg/calculator.py")}')
    print(f'Test 3: \n{get_file_content("calculator", "bin/cat")}')
    print(f'Test 4: \n{get_file_content("calculator", "pkg/does_not_exist.py")}')


get_file_content_test()
