import os 

def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try: 
        contents_list = os.listdir(full_path)
        info_lines = []
        for content in contents_list:
            size = os.path.getsize(os.path.join(full_path, content))
            is_dir = os.path.isdir(os.path.join(full_path, content))
            line = f"- {content}: file_size={size} bytes, is_dir={is_dir}"
            info_lines.append(line)
        info = "\n".join(info_lines)
        return info
    except Exception as e:
        return f"Error: {e}"

