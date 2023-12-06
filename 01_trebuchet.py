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

written_digits = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, 
    "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
}

# find written digits:
def find_digits(line):
    digits_found = dict()
    for digit in written_digits:
        if digit in line:
            start = 0
            while digit in line[start:]:
                digit_index = line.find(digit, start)
                digits_found[digit_index] = digit
                start = digit_index + 1               
    return digits_found

# find first written digit
def find_first_digit(digit_dict):
    return digit_dict[min(digit_dict.keys())]

# find last written digit
def find_last_digit(digit_dict):
    return digit_dict[max(digit_dict.keys())]  

# create calibration value out of first and last digit taking written digits into account
def create_calibration_value(digit_dict):
    return int(str(written_digits[find_first_digit(digit_dict)]) + str(written_digits[find_last_digit(digit_dict)]))

# sum calibration values
total = 0

for line in imported_data:
    sum = create_calibration_value(find_digits(line))
    total += sum

# print result
print("The sum of all calibration values in the document including written digits is:", total)