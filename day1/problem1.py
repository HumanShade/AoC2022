file_name = 'example.txt'
file_name = 'input.txt'
top_calories = 0
total = 0

with open(file_name, 'r') as f:
    lines = f.readlines()
    last_idx = len(lines) - 1
    for idx, line in enumerate(lines):
        try:
            total += int(line.strip())
        except:
            pass

        if line == '\n' or idx == last_idx:
            if total > top_calories:
                top_calories = total
            total = 0

print(f"Max calories: {top_calories}")
            
