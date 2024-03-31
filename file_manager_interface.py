import functions
import os


def main():
    current_directory = os.path.abspath(settings.WORKING_DIRECTORY)  
    print(f'Welcome to File Manager. Current directory: {current_directory}')

    while True:
        command = input("Enter a command: ")

        if command == 'create_folder':
            folder_name = input("Enter folder name to create: ")
            functions.create_folder(folder_name)
            print(f'Folder {folder_name} created.')

        elif command == 'delete_folder':
            folder_name = input("Enter folder name to delete: ")
            functions.delete_folder(folder_name)
            print(f'Folder {folder_name} deleted.')

        elif command == 'list_files':
            files = functions.list_files()
            print("Files in current directory:")
            for file in files:
                print(file)

        else:
            print("Unknown command. Please try again.")

if __name__ == '__main__':
    main()
