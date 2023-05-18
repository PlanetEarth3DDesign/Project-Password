import os

# set the directory path
directory_path = 'C:/Users/User/Downloads/Passwords/'

# loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):  # check if the file is a text file
        filepath = os.path.join(directory_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(filepath, 'w', encoding='ascii', errors='ignore') as f:
            f.write(content)
