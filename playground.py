from character import *
from weaponry import *


def build_basics():
    build_weapon_list()


if __name__ == '__main__':
    build_basics()
    aragorn = Unit(name='Aragorn', strength=16, dexterity=16,
                   constitution=14, intelligence=14,
                   wisdom=15, charisma=14,
                   level=12, character_class=CharacterClassList.undefined_class)

