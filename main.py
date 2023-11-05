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
    df = pd.read_csv(weapon_list_dir, sep=';')
    aragorn = UnitList.get_unit('Aragorn')
    legolas = UnitList.get_unit('Legolas')
    check_basics()
    generic_actions.perform_attack(legolas.attack(aragorn, weapon=WeaponList.weapon_dict['short sword']))
    aragorn.put_on_weapon(WeaponList.weapon_dict['blaster'])
    legolas.put_on_weapon(WeaponList.weapon_dict['blaster'])
    print(WeaponList.weapon_dict.keys())
    open_app()
