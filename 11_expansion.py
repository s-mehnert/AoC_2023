# AoC 2023 --- Day 11 

# import puzzle input
imported_data = list()

with open("11_input.txt") as input:
    for line in input.readlines():
        imported_data.append(list(line.strip("\n")))

# calculate expansion

def expand(nested_list):
    expanded_list = list()
    for row in nested_list:
        expanded_list.append(row)
        if "#" not in row:
            expanded_list.append(row)
    return expanded_list
    
def transpose(nested_lst):
    return [[row[i] for row in nested_lst] for i in range(len(nested_lst[0]))]

expanded_universe = transpose(expand(transpose(expand(imported_data))))

# define location of galaxies within universe 

galaxies = dict()
galaxy_counter = 1
for i in range(len(expanded_universe)):
    for j in range(len(expanded_universe[0])):
        if expanded_universe[i][j] == "#":
            expanded_universe[i][j] = str(galaxy_counter) # or use int?
            galaxies[str(galaxy_counter)] = (i, j)
            galaxy_counter += 1

for row in expanded_universe:
    print(row)

for galaxy, pos in galaxies.items():
    print(galaxy, "--> position:", pos)

# find all galaxy pairs

combinations = list(galaxies)
galaxy_pairs = list()
for i in range(len(combinations)):
    for j in range(i+1, len(combinations)):
        galaxy_pairs.append((combinations[i], combinations[j]))
print(combinations)
for pair in galaxy_pairs:
    print(pair)
print(len(galaxy_pairs))

# find shortest path between two galaxies

print(galaxies["9"][0])
def find_shortest_path(gal1, gal2): # doesn't work --> find out why
    distance1 = galaxies[gal1][0] - galaxies[gal2[0]]
    print(distance1)
    distance2 = galaxies[gal2][1] - galaxies[gal2][2]
    return abs(distance1 + distance2)

print(find_shortest_path("5", "9"))