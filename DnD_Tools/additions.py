from math import floor
from os import path
import random as r

this_dir = path.dirname(path.abspath(__file__))

weapons_ranges_associations_dict = {
                'melee': ['melee', 'close', 'saber', 'sword', 'blade', 'baton', 'knife', 'spear'],
                'short': ['short', 'blaster', 'pistol', 'bow'],
                'long': ['long', 'disruptor', 'gun', 'launcher', 'crossbow'],
                'very long': ['very', 'sniper', 'rifle', 'max'],
                }

damage_types = [
                "Acid",
                "Bludgeon",
                "Cold",
                "Electrical",
                "Energy",
                "Fire",
                "Ion",
                "Necrotic",
                "Piercing",
                "Poison",
                "Psychic",
                "Radiation",
                "Slashing",
                "Sound",
                ]


class DamageInstance:
    damage_dict: dict

    def __init__(self, damage_dict):
        self.damage_dict = damage_dict

    def full_damage(self):
        damage_dealt = 0
        for damage in self.damage_dict.values():
            damage_dealt += damage
        return damage_dealt


class Attribute:
    name: str
    value: int

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_bonus(self):
        return floor((self.value - 10)/2)


class CharacterClass:
    name: str
    vitality_dice: int

    initializer = False

    def __init__(self, name: str, vitality_dice: int, add_to_list=True):
        self.name = name.lower()
        self.vitality_dice = vitality_dice

        if self.initializer:
            if name in CharacterClassList.character_classes_dict.keys():
                raise Exception(f"'{name.title()}'There is already a class with that name!")
        else:
            CharacterClass.initializer = True
        if add_to_list:
            CharacterClassList.character_classes_dict[self.name] = self

    def show_status(self):
        print(f"{self.name.upper()}\nVitality die: k{self.vitality_dice}")


class CharacterClassList:
    character_classes_dict: dict[str, CharacterClass] = {}
    undefined_class = CharacterClass('undefined', 10, add_to_list=False)

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterClassList, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_classes_list(cls):
        print(f"{'*' * 10}\n")
        for character in cls.character_classes_dict.values():
            character.show_status()
        print(f"{'*' * 10}")


def range_parse(weapon_range):
    if type(weapon_range) is int:
        if weapon_range == 1:
            normal_range = 1
            long_range = 1
        elif weapon_range == 2:
            normal_range = 60
            long_range = 120
        elif weapon_range == 3:
            normal_range = 90
            long_range = 180
        elif weapon_range == 4:
            normal_range = 120
            long_range = 240
        else:
            raise ValueError("Incorrect range value!")
    elif type(weapon_range) is str:
        if '|' in weapon_range:
            range_list = weapon_range.split('|')
            normal_range = int(range_list[0])
            long_range = int(range_list[1])
        elif weapon_range in weapons_ranges_associations_dict['very long']:
            normal_range = 120
            long_range = 240
        elif weapon_range in weapons_ranges_associations_dict['long']:
            normal_range = 90
            long_range = 180
        elif weapon_range in weapons_ranges_associations_dict['short']:
            normal_range = 60
            long_range = 120
        elif weapon_range in weapons_ranges_associations_dict['melee']:
            normal_range = 1
            long_range = 1
        else:
            raise ValueError("Incorrect range value!")
    else:
        raise ValueError("Incorrect range value!")

    return normal_range, long_range


class ColorText:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def calc_weapon_damage(number_of_dice, die_max_value, damage=0):
    damage_dice_result_list = []
    for dice_number in range(number_of_dice):
        roll_result = r.randint(1, die_max_value)
        damage_dice_result_list.append(roll_result)
        damage += roll_result
    return damage_dice_result_list, damage



