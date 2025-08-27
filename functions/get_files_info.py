import os 

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath.join(working_directory, directory)

    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    contents = os.listdir(directory)
    for content in contents:
        size = os.path.getsize(content)
        is_file = os.path.isfile(content)
        
