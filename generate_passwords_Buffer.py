import io
import itertools
import multiprocessing

code_chars = "0123456789abcdefghijklmnopqrstuvwxyz+-_"
code_length = 8

def generate_combinations(args):
    chars, length, start, end = args
    combinations = []
    for combination in itertools.islice(itertools.product(chars, repeat=length), start, end):
        combinations.append("".join(combination))
    return combinations

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()
    chunk_size = 500000000  // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        buffer = io.StringIO() # create a string buffer
        for start in range(0, len(code_chars)**code_length - 1, chunk_size):
            end = min(start + chunk_size, len(code_chars)**code_length)
            print(f"Generating combinations for code length {code_length}, from {start} to {end}")
            result = pool.apply_async(generate_combinations, [(code_chars, code_length, start, end)])
            for combination in result.get():
                buffer.write(combination + "\n") # write to the buffer instead of directly to the file
        with open("passwords.txt", "w") as file:
            file.write(buffer.getvalue()) # dump the contents of the buffer to the file all at once
