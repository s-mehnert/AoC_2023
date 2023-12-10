# AoC 2023 --- Day 10 

# import puzzle input
imported_data = list()

with open("10_input.txt") as input:
    for line in input.readlines():
        imported_data.append(list(line.strip("\n")))

# find starting position

def find_starting_pos(complete_maze):
    for row, line in enumerate(complete_maze):
        for col, pipe in enumerate(line):
            if pipe == "S":
                return row, col

starting_pos = find_starting_pos(imported_data)

pipe_shapes = {
    "J": ["west", "north"],
    "L": ["east", "north"],
    "F": ["east", "south"],
    "7": ["west", "south"],
    "-": ["east", "west"],
    "|": ["north", "south"]
}

# find connections

def connection_east(complete_maze, pos):
    row, col = pos
    connection = False
    try:
        east = complete_maze[row][col+1]
        if east in ["-", "J", "7"]:
            connection = True
    except: 
        return connection
    return connection

def connection_west(complete_maze, pos):
    row, col = pos
    connection = False
    try:
        west = complete_maze[row][col-1]
        if west in ["-", "L", "F"]:
            connection = True
    except: 
        return connection
    return connection

def connection_north(complete_maze, pos):
    row, col = pos
    connection = False
    try:
        north = complete_maze[row-1][col]
        if north in ["|", "7", "F"]:
            connection = True
    except: 
        return connection
    return connection

def connection_south(complete_maze, pos):
    row, col = pos
    connection = False
    try:
        south = complete_maze[row+1][col]
        if south in ["|", "L", "J"]:
            connection = True
    except: 
        return connection
    return connection

connections = {
    "south": connection_south,
    "north": connection_north,
    "east": connection_east,
    "west": connection_west
}

# replace starting position with correct pipe in complete_maze

def replace_starting_pos(complete_maze, starting_pos):
    possible_connections = list()
    if connection_east(complete_maze, starting_pos):
        possible_connections.append("east")
    if connection_west(complete_maze, starting_pos):
        possible_connections.append("west")
    if connection_north(complete_maze, starting_pos):
        possible_connections.append("north")
    if connection_south(complete_maze, starting_pos):
        possible_connections.append("south")
    for shape, directions in pipe_shapes.items():
        if directions == possible_connections:
            row, col = starting_pos
            complete_maze[row][col] = shape
            return complete_maze

complete_maze = replace_starting_pos(imported_data, starting_pos)

# find through complete_maze

def move(direction, pos):
    row, col = pos
    if direction == "south":
        return (row+1, col)
    if direction == "north":
        return (row-1, col)
    if direction == "east":
        return (row, col+1)
    if direction == "west":
        return (row, col-1)
    
def find_opposite_dir(direction):
    if direction == "north":
        return "south"
    if direction == "south":
        return "north"
    if direction == "east":
        return "west"
    if direction == "west":
        return "east"

def find_next_pos(pos, coming_from=None):
    row, col = pos
    dir1, dir2 = pipe_shapes[complete_maze[row][col]]
    if not coming_from or dir1 == coming_from:
        if connections[dir2](complete_maze, pos):
            return move(dir2, pos), find_opposite_dir(dir2)
    elif connections[dir1](complete_maze, pos):
        return move(dir1, pos), find_opposite_dir(dir1)
    
# next_1 = find_next_pos(starting_pos)
# print(next_1)
# next_pos, coming_from = next_1
# next_2 = find_next_pos(next_pos, coming_from)
# print(next_2)

path = [starting_pos]
next_pos = find_next_pos(starting_pos)

while next_pos[0] != starting_pos:
    pos, coming_from = next_pos
    path.append(pos)
    next_pos = find_next_pos(pos, coming_from)

print(f"The farthest point is {len(path)//2} steps away from the starting position.")
