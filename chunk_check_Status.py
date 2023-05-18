code_chars = "0123456789abcdefghijklmnopqrstuvwxyz+-_"
code_length = 8
start = 40000000000
end = 40031250000

total_combinations = len(code_chars) ** code_length
completed_combinations = start - 1
remaining_combinations = total_combinations - end

percent_complete = (completed_combinations / total_combinations) * 100
percent_remaining = (remaining_combinations / total_combinations) * 100

print(f"Progress: {percent_complete:.2f}%")
print(f"Remaining: {percent_remaining:.2f}%")
