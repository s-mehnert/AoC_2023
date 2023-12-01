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


