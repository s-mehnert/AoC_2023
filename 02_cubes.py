# AoC 2023 --- Day 1 

# import puzzle input
imported_data = list()

with open("02_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n").strip("Game ").split(": "))

print(imported_data)

# format data

games = dict()

for entry in imported_data:
    games[int(entry[0])] = entry[1].split("; ")

for key, value in games.items():
    print(key, "-->", value)

# Part 1