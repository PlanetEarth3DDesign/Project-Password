import os
import chardet

directory_path = 'C:/Users/wes4r/Downloads/Passwords/'

for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read(1000))
        print(f"{filename}: {result['encoding']}")