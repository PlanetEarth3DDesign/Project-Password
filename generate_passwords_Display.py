import itertools
import multiprocessing
import time
import os.path


def generate_combinations(args):
    chars, length, start, end = args
    combinations = []
    for combination in itertools.islice(itertools.product(chars, repeat=length), start, end):
        combinations.append("".join(combination))
    return combinations


def generate_passwords(chars, lengths, num_processes, chunk_size):
    for length in lengths:
        file_name = f"passwords_{length}.txt"
        if os.path.exists(file_name):
            with open(file_name) as f:
                num_lines = sum(1 for _ in f)
            print(f"{file_name} already exists with {num_lines} lines, skipping...")
            continue

        with multiprocessing.Pool(processes=num_processes) as pool, open(file_name, "w") as file:
            total_combinations = len(chars) ** length
            chunks = range(0, total_combinations, chunk_size)
            num_chunks = len(chunks) - 1
            elapsed_time = 0.0  # default value

            print(f"Generating {total_combinations} combinations for code length {length}...")
            start_time = time.time()
            for i, start in enumerate(chunks[:-1]):
                end = chunks[i+1]
                result = pool.apply_async(generate_combinations, [(chars, length, start, end)])
                for combination in result.get():
                    file.write(combination + "\n")
                elapsed_time = time.time() - start_time
                percent_complete = int((end / total_combinations) * 100)
                time_remaining = round((elapsed_time / (end - chunks[0])) * (total_combinations - end))
                print(f"Progress: {percent_complete}% ({i+1}/{num_chunks} chunks), "
                      f"Elapsed time: {elapsed_time:.2f}s, Time remaining: {time_remaining}s", end="\r")

            if elapsed_time > 0.0:
                print(f"Progress: 100% ({num_chunks}/{num_chunks} chunks), Elapsed time: {elapsed_time:.2f}s")
                print(f"Generated {total_combinations} combinations for code length {length}")
            else:
                print(f"No combinations generated for code length {length}")




if __name__ == "__main__":
    chars = "1234567890abcdefghijklmnopqrstuvwxyz+-_"
    lengths = [8]
    num_processes = 1
    chunk_size = 10000000

    generate_passwords(chars, lengths, num_processes, chunk_size)
