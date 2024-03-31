import os

WORKING_DIRECTORY = "C:/Users/persi/git/poject2/.git/"

def list_files_and_folders():
    file_list = []
    folder_list = []

    os.chdir(WORKING_DIRECTORY)

    for item in os.listdir():
        if os.path.isfile(item):
            file_list.append(item)
        elif os.path.isdir(item):
            folder_list.append(item)

    print("Files:")
    for file in file_list:
        print(file)

    print("\nFolders:")
    for folder in folder_list:
        print(folder)

list_files_and_folders()
