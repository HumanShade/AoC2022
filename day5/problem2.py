# file_name = 'example.txt'
file_name = 'input.txt'

def main():
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        stacks = ''
        for idx, line in enumerate(lines):
            if line[:4] == "move":
                if stacks == '':
                    stacks = define_problem(lines[:idx-1])
                
                line = line.split(' ')
                amount = int(line[1])
                src = int(line[3])
                dst = int(line[5])
                
                stacks[dst] += stacks[src][-amount:]
                stacks[src] = stacks[src][:-amount]

        solution = ''.join([stacks[key][-1] for key in stacks.keys()])
        print(solution)


def define_problem(strings: list):

    nr_stacks = range(1, len(set(strings[-1])))
    stack_positions = [1+4*(val-1) for val in nr_stacks]
    stacks = {stack_nr: '' for stack_nr in nr_stacks}
    for string in reversed(strings[:-1]):
        items = [string[idx] for idx in stack_positions]
        for stack, item in zip(stacks.keys(), items):
            stacks[stack] += item
    
    for key in stacks.keys():
        stacks[key] = stacks[key].replace(' ', '')

    return stacks


if __name__ == "__main__":
    main()