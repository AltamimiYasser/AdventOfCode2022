# A Y
# B X
# C Z
#
# Opponent:You
#
# Opponent
# A -> Rock
# B -> Paper
# C -> Scissors 
#
# You
# X -> you need to lose
# Y -> you need to draw
# Z -> you need to win
#
# Total score = sum of scores in each round
#
# shape scores:
# 1: Rock
# 2: Paper
# 3: Scissors
# +
# 0 if round lose
# 3 if round draw
# 6 if round won

# TODO: get total score of input
rock = 'A'
paper = 'B'
scissors = 'C'

lose = 'X'
draw = 'Y'
win = 'Z'


def get_round_points(opponent, mine):
    if mine == rock:
        if opponent == rock:
            return 3 + 1
        if opponent == paper:
            return 0 + 1
        if opponent == scissors:
            return 6 + 1

    elif mine == paper:
        if opponent == rock:
            return 6 + 2
        if opponent == paper:
            return 3 + 2
        if opponent == scissors:
            return 0 + 2

    elif mine == scissors:
        if opponent == rock:
            return 0 + 3
        if opponent == paper:
            return 6 + 3
        if opponent == scissors:
            return 3 + 3
    return 0


def get_my_choice(opponent, action):
    if opponent == rock:
        if action == lose:
            return scissors
        if action == draw:
            return rock
        if action == win:
            return paper
    pass

    if opponent == paper:
        if action == lose:
            return rock
        if action == draw:
            return paper
        if action == win:
            return scissors
    pass

    if opponent == scissors:
        if action == lose:
            return paper
        if action == draw:
            return scissors
        if action == win:
            return rock
    pass

with open('input.txt') as f:

    result = 0
    testing = '''A Y
B X
C Z'''

    # for line in testing.splitlines():
    #     print(f"line: {line}")
    #     opponent_choice = line[0]
    #     print(f'opponent_choice {opponent_choice}')
    #     my_needed_action = line[2]
    #     print(f'action needed {my_needed_action}')
    #     my_choice = get_my_choice(opponent_choice, my_needed_action)
    #     print(f'my choice {my_choice}')
    #     result += getRoundPoints(opponent_choice, my_choice)
    #     print(f'result {result}')

    for line in f:
        opponent_choice = line[0]
        my_needed_action = line[2]
        my_choice = get_my_choice(opponent_choice, my_needed_action)
        result += get_round_points(opponent_choice, my_choice)

    print(result)


