# file_name = 'example.txt'
file_name = 'input.txt'

"""
A, X = Rock
B, Y = Paper
C, Z = Scissors
"""

win_condition = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

draw_condition = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

shape_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

points = 0

with open(file_name, 'r') as f:
    lines = f.read().splitlines() 
    for line in lines:
        opponent = line[0]
        my_input = line[2]
    
        # Input score
        points += shape_score[my_input]

        # Win
        if my_input == win_condition[opponent]:
            points += 6
            continue
            
        # draw
        if my_input == draw_condition[opponent]:
            points += 3
            continue
    
print(f"Tournament score: {points}")