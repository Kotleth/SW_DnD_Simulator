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
    red = '<span style="color:red;">'
    green = '<span style="color:green;">'
    yellow = '<span style="color:yellow;">'
    end = '</span>'
    blue = '<span style="color:blue;">'
    cyan = '<span style="color:cyan;">'
    bold = '<span style="font-weight:bold;">'
    underline = '<span style="text-decoration:underline;">'


def calc_weapon_damage(number_of_dice, die_max_value, damage=0):
    damage_dice_result_list = []
    for dice_number in range(number_of_dice):
        roll_result = r.randint(1, die_max_value)
        damage_dice_result_list.append(roll_result)
        damage += roll_result
    return damage_dice_result_list, damage


def parse_weapon_damage(damage: str) -> (int, int, int):
    """Returns: static damage, number_of_dice, die_max_value"""
    damage = damage.replace(" ", "")
    if '+' in damage and 'k' in damage:
        static_damage, dice_damage = damage.split("+")
        number_of_dice, die_max_value = dice_damage.split("k")
    elif 'k' in damage:
        static_damage = 0
        number_of_dice, die_max_value = damage.split("k")
    else:
        try:
            static_damage = int(damage)
            number_of_dice = 0
            die_max_value = 0
        except Exception as e:
            print(f"Error = {e}")
            print(f"Damage = {damage}")
            raise ValueError("Wrong format of damage!")
    return int(static_damage), int(number_of_dice), int(die_max_value)


class DamageTypes:
    acid = "Acid"
    bludgeon = "Bludgeon"
    cold = "Cold"
    electrical = "Electrical"
    energy = "Energy"
    fire = "Fire"
    ion = "Ion"
    necrotic = "Necrotic"
    piercing = "Piercing"
    poison = "Poison"
    psychic = "Psychic"
    radiation = "Radiation"
    slashing = "Slashing"
    sound = "Sound"


class ArmorType:
    unknown = 'unknown'
    light = 'light'
    medium = 'medium'
    heavy = 'heavy'
    power = 'power'


class Position:
    x_coord: int
    y_coord: int

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def distance(self, other_position):
        return ((self.x_coord - other_position.x_coord)**2 + (self.y_coord - other_position.y_coord)**2)**0.5

    def set(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def get(self):
        return self.x_coord, self.y_coord
