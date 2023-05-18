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

## File Encoding Detection

This script detects the encoding of text files in a specified directory using the chardet library.

    File_Encoding_Check.py - Detects the encoding of text files.

Usage:

    Ensure that you have the chardet library installed (pip install chardet).
    Modify the directory_path variable to specify the directory containing the text files.
    Run the script.

The script will iterate over the files in the directory and print the detected encoding for each file.

2. File Encoding Conversion

This script converts the encoding of text files in a specified directory from UTF-8 to ASCII.

    File_Encoder.py - Converts text file encoding.

Usage:

    Modify the directory_path variable to specify the directory containing the text files.
    Run the script.

The script will iterate over the files in the directory, read the content of each file as UTF-8, and overwrite the file with the content encoded in ASCII.

3. Merge Text Files

This script merges multiple text files into a single output file.

    merge_text_files.py - Merges text files into a single output file.

Usage:

    Modify the input_dir and output_file variables to specify the input directory and output file paths, respectively.
    Run the script.

The script will collect all the text files in the input directory and concatenate their contents into the output file.

4. Unique Password Extraction

This script extracts unique passwords from multiple text files and saves them to a new file With No duplicates .

    Merge_Text_Files_No_Duplicates.py - Extracts unique passwords from text files.

Usage:

    Modify the directory_path and output_path variables to specify the input directory and output file paths, respectively.
    Run the script.

The script will iterate over the files in the directory, read each line in the files, and extract unique passwords, ignoring empty lines. The unique passwords will be saved to the specified output file.

After running the script, it will display the number of unique passwords extracted and the path to the output file.

Feel free to customize the script variables and paths according to your specific requirements.

Certainly! Here's an example of a more detailed disclaimer:
Disclaimer

Important: This software is intended for educational and development purposes only.

The scripts provided in this repository are intended to demonstrate various programming concepts and techniques. They are not intended for any illegal or unethical use. It is the user's responsibility to ensure that they comply with all applicable laws and regulations when using these scripts.

Usage of these scripts for any unauthorized activities is strictly prohibited.

The scripts may involve accessing, modifying, or processing files and data. It is essential to ensure that you have the necessary permissions and legal rights to perform such actions on the files and data you work with. The authors and contributors of these scripts are not responsible for any misuse or illegal activities conducted by users.

By using these scripts, you agree that:

    You will use them solely for educational, learning, and development purposes.
    You will comply with all applicable laws and regulations.
    You will respect the rights and privacy of others.
    You will not engage in any unauthorized, illegal, or unethical activities.

The authors and contributors of these scripts do not make any warranties or guarantees regarding the accuracy, reliability, or suitability of the scripts for any particular purpose. They shall not be held liable for any damages or consequences arising from the use or misuse of these scripts.

Please use these scripts responsibly and ethically.

# Sizes
10 Letter 2 key =
10 Letter 3 key =
10 Letter 4 key =
10 Letter 5 key =
10 Letter 6 key =
10 Letter 7 key =
10 Letter 8 key =
10 Letter 9 Key =
10 Letter 10 key =

36 Letter 2 Key =
36 Letter 3 key =
36 Letter 4 Key =
36 Letter 5 key =
36 Letter 6 key =
36 Letter 7 key = 500G
36 Letter 8 key = ill let you know if it ever complets LOL
36 Letter 9 Key = Pass on to your grand kids 
36 Letter 10 key = Really?
36 Letter 11 key = You are Joking?
36 Letter 12 key = its impossible why would you even thank you could? Do you know what a petabyte is try like 30-Petabytes+

## License

This script is provided under the [MIT License](LICENSE).

