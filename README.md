# Project-Password
This script generates all possible combinations of a given character set and length, and saves them to a text file.
The script supports resuming from the last generated chunk in case of interruption or to continue generating combinations.

## Prerequisites

- Python 3.x
- Required Python packages (automatically installed via pip):
  - `itertools`
  - `multiprocessing`

## Usage

1. Clone the repository or download the script file (`generate_passwords.py`) to your local machine.

2. Open the script file (`generate_passwords.py`) in a text editor.

3. Modify the following variables in the script according to your requirements:

   - `code_chars`: The character set to be used for generating passwords. You can modify it to include/exclude characters as needed.
   - `code_length`: The desired length of the generated passwords.
   - `chunk_size`: The number of combinations to be generated per chunk. You can adjust this value based on your system's memory and performance.

4. Save the script file after making the necessary modifications.

5. Open a terminal or command prompt and navigate to the directory where the script file is located.

6. Run the script using the following command: "Python3 generate_passwords.py"

The script will start generating combinations and save them to a file named `passwords.txt`.

7. The script will display progress information, including the current chunk being processed. If the script is interrupted, you can re-run it, and it will resume from the last generated chunk automatically.

## Notes

Work in progress - The script utilizes multiprocessing to distribute the computation across multiple CPU cores, making the process faster. The number of processes used is equal to the number of CPU cores available on your system. You can adjust the `num_processes` variable in the script to specify a different number of processes if needed.

- The script generates combinations in chunks to avoid loading the entire combination space into memory at once. The `chunk_size` variable controls the number of combinations generated per chunk. Adjust it according to your system's memory capacity.

- The script appends the generated combinations to the output file (`passwords.txt`). If you want to start fresh and overwrite the existing file, make sure to delete or rename the file before running the script.

- It is recommended to run the script on a machine with sufficient resources (RAM, disk space) to handle the potentially large output file and the computation.

- Remember to use this script responsibly and only for legal and ethical purposes. Generating and using large sets of passwords without proper authorization may be against the law or violate terms of service.

## License

This script is provided under the [MIT License](LICENSE).

