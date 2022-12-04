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

lose_condition = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
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

        match my_input:
            case 'X':   # lose
                shape = lose_condition[opponent]
                points += shape_score[shape]

            case 'Y':   # draw
                shape = draw_condition[opponent] 
                points += shape_score[shape] + 3

            case 'Z':   # win
                shape = win_condition[opponent] 
                points += shape_score[shape] + 6
            
print(f"Tournament score: {points}")