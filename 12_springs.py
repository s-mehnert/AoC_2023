# AoC 2023 --- Day 12 

# import puzzle input
imported_data = list()

with open("12_input.txt") as input:
    for line in input.readlines():
        springs, report = line.split()
        report = report.split(",")
        imported_data.append((springs, report))

for line in imported_data:
    print(line)

# Part 1