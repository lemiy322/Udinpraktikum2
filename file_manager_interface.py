import os
from file_manager import FileManager

def main():
    file_manager = FileManager()

    while True:
        print("\nCurrent Directory:", os.getcwd)
        print("1. List directory contents")
        print("2. Change directory")
        print("3. Make folder")
        print("4. Remove folder")
        print("5. Create file")
        print("6. Read file")
        print("7. Write file")
        print("8. Delete file")
        print("9. Rename file")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contents = file_manager.list_directory()
            print("\nDirectory contents:")
            for item in contents:
                print(item)

        elif choice == "2":
            folder_name = input("Enter folder name or '..' to go up a level: ")
            file_manager.change_directory(folder_name)

        elif choice == "3":
            folder_name = input("Enter folder name to create: ")
            file_manager.make_folder(folder_name)

        elif choice == "4":
            folder_name = input("Enter folder name to remove: ")
            file_manager.remove_folder(folder_name)

        elif choice == "5":
            file_name = input("Enter file name to create: ")
            file_manager.create_file(file_name)

        elif choice == "6":
            file_name = input("Enter file name to read: ")
            content = file_manager.read_file(file_name)
            print("\nFile content:")
            print(content)

        elif choice == "7":
            file_name = input("Enter file name to write to: ")
            content = input("Enter content to write: ")
            file_manager.write_file(file_name, content)

        elif choice == "8":
            file_name = input("Enter file name to delete: ")
            file_manager.delete_file(file_name)

        elif choice == "9":
            old_name = input("Enter file name to rename: ")
            new_name = input("Enter new name: ")
            file_manager.rename_file(old_name, new_name)

        elif choice == "10":
            print("Exiting file manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


