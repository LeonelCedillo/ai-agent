import os 

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath.join(working_directory, directory)

    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    contents_list = os.listdir(directory)
    info_lines = []
    for content in contents_list:
        size = os.path.getsize(content)
        is_dir = os.path.isdir(content)
        line = f"- {content}: file_size={size} bytes, is_dir={is_dir}"
        info_lines.append(line)
    info_str = "\n".join(info_lines)

