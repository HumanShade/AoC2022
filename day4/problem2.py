# file_name = 'example.txt'
file_name = 'input.txt'

with open(file_name, 'r') as f:
    lines = f.read().splitlines()
    sum = 0
    for line in lines:
        elves = [value.split(sep='-') for value in line.split(sep=',')]
        elf1, elf2 = [set(range(int(value[0]), int(value[1])+1)) for value in elves]
        if elf1 & elf2:
            sum+=1

    print(f"Total sum {sum}")
