# AoC 2023 --- Day 5 

# import puzzle input
imported_data = list()

with open("05_input.txt") as input:
    imported_data = input.read().split("\n\n")

# format data into suitable data_structures

pop_off_list = list(reversed(imported_data))

seeds = [int(seed) for seed in pop_off_list.pop().split()[1:]]
print("Seeds:", seeds)

seed_to_soil = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Seed-to-Soil Map:", seed_to_soil)

soil_to_fertilizer = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Soil-to-Fertilizer Map:", soil_to_fertilizer)

fertilizer_to_water = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Fertilizer-to-Water Map:", fertilizer_to_water)

water_to_light = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Water-to-Light Map:", water_to_light)

light_to_temperature = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Light-to-Temperature Map:", light_to_temperature)

temperature_to_humidity = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Temperature-to-Humidity Map:", temperature_to_humidity)

humidity_to_location = [tuple(int(num) for num in entry.split()) for entry in pop_off_list.pop().split("\n")[1:]]
print("Humidity-to-Location Map:", humidity_to_location)

del pop_off_list

# Part 1
