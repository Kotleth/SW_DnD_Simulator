import pandas as pd

from DnD_Tools import generic_actions
from content_builder import *
from DnD_Tools.GUI import *


def check_basics():
    assert any(list(WeaponList.weapon_dict.values())), "Weapons didn't initialized!"
    assert any(list(CharacterClassList.character_classes_dict.values())), "Character classes didn't initialized!"
    assert any(list(UnitList.units_dict.values())), "Units didn't initialized!"


def build_basics():
    build_weapon_list()
    build_classes_list()
    build_units_list()


if __name__ == '__main__':
    build_basics()
    check_basics()
    open_app()
