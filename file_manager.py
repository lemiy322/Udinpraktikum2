import os
from settings import WORKING_DIRECTORY

class FileManager:
    def __init__(self):
        self.current_directory = WORKING_DIRECTORY

    def list_directory(self):
        files_and_folders = os.listdir('.')
        return files_and_folders

    def make_folder(self, folder_name):
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(folder_path, exist_ok=True)

    def remove_folder(self, folder_name):
        folder_path = os.path.join(os.getcwd(), folder_name)
        os.rmdir(folder_path)

    def change_directory(self, folder_name):
        if folder_name == "..":
            self.current_directory = os.path.dirname(self.current_directory)
        else:
            new_directory = os.path.join(self.current_directory, folder_name)
            if os.path.isdir(new_directory):
                self.current_directory = new_directory
            else:
                print("Directory doesn't exist.")

    def create_file(self, file_name):
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "w") as file:
            pass

    def read_file(self, file_name):
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "r") as file:
            content = file.read()
        return content

    def write_file(self, file_name, content):
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "w") as file:
            file.write(content)

    def delete_file(self, file_name):
    file_path = os.path.join(self.current_directory, file_name)
    try:
        os.remove(file_path)
        print(f"File '{file_name}' has been successfully deleted.")
    except OSError as e:
        print(f"Error deleting file: {e}")

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.current_directory, old_name)
        new_path = os.path.join(self.current_directory, new_name)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    file_manager = FileManager()

