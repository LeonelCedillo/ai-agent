get_files_info("calculator", "."):
# Result for current directory:
#  - main.py: file_size=576 bytes, is_dir=False
#  - tests.py: file_size=1343 bytes, is_dir=False
#  - pkg: file_size=92 bytes, is_dir=True

get_files_info("calculator", "pkg"):
# Result for 'pkg' directory:
#  - calculator.py: file_size=1739 bytes, is_dir=False
#  - render.py: file_size=768 bytes, is_dir=False

get_files_info("calculator", "/bin"):
# Result for '/bin' directory:
#     Error: Cannot list "/bin" as it is outside the permitted working directory

get_files_info("calculator", "../"):
# Result for '../' directory:
#     Error: Cannot list "../" as it is outside the permitted working directory