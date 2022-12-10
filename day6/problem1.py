# file_name = 'example1.txt'
# file_name = 'example2.txt'
# file_name = 'example3.txt'
# file_name = 'example4.txt'
# file_name = 'example5.txt'
# file_name = 'example2.txt'
file_name = 'input.txt'

def main():
    with open(file_name, 'r') as f:
        line = f.read()
        for idx in range(len(line)):
            if len(set(line[idx:idx+4])) == 4:
                print(f"Marker after: {idx+4}")
                break

if __name__ == "__main__":
    main()