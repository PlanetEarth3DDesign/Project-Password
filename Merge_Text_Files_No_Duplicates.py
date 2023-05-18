import os

# set the directory path where the password files are located
directory_path = 'C:/Users/User/Desktop/projectPassword/passwords/'

# create an empty set to store the unique passwords
unique_passwords = set()

# loop through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):  # check if the file is a text file
        filepath = os.path.join(directory_path, filename)
        try:
            with open(filepath, 'r', encoding='ascii') as f:
                # read each line in the file and add the passwords to the set
                for line in f:
                    password = line.strip()
                    if password:  # ignore empty lines
                        unique_passwords.add(password)
        except UnicodeDecodeError:
            print(f"Error reading file {filename}: UnicodeDecodeError")

# write the unique passwords to a new output file
output_path = 'C:/Users/wes4r/Desktop/projectPassword/password/WebList.txt'
with open(output_path, 'w') as f:
    for password in unique_passwords:
        f.write(password + '\n')

# print completion message
print(f'Finished processing {len(unique_passwords)} unique passwords from {len(os.listdir(directory_path))} files. Unique passwords saved to {output_path}.')
