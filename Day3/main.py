# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZTfirst_half
# CrZsJsPPZsGzwwsLwLmpwMDw
#
# every line is a backpack,
# every line is divided in half, first half is the first compartment and the second half is the second compartment
#
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
#
# if there is a comman type (letter) in both sides then add its priority to the result int
# print the result
#
# assign the letters to their priority
import string

prio = {}

for i, letter in enumerate(string.ascii_lowercase):
    prio[letter] = i + 1

for i, letter in enumerate(string.ascii_uppercase):
    prio[letter] = i + 27
#
# for key, value in prio.items():
#     print(f"key: {key} value: {value}")

testing = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

with open('input.txt', 'r') as f:
    result = 0
    currentGroup = []
    index = 0

    # for line in testing.splitlines():
    #
    #     # is the index 0?
    #     if index == 0:
    #         currentGroup = []
    #
    #     # add the current line
    #     currentGroup.append(line)
    #
    #     # increase the index
    #     index += 1
    #
    #     # is the index 3?
    #     if index == 3:
    #         found = False
    #         print(f"current group is: {currentGroup}")
    #         # find the common_letters between the last three lines
    #         for letter in currentGroup[0]:
    #             if found: break
    #             if letter in currentGroup[1]:
    #                 if letter in currentGroup[2]:
    #                     print(f"found the letter common in three of them: {letter}")
    #                     # add them to the result
    #                     result += prio[letter]
    #                     found = True
    #
    #         index = 0
    #
    #
    # print(result)

        # # devide the line in half
        # half_length = len(line) // 2
        # first_half = line[:half_length]
        # second_half = line[half_length:]
    #
        # get the first three lines

        # find common letters
        # common_letters = set();
        #
        # for letter in first_half:
        #     if letter in second_half:
        #         common_letters.add(letter)
        #
        # for letter in common_letters:
        #     result += prio[letter]

        # 
        # get the priority value of the common letter and add it to the result
    for line in f:
        # is the index 0?
        if index == 0:
            currentGroup = []
            
        # add the current line
        currentGroup.append(line)

        # increase the index
        index += 1

        # is the index 3?
        if index == 3:
            found = False
            # find the common_letters between the last three lines
            for letter in currentGroup[0]:
                if found: break
                if letter in currentGroup[1]:
                    if letter in currentGroup[2]:
                        # add them to the result
                        result += prio[letter]
                        found = True

            index = 0

        
    print(result)

    # print the result
