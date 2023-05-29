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
# X -> Rock
# Y -> Paper
# Z -> Scissors
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
oRock = 'A'
oPapaer = 'B'
oScissors = 'C'

mRock = 'X'
mPaper = 'Y'
mScissors = 'Z'


def getWinner(opponent, mine):
    if mine == mRock:
        if opponent == oRock:
            return 3 + 1
        if opponent == oPapaer:
            return 0 + 1
        if opponent == oScissors:
            return 6 + 1

    elif mine == mPaper:
        if opponent == oRock:
            return 6 + 2
        if opponent == oPapaer:
            return 3 + 2
        if opponent == oScissors:
            return 0 + 2

    elif mine == mScissors:
        if opponent == oRock:
            return 0 + 3
        if opponent == oPapaer:
            return 6 + 3
        if opponent == oScissors:
            return 3 + 3
    return 0

with open('input.txt') as f:

    result = 0
    testing = '''A Y
    B X
    C Z'''

    for line in f:
        opponent_choice = line[0]
        my_choice = line[2]
        result += getWinner(opponent_choice, my_choice)

    print(result)


