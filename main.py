import pandas as pd

from DnD_Tools import generic_actions
from DnD_Tools.content_builder import *
from DnD_Tools.character import Unit
from DnD_Tools.GUI import *


def build_basics():
    build_weapon_list()
    build_classes_list()


if __name__ == '__main__':
    build_basics()
    df = pd.read_csv(weapon_list_dir, sep=';')
    print(df)
    # print(df.columns)
    aragorn = Unit(name='Aragorn', strength=16, dexterity=16,
                   constitution=14, intelligence=14,
                   wisdom=15, charisma=14,
                   level=12, character_class=CharacterClassList.undefined_class)
    legolas = Unit(name='Legolas', strength=12, dexterity=19,
                   constitution=12, intelligence=14,
                   wisdom=16, charisma=12,
                   level=12, character_class=CharacterClassList.undefined_class)
    generic_actions.perform_attack(legolas.attack(aragorn, weapon=WeaponList.weapon_dict['short sword']))
    aragorn.put_on_weapon(WeaponList.weapon_dict['blaster'])
    legolas.put_on_weapon(WeaponList.weapon_dict['blaster'])
    duel_result = 0
    for i in range(100):  # TODO make it a function
        duel_result += generic_actions.start_duel(aragorn, legolas, 99, True)
        aragorn.long_rest()
        legolas.long_rest()
    print(duel_result)

    # app = QApplication(sys.argv)
    # window = MyMainWindow()
    # window.show()
    # sys.exit(app.exec())

