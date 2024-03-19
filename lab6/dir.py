import os
#rask1
def list_directories_and_files(path):
    print("Directories:")
    for dir_entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_entry)):
            print(dir_entry)

    print("\nFiles:")
    for file_entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_entry)):
            print(file_entry)

def list_all_directories_and_files(path):
    for root, dirs, files in os.walk(path):
        print("Directory:", root)
        print("Subdirectories:")
        for dir_name in dirs:
            print(os.path.join(root, dir_name))
        print("Files:")
        for file_name in files:
            print(os.path.join(root, file_name))
        print()


path = input("Enter the path: ")

print("\nListing only directories and files:")
list_directories_and_files(path)

print("\nListing all directories and files:")
list_all_directories_and_files(path)

#task2
import os

def check_access(path):
    print(f"Existence: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

# Example usage:
path = input("Enter the path: ")
check_access(path)

#task3
import os

def analyze_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")
path = input("Enter the path: ")
analyze_path(path)

#task4
import os

def analyze_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")


path = input("Enter the path: ")
analyze_path(path)

#task5
def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')


filename = input("Enter the filename: ")
lst = [1, 2, 3, 4, 5]
write_list_to_file(filename, lst)

#task6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            pass

generate_files()

#task7
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            pass

generate_files()

#task8
import os

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File '{path}' deleted successfully.")
    else:
        print("File not found.")


path = input("Enter the path of the file to delete: ")
delete_file(path)

