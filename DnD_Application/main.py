# from DnD_Tools import generic_actions
import time

from DnD_Resources.content_builder import *
from DnD_Application.GUI import *
from DnD_Tools import map_essentials

def temporary(strength, prof, weapon_die, crit_chance):
    turn = 10
    ac = 15
    animal_str = 1
    dmg = 0
    for i in range(turn):
        hit_roll = r.randint(1, 20)
        if hit_roll + strength + prof > 20 - crit_chance:
            dmg += strength + r.randint(1, weapon_die)
        elif hit_roll + strength + prof >= ac:
            dmg += strength + r.randint(1, weapon_die) * 2
    return dmg/turn

if __name__ == '__main__':
    build_basics()
    battle_map = map_essentials.MapNoMesh(5, 5)
    damage_avg = []
    for i in range(10000):
        damage_avg.append(temporary(strength=1, prof=3, weapon_die=10, crit_chance=2))
    damage_avg_1 = 3 * 4.5 + 2.5 + 3
    open_app()


