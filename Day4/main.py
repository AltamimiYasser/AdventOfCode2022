#
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
#

testing = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

with open('input.txt', 'r') as f:
    result = 0

    # for each line compare each side
    for line in f:
        splittedPair = line.split(',')

        first = splittedPair[0].split('-')
        second = splittedPair[1].split('-')
        first_min = int(first[0])
        first_max = int(first[1])
        second_min = int(second[0])
        second_max = int(second[1])


        if first_min <= second_max and second_min <= first_max:
            result += 1


    print(result)


# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8
