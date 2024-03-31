import settings
import functions

functions.create_folder('my_folder')

functions.create_file('my_file.txt', 'Hello, world!')

files = functions.list_files()
print(files)

functions.delete_file('my_file.txt')

functions.delete_folder('my_folder')

