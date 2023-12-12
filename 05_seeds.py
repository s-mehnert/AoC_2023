# AoC 2023 --- Day 5 

# import puzzle input
imported_data = list()

with open("05_input.txt") as input:
    imported_data = input.read().split("\n\n")

# format data into suitable data_structures

pop_off_list = list(reversed(imported_data))

seeds = [int(seed) for seed in pop_off_list.pop().split()[1:]]
seed_to_soil = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
soil_to_fertilizer = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
fertilizer_to_water = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
water_to_light = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
light_to_temperature = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
temperature_to_humidity = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
humidity_to_location = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]

del pop_off_list

# Part 1

def find_destination(source, map):
    for rule in map:
        dest, start, length = rule
        if source in range(start, start+length):
            return dest+source-start
    return source

soil_destinations = [find_destination(seed, seed_to_soil) for seed in seeds]
fertilizer_destinations = [find_destination(soil, soil_to_fertilizer) for soil in soil_destinations]
water_destinations = [find_destination(fertilizer, fertilizer_to_water) for fertilizer in fertilizer_destinations]
light_destinations = [find_destination(water, water_to_light) for water in water_destinations]
temperature_destinations = [find_destination(light, light_to_temperature) for light in light_destinations]
humidity_destinations = [find_destination(temperature, temperature_to_humidity) for temperature in temperature_destinations]
locations = [find_destination(humidity, humidity_to_location) for humidity in humidity_destinations]

print("The lowest location number is:", min(locations))

# Part 2

seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

seeds_part_2 = list()
for tup in seed_ranges:
    for i in range(tup[0], tup[0]+tup[1]):
        seeds_part_2.append(i)

soil_destinations = [find_destination(seed, seed_to_soil) for seed in seeds_part_2]
fertilizer_destinations = [find_destination(soil, soil_to_fertilizer) for soil in soil_destinations]
water_destinations = [find_destination(fertilizer, fertilizer_to_water) for fertilizer in fertilizer_destinations]
light_destinations = [find_destination(water, water_to_light) for water in water_destinations]
temperature_destinations = [find_destination(light, light_to_temperature) for light in light_destinations]
humidity_destinations = [find_destination(temperature, temperature_to_humidity) for temperature in temperature_destinations]
locations = [find_destination(humidity, humidity_to_location) for humidity in humidity_destinations]

print("The lowest location number with seed ranges is:", min(locations))