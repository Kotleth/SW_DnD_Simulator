import pandas as pd

from DnD_Tools import generic_actions
from DnD_Tools.content_builder import *
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
    print(df)
    # aragorn = Unit(name='Aragorn', strength=16, dexterity=16,
    #                constitution=14, intelligence=14,
    #                wisdom=15, charisma=14,
    #                level=12, character_class=CharacterClassList.undefined_class)
    aragorn = UnitList.get_unit('Aragorn')
    legolas = UnitList.get_unit('Legolas')
    check_basics()
    generic_actions.perform_attack(legolas.attack(aragorn, weapon=WeaponList.weapon_dict['short sword']))
    aragorn.put_on_weapon(WeaponList.weapon_dict['blaster'])
    legolas.put_on_weapon(WeaponList.weapon_dict['blaster'])
    # generic_actions.duel_series(aragorn, legolas, show_fight_description=True)
    print("XDDDD")
    print(UnitList.units_dict.keys())
    print(WeaponList.weapon_dict.keys())
    Weapon(name='energy crossbow', static_damage=2, number_of_dice=2, die_max_value=6, crit_chance=19,
           multiplier_crit=2, damage_type='energy',
           weapon_range='crossbow')
    print(WeaponList.weapon_dict.keys())
    Unit(name='John', strength=16, dexterity=16,
         constitution=14, intelligence=14,
         wisdom=15, charisma=14,
         level=12, character_class=CharacterClassList.undefined_class)
    Unit(name='Bovi', strength=16, dexterity=16,
         constitution=14, intelligence=14,
         wisdom=15, charisma=14,
         level=12, character_class=CharacterClassList.undefined_class)
    # global window
    # app = QApplication(sys.argv)
    # window = MyMainWindow()
    # window.show()
    # sys.exit(app.exec_())

    open_app()
