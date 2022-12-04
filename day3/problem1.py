# file_name = 'example.txt'
file_name = 'input.txt'

lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
total = 0

with open(file_name, 'r') as f:
    lines = f.read().splitlines()

    for line in lines:
        half = len(line) // 2
        first = line[:half]
        second = line[half:]
        
        common_character = list(set(first).intersection(second))[0]

        if common_character.isupper():
            total += upper_case.index(common_character) + 27
        else:
            total += lower_case.index(common_character) + 1
    
    print(f"Total priority: {total}")
