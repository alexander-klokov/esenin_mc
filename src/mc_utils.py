import os
import glob

kernel = 3

def load_data(directory_path):

    # Use a wildcard pattern to get a list of all files in the directory
    file_list = glob.glob(os.path.join(directory_path, '*'))

    data = ""

    # Iterate through the files and read them
    for file_path in file_list:
        # Check if the path is a file (not a subdirectory)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read().lower().strip().replace("\n", "")
                data = data + content

    return data