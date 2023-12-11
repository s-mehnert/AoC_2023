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

# define location of galaxies within expanded universe 

galaxies = dict()
galaxy_counter = 1
for i in range(len(expanded_universe)):
    for j in range(len(expanded_universe[0])):
        if expanded_universe[i][j] == "#":
            expanded_universe[i][j] = str(galaxy_counter) # or use int?
            galaxies[str(galaxy_counter)] = (i, j)
            galaxy_counter += 1

# find all galaxy pairs

combinations = list(galaxies)
galaxy_pairs = list()
for i in range(len(combinations)):
    for j in range(i+1, len(combinations)):
        galaxy_pairs.append((combinations[i], combinations[j]))

# find shortest path between two galaxies

def find_shortest_path(gal1, gal2): # doesn't work --> find out why
    distance1 = abs(galaxies[gal1][0] - galaxies[gal2][0])
    distance2 = abs(galaxies[gal1][1] - galaxies[gal2][1])
    return distance1 + distance2

# calculate sum of shortest paths between all galaxy pairs

total = 0

for pair in galaxy_pairs:
    total += find_shortest_path(*pair)

print(f"The sum of the shortest paths between all galaxy pairs is {total} steps.")

# Part 2

# define location of galaxies within original universe 

galaxies_o = dict()
galaxy_counter_o = 1
for i in range(len(imported_data)):
    for j in range(len(imported_data[0])):
        if imported_data[i][j] == "#":
            imported_data[i][j] = str(galaxy_counter_o)
            galaxies_o[str(galaxy_counter_o)] = (i, j)
            galaxy_counter_o += 1

# find all galaxy pairs

combinations_o = list(galaxies_o)
galaxy_pairs_o = list()
for i in range(len(combinations_o)):
    for j in range(i+1, len(combinations_o)):
        galaxy_pairs_o.append((combinations_o[i], combinations_o[j]))

# find shortest path between two galaxies

def find_shortest_path(gal1, gal2): # doesn't work --> find out why
    distance1 = abs(galaxies_o[gal1][0] - galaxies_o[gal2][0])
    distance2 = abs(galaxies_o[gal1][1] - galaxies_o[gal2][1])
    return distance1 + distance2

# calculate sum of shortest paths between all galaxy pairs in original universe

total_o = 0

for pair_o in galaxy_pairs_o:
    total_o += find_shortest_path(*pair_o)

print(f"The sum of the shortest paths between all galaxy pairs in the original universe is {total_o} steps.")

# find multiplication factor

difference = total-total_o
ten_times = difference*8
tenth_difference = ten_times + difference

total_steps = total_o
difference = tenth_difference
for i in range(6):
    total_steps += tenth_difference
    tenth_difference *= 10

print(f"According to new expansion rules the sum of the shortest paths between all galxy pairsis {total_steps} steps.")
