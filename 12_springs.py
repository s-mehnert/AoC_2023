# AoC 2023 --- Day 12 

# import puzzle input
imported_data = list()

with open("12_input.txt") as input:
    for line in input.readlines():
        springs, report = line.split()
        report = report.split(",")
        imported_data.append((springs, report))

# Part 1

# interpret spring report facts

def find_facts(report_entry):
    springs, report = report_entry
    print(springs)
    facts = list()
    start = 0
    while start < len(springs) and count_springs(springs, start) >= 0:
        damaged = count_springs(springs, start)
        start += damaged
        facts.append(damaged)
        print(facts)
        print(start)
        print(damaged)
    return facts

def count_springs(springs, start=0):
    for idx, item in enumerate(springs, start):
        if item == "#":
            for i, spring in enumerate(springs[idx:]):
                if item != "#" or i == len(springs[idx:])-1:
                    return i+1
    return -1

#print(find_facts(imported_data[1]))

# experiment

entry = imported_data[1]
print()
line, report = entry
print("Line:", line, "\nReport:", report)
print()

new_line = list()
start = None
end = None

next_damaged_spring_group = int(report.pop(0))
for i, char in enumerate(line):
    print(i, char)
    if char == "?":
        length = next_damaged_spring_group
        if line[i:].startswith(length*"?") and (i+length >= len(line) or line[i+length] != "#"):
            new_line.append(length*"#")
            if i+length < len(line) and line[i+length+1] == "?":
                new_line.append(".")
                length += 1
            next_damaged_spring_group = int(report.pop(0))
            for times in range(length):
                continue
    else:
        new_line.append(char)

print("New line:", new_line)
    


