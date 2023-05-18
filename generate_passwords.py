import itertools
import os

code_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
code_length = 8
chunk_size = 100000000  # Chunk size used during generation

def generate_combinations(start, end):
    combinations = []
    for combination in itertools.islice(itertools.product(code_chars, repeat=code_length), start, end):
        combinations.append("".join(combination))
    return combinations

def write_combinations(file_path, combinations):
    with open(file_path, "a") as file:
        for combination in combinations:
            file.write(combination + "\n")

if __name__ == "__main__":
    file_path = "passwords.txt"
    file_check = "C:/Users/wes4r/Desktop/projectPassword/passwords1.txt"
    # Check if the file exists
    if os.path.exists(file_check):
        print("Resuming from the last generated chunk...")
        with open(file_check, "r") as file:
            last_chunk = sum(1 for _ in file)  # Number of combinations generated so far
    else:
        last_chunk = 0

    remaining_combinations = len(code_chars) ** code_length - last_chunk
    num_chunks = (remaining_combinations - 1) // chunk_size + 1

    for i in range(num_chunks):
        start = last_chunk + i * chunk_size
        end = min(start + chunk_size, len(code_chars) ** code_length)
        print(f"Generating combinations for code length {code_length}, from {start} to {end}")
        combinations = generate_combinations(start, end)
        write_combinations(file_path, combinations)
