# AoC 2023 --- Day 10 

# import puzzle input
imported_data = list()

with open("10_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n")) # or use list(line.strip("\n"))

for line in imported_data:
    print(line)

