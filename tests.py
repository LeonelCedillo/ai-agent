from functions.get_files_info import get_files_info

def tests():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")
    # Result for current directory:
    #  - main.py: file_size=576 bytes, is_dir=False
    #  - tests.py: file_size=1343 bytes, is_dir=False
    #  - pkg: file_size=92 bytes, is_dir=True

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    # Result for 'pkg' directory:
    #  - calculator.py: file_size=1739 bytes, is_dir=False
    #  - render.py: file_size=768 bytes, is_dir=False

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    # Result for '/bin' directory:
    #     Error: Cannot list "/bin" as it is outside the permitted working directory

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    # Result for '../' directory:
    #     Error: Cannot list "../" as it is outside the permitted working directory



if __name__ == "__main__":
    tests()