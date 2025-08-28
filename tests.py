# TESTS FOR FUNCTION: get_files_info
# from functions.get_files_info import get_files_info

# def tests():
#     result = get_files_info("calculator", ".")
#     print("Result for current directory:")
#     print(result)
#     print("")
#     # Result for current directory:
#     #  - main.py: file_size=576 bytes, is_dir=False
#     #  - tests.py: file_size=1343 bytes, is_dir=False
#     #  - pkg: file_size=92 bytes, is_dir=True

#     result = get_files_info("calculator", "pkg")
#     print("Result for 'pkg' directory:")
#     print(result)
#     # Result for 'pkg' directory:
#     #  - calculator.py: file_size=1739 bytes, is_dir=False
#     #  - render.py: file_size=768 bytes, is_dir=False

#     result = get_files_info("calculator", "/bin")
#     print("Result for '/bin' directory:")
#     print(result)
#     # Result for '/bin' directory:
#     #     Error: Cannot list "/bin" as it is outside the permitted working directory

#     result = get_files_info("calculator", "../")
#     print("Result for '../' directory:")
#     print(result)
#     # Result for '../' directory:
#     #     Error: Cannot list "../" as it is outside the permitted working directory



# if __name__ == "__main__":
#     tests()





# TESTS FOR FUNCTION: get_file_content
# from functions.get_file_content import get_file_content

# def tests():
#     # result = get_file_content("calculator", "lorem.txt")
#     # print("Result for lorem.txt:")
#     # print(result)
#     # print("")
    
#     result = get_file_content("calculator", "main.py")
#     print("Result for main.py:")
#     print(result)
#     print("")

#     result = get_file_content("calculator", "pkg/calculator.py")
#     print("Result for pkg/calculator.py:")
#     print(result)
#     print("")

#     result = get_file_content("calculator", "/bin/cat") # (this should return an error string)
#     print("Result for /bin/cat:")
#     print(result)
#     print("")

#     result = get_file_content("calculator", "pkg/does_not_exist.py") # (this should return an error string)
#     print("Result for pkg/does_not_exist.py:")
#     print(result)
#     print("")


# if __name__ == "__main__":
#     tests()







# TESTS FOR FUNCTION: get_file_content
# from functions.write_file import write_file

# def tests():
#     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     print("Result for lorem.txt:")
#     print(result)
#     print("")

#     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     print("Result for pkg/morelorem.txt:")
#     print(result)
#     print("")

#     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#     print("Result for /tmp/temp.txt:")
#     print(result)
#     print("")


# if __name__ == "__main__":
#     tests()





# TESTS FOR FUNCTION: run_python_file
from functions.run_python import run_python_file

def tests():
    result = run_python_file("calculator", "main.py") # (should print the calculator's usage instructions)
    print("Result for main.py:")
    print(result)
    print("")

    result = ("calculator", "main.py", ["3 + 5"]) # (should run the calculator... which gives a kinda nasty rendered result)
    print("Result for main.py, [3 + 5]:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for tests.py:")
    print(result)
    print("")
    
    result = run_python_file("calculator", "../main.py") # (this should return an error)
    print("Result for ../main.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py") # (this should return an error)
    print("Result for nonexistent.py:")
    print(result)
    print("")


if __name__ == "__main__":
    tests()