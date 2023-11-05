from os import path
from csv import writer
from additions import CharacterClass, CharacterClassList
from weaponry import Weapon, WeaponList
from character import Unit, UnitList

# TODO builder for weapons, armors and character classes

this_dir = path.dirname(path.abspath(__file__))
weapon_list_dir = f"{this_dir}/weapon_list.csv"
print(weapon_list_dir)

weapon_list = [
    ['Name', 'Damage', 'Damage_type', 'Traits', 'Crit_multiplier', 'Crit_range', 'Range', 'Weapon_type', 'Price'],
    ['blaster', '1k10', 'energy', 'light', '2x', '19-20', '60|120', 'blaster', '200'],
    ['lightsaber', '2k6', 'energy', 'light, finesse', '2x', '19-20', 'melee', 'lightsaber', '800'],
]


def build_classes_list():
    """ Creates a classes list """
    CharacterClass(name='soldier', vitality_dice=12)
    CharacterClass(name='jedi knight', vitality_dice=10)
    CharacterClass(name='scoundrel', vitality_dice=8)


def build_weapon_list():
    """ Creates a weapons list """
    Weapon(name='long sword', number_of_dice=1, die_max_value=10, crit_chance=19, multiplier_crit=2, damage_type='slashing', weapon_range='sword')
    Weapon(name='short sword', number_of_dice=1, die_max_value=8, crit_chance=19, multiplier_crit=2, damage_type='slashing', weapon_range=1)
    Weapon(name='blaster', number_of_dice=1, die_max_value=10, crit_chance=19, multiplier_crit=2, damage_type='energy', weapon_range='blaster')
    Weapon(name='energy crossbow', static_damage=2, number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=2, damage_type='energy', weapon_range='crossbow')


def build_units_list():
    """ Creates a units list """
    Unit(name='Aragorn', strength=16, dexterity=16,
         constitution=14, intelligence=14,
         wisdom=15, charisma=14,
         level=12, character_class=CharacterClassList.undefined_class)
    Unit(name='Legolas', strength=12, dexterity=19,
         constitution=12, intelligence=14,
         wisdom=16, charisma=12,
         level=12, character_class=CharacterClassList.undefined_class)


# with open(weapon_list_dir, mode='a') as file:
#     csv_writer = writer(file, delimiter=';')
#     for weapon in weapon_list:
#         csv_writer.writerow(weapon)


# def essential_init():
