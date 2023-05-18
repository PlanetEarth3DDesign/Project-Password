import os

input_dir = 'C:/Users/User/Desktop/projectPassword/Passwords/'
output_file = 'C:/Users/User/Desktop/projectPassword/Passwords/NewPassword.txt'

# Get a list of all text files in the input directory
input_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".txt")]

# Open the output file in append mode
with open(output_file, "a") as output:
    # Loop through each input file
    for input_file in input_files:
        # Open the input file in read mode
        with open(input_file, "r") as input:
            # Read the contents of the input file and write them to the output file
            output.write(input.read())
