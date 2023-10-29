from math import floor
from os import path


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

    def __init__(self, name, vitality_dice):
        self.name = name
        self.vitality_dice = vitality_dice

    def show_status(self):
        print(f"{self.name.upper()}\nVitality die: k{self.vitality_dice}")


class CharacterClassList:
    character_classes_dict: dict[str, CharacterClass] = {}
    undefined_class = CharacterClass('undefined', 10)

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



