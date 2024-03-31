import os

def create_folder(folder_name):
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)
    os.mkdir(folder_path)

def create_file(file_name, content):
    file_path = os.path.join(settings.WORKING_DIRECTORY, file_name)
    with open(file_path, 'w') as file:
        file.write(content)

def list_files():
    files = os.listdir(settings.WORKING_DIRECTORY)
    return files

def delete_file(file_name):
    file_path = os.path.join(settings.WORKING_DIRECTORY, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f'File {file_name} not found.')

def delete_folder(folder_name):
    folder_path = os.path.join(settings.WORKING_DIRECTORY, folder_name)
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
    else:
        print(f'Folder {folder_name} not found.')
