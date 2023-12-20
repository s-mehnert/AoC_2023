# AoC 2023 --- Day 19 

# import puzzle input
imported_data = list()

with open("19_input.txt") as input:
    workflows, ratings = input.read().split("\n\n")
    imported_data = [workflows.split("\n"), ratings.split("\n")]

# Part 1

# format part ratings

workflows, ratings = imported_data

ratings = [[category.split("=") for category in rating.strip("{}").split(",")] for rating in ratings]
part_ratings = list()
for rating in ratings:
    rating_dict = dict()
    for category in rating:
        key, val = category
        rating_dict[key] = int(val)
    part_ratings.append(rating_dict)

workflows = [workflow.split("{") for workflow in workflows]
workflows_dict = dict()
for workflow in workflows:
    key, val = workflow
    workflows_dict[key] = val.strip("}")

print(workflows)
print(workflows_dict)

# unpack workflows

wf1 = "s<1351:px,qqz"
def unpack_rules(workflow):
    rules = workflow.split(",")
    return rules

print(unpack_rules(wf1))


