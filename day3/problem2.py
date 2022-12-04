# file_name = 'example.txt'
file_name = 'input.txt'

lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
total = 0

with open(file_name, 'r') as f:
    lines = f.read().splitlines()
    
    group = []
    for idx, line in enumerate(lines):
        group.append(line)

        if len(group) == 3:
            common_character = list(set(group[0]) & set(group[1]) & set(group[2]))[0]

            if common_character.isupper():
                total += upper_case.index(common_character) + 27
            else:
                total += lower_case.index(common_character) + 1
        
            group = []
            
    
    print(f"Total priority: {total}")
