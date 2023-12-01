# AoC 2023 --- Day 1 --- Part 1

# import puzzle input
imported_data = list()

with open("01_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

# check if character is a number
def is_number(char):
    try: 
        num = int(char)
    except:
        return False
    return True

# extract numbers
def find_nums(line):
    num_list = list()
    for char in line:
        if is_number(char):
            num_list.append(char)
    return num_list

# turn numbers into calibration values
def create_calibration_value(num_list):
    return int(num_list[0] + num_list[-1])

# sum calibration values
sum = 0

for line in imported_data:
    sum += (create_calibration_value(find_nums(line)))

# print result
print("The sum of all calibration values in the document is:", sum)


# Day 1 --- Part 2

written_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# find written digits:
def find_digits(line):
    digits_found = dict()
    for digit in written_digits:
        if digit in line:
            digits_found[line.find(digit)] = digit
    return digits_found

digit_dict = find_digits(line)

# find first written digit
def find_first_digit(digit_dict):
    return digit_dict[min(digit_dict.keys())]

# find last written digit
def find_last_digit(digit_dict):
    return digit_dict[max(digit_dict.keys())]

# adjust find_nums function to return indices as well
def find_nums_and_indices(line):
    num_list = list()
    for i, char in enumerate(line):
        if is_number(char):
            num_list.append((char, i))
    if not num_list:
        first_num = find_digits(line)
        last_num = find_digits(line)
    else:
        first_num, first_index = num_list[0]
        last_num, last_index = num_list[-1]
        if find_digits(line[:first_index]):
            first_num = find_digits(line[:first_index])
        if find_digits(line[last_index:]):
            last_num = find_digits(line[last_index:])
    return (first_num, last_num)    

# adjust create_calibration_value function to take written digits into account
def create_calibration_value_with_written_digits(num_list):
    first_num, last_num = num_list
    if isinstance(first_num, dict):
        first_num = written_digits[find_first_digit(first_num)]
    if isinstance(last_num, dict):
        last_num = written_digits[find_last_digit(last_num)]
    return int(str(first_num) + str(last_num))

# sum calibration values
total = 0

for line in imported_data:
    sum = create_calibration_value_with_written_digits(find_nums_and_indices(line))
    print(sum)
    total += sum

# print result
print("The sum of all calibration values in the document is:", total)