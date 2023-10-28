import pandas as pd

from DnD_Tools import generic_actions
from DnD_Tools.content_builder import *
from DnD_Tools.character import Unit
from DnD_Tools.GUI import *


def build_basics():
    build_weapon_list()


if __name__ == '__main__':
    build_basics()
    df = pd.read_csv(weapon_list_dir, sep=';')
    print(df)
    # print(df.columns)
    # aragorn = Unit(name='Aragorn', strength=16, dexterity=16,
    #                constitution=14, intelligence=14,
    #                wisdom=15, charisma=14,
    #                level=12, character_class=CharacterClassList.undefined_class)
    # legolas = Unit(name='Legolas', strength=12, dexterity=19,
    #                constitution=12, intelligence=14,
    #                wisdom=16, charisma=12,
    #                level=12, character_class=CharacterClassList.undefined_class)
    # print(aragorn.vitality_points)
    # generic_actions.perform_attack(legolas.melee_attack(aragorn, weapon=WeaponList.weapon_dict['short sword']))
    # print(aragorn.vitality_points)
    # WeaponList.weapon_dict['blaster'].show_status()

    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

