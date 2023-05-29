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
    # for line in testing.splitlines():
    #     # devide the line in half
    #     half_length = len(line) // 2
    #     first_half = line[:half_length]
    #     second_half = line[half_length:]
    #
    #     # find common letters 
    #     common_letters = set();
    #
    #     for letter in first_half:
    #         if letter in second_half:
    #             common_letters.add(letter)
    #
    #     for letter in common_letters:
    #         result += prio[letter]
    #
    # print(result)
        # 
        # get the priority value of the common letter and add it to the result
    for line in f:
        half_length = len(line) // 2
        first_half = line[:half_length]
        second_half = line[half_length:]

        # find common letters 
        common_letters = set();

        for letter in first_half:
            if letter in second_half:
                common_letters.add(letter)

        for letter in common_letters:
            result += prio[letter]

    print(result)

    # print the result
