file = ''
results = []

with open('input.txt', 'r') as f:
    result = 0
    for line in f:
        if not line.strip(): ## white space
            results.append(result)
            result = 0
        else:
            result += int(line)

top_three = 0
for i in range(3):
    top_three += results.pop(results.index(max(results)))

print(top_three)

## 1. if line is not empty:
    ## 1. add line to current result
## if line is empty, add result to the results array and set result to 0
## get the largest number in the array

