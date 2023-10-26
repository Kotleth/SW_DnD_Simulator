from os import path
from csv import writer

# TODO builder for weapons, armors and character classes

this_dir = path.dirname(path.abspath(__file__))
weapon_list_dir = f"{this_dir}/weapon_list.csv"
print(weapon_list_dir)

weapon_list = [
    ['Name', 'Damage', 'Damage_type', 'Traits', 'Crit_multiplier', 'Crit_range', 'Range', 'Weapon_type', 'Price'],
    ['blaster', '1k10', 'energy', 'light', '2x', '19-20', '60|120', 'blaster', '200'],
    ['lightsaber', '2k6', 'energy', 'light, finesse', '2x', '19-20', 'melee', 'lightsaber', '800'],
    ]

with open(weapon_list_dir, mode='a') as file:
    csv_writer = writer(file)
    csv_writer.writerow()