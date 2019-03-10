import re
fh = open('regex_sum_147417.txt')
numbers = []
sum = 0

for line in fh:
    number = re.findall('[0-9]+', line)
    if len(number) >= 1:
        numbers.append(number)

# Flatten list of lists into one list so that list items can be converted to int easily
numbers = [i for lst in numbers for i in lst]

for number in numbers:
    sum = sum + int(number)

print(sum)