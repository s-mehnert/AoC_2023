# AoC 2023 --- Day 1 

# import puzzle input
imported_data = list()

with open("02_input.txt") as input:
    for line in input.readlines():
        imported_data.append(line.strip("\n").lstrip("Game ").split(": "))

# format data

games = dict()

for entry in imported_data:
    value = [subset.split(", ") for subset in entry[1].split("; ")]
    games[int(entry[0])] = value

# Part 1

max_num_color = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def cube_numbers_possible(subset):
    for cube_color in subset:
        number, color = cube_color.split()
        if int(number) > max_num_color[color]:
            return False
    return True

def evaluate_game(id, game):
    for subset in game:
        if not cube_numbers_possible(subset):
            return 0
    return id

sum_of_ids = 0

for id, game in games.items():
    sum_of_ids += evaluate_game(id, game)

print("The sum of all possible game IDs is", sum_of_ids)
