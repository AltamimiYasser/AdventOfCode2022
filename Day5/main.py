


with open('input.txt', 'r') as f:
    lines = f.readlines()


def getVerticalArray(lines):
    cells = []
    for line in lines:
        current_cell = ''
        current_index = 0

        current_cells = []
        for letter in line:
            if current_index != 3:
                current_cell += letter
                current_index += 1
            else:
                current_cells.append(current_cell)
                current_cell = ''
                current_index = 0
        current_cells.append(current_cell)
        cells.append(current_cells)

    vertical_arr = [[row[i] for row in cells] for i in range(len(cells[0]))]
    return(vertical_arr)


# separate the first part and the second part by the blank line
first_part = ''
second_part = ''

in_first_part = True
for line in lines:
    if in_first_part:
        if not line.strip(): # empty line
            in_first_part = False
            continue
        first_part += line
    else:
        second_part += line


first_part = first_part.splitlines()[:-1]
first_part = getVerticalArray(first_part)
first_part = [[s for s in inner_arr if s.strip() != ''] for inner_arr in first_part]

second_part = second_part.splitlines()
second_part_splitted = []

# parse second_part into a 2 dimensional array
for item in second_part:
    second_part_splitted.append(item.split(' '))

for item in second_part_splitted:
    quantity = int(item[1])
    origin = int(item[3]) - 1
    dest = int(item[5]) - 1
    
    to_be_left = first_part[origin][:quantity] # this is working

    # remove the lifted items from its origin
    first_part[origin] = first_part[origin][quantity:] 

    first_part[dest] = to_be_left + first_part[dest]

resutl = ''
for item in first_part:
    resutl += item[0][1]

print(resutl)



# ['move', '1', 'from', '2', 'to', '1']
# ['move', '3', 'from', '1', 'to', '3']
# ['move', '2', 'from', '2', 'to', '1']
# ['move', '1', 'from', '1', 'to', '2']


#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
