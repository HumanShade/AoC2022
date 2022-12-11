# file_name = 'example.txt'
# file_name = 'example2.txt'
file_name = 'input.txt'
import uuid
from datetime import datetime

def main():
    with open(file_name, 'r') as f:
            lines = f.read().splitlines()
            directory = {}
            path = []
            
            # Scan directory
            for line in lines:
                if line[0].isnumeric(): # File
                    split = line.split(' ')
                    directory = add_file(directory, split, path)

                elif line[0] == '$' and line[2:4] == 'cd':    # cd command
                    key = line[5:]
                    if key == '..':
                        key = path[:-1]
                        path.pop()
                    else:
                        path.append(key)

            # Calculate the smallest directory that frees enough space
            used_memory, directories = calculate_size(directory)
            max_memory = 70000000
            required_memory = 30000000
            available_memory = max_memory - used_memory
            missing_memory = required_memory - available_memory
            possible_directories = []
            for key in directories:
                if directories[key] >= missing_memory:
                    possible_directories.append(directories[key])
        
            possible_directories.sort()
            print(possible_directories[0])


def add_file(directory, split, path: list):
    # Create directory as dictionary using recursion
    if len(path) >= 1:
        if path[0] not in directory.keys():
            directory[path[0]] = {}
        directory[path[0]] = add_file(directory[path[0]], split, path[1:])

    if len(path) == 1:  # if at the end of the path, add the file
        if path[0] in directory.keys():
            directory[path[0]][split[1]] = int(split[0])
        else:
            directory[path[0]] = {
                split[1]: int(split[0])
            }
            
    return directory


def calculate_size(directory):
    # Calculate directory size using recursion
    sum = 0
    directories = {}
    for key, value in directory.items():
        if isinstance(value, dict):
            result, new_dirs = calculate_size(value)
            # manage duplicate keys being overwritten
            if bool(directories) and bool(new_dirs) and any([key in new_dirs.keys() for key in directories.keys()]) :
                # Change key to a unique id if found in another directory  
                new_dirs = {str(uuid.uuid4()) + str(datetime.now()) if k in directories.keys() else k:v for k, v in new_dirs.items()}
            directories = directories | new_dirs
            sum += result
            directories[key] = result
            
        elif isinstance(value, int):
            sum += value
        
    return sum, directories


if __name__ == "__main__":
    main()
