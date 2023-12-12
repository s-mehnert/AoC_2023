# AoC 2023 --- Day 5 

# import puzzle input
imported_data = list()

with open("03_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n"))

# Part 1

# find symbols

def is_symbol(field):
    return not field.isdigit() and field != "."

def find_adjacent_symbol(map, i, j):
    if i > 0:
        if j > 0:
            if is_symbol(map[i-1][j-1]):
                return True
            if is_symbol(map[i][j-1]):
                return True
            if is_symbol(map[i-1][j]):
                return True
        if j < len(map[0])-1:
            if is_symbol(map[i-1][j+1]):
                return True
            if is_symbol(map[i][j+1]):
                return True
    if i < len(map)-1:
        if j < len(map[0])-1:
            if is_symbol(map[i+1][j+1]):
                return True
            if is_symbol(map[i][j+1]):
                return True
            if is_symbol(map[i+1][j]):
                return True
        if j > 0:
            if is_symbol(map[i+1][j-1]):
                return True
            if is_symbol(map[i][j-1]):
                return True
    return False

# extract numbers

def extract_numbers(map):
    num_list = list()
    num = ""
    symbol_found = False
    for i, line in enumerate(map):
        for j, field in enumerate(line):
            if field.isdigit():
                num += field
                if not symbol_found:
                    symbol_found = find_adjacent_symbol(map, i, j)
            else:
                if symbol_found:
                    num_list.append(num)
                    symbol_found = False
                num = ""
    return [int(num) for num in num_list if num]

print("The sum of all the part numbers in the engine schematic is:", sum(extract_numbers(imported_data)))
