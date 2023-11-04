from character import Unit
from additions import ColorText


def duel_series(duelist_1: Unit, duelist_2: Unit, duels_number=100, max_rounds=100, show_fight_description=False):
    duel_result = 0
    for i in range(duels_number):  # TODO make it a function
        duel_result += start_duel(duelist_1, duelist_2, max_rounds, show_fight_description)
        duelist_1.long_rest()
        duelist_2.long_rest()
    print(duel_result)
    if duel_result == 0:
        print("A series of duels ended in a draw!")
    else:
        print(f"{duelist_1.name.title() if duel_result > 0 else duelist_2.name.title()} has won by {abs(duel_result)} duels!")


def start_duel(duelist_1: Unit, duelist_2: Unit, max_rounds: int, show_fight_description=False):
    current_round = 0
    attack_order: [Unit] = sorted([duelist_1, duelist_2], key=lambda x: x.get_initiative_roll())
    while (max_rounds > current_round and
           duelist_1.current_vitality_points > 0 and
           duelist_2.current_vitality_points > 0):
        if show_fight_description:
            perform_attack(attack_order[0].attack(attack_order[1]))
            perform_attack(attack_order[1].attack(attack_order[0]))
            print(duelist_1.current_vitality_points, duelist_1.name)
            print(duelist_2.current_vitality_points, duelist_2.name)
        else:
            attack_order[0].attack(attack_order[1])
            attack_order[1].attack(attack_order[0])
    print(duelist_1.current_vitality_points, duelist_1.name)
    print(duelist_2.current_vitality_points, duelist_2.name)

    return 1 if duelist_1.current_vitality_points > duelist_2.current_vitality_points else -1


def perform_attack(attack_result: Unit.attack):
    # TODO include 1 and 20 as a critical failure and a critical success respectively
    # A math here is fine, you just need to include things like a character's strength bonus.
    attack_roll: int = attack_result[0]
    damage_dealt: int = attack_result[1]
    damage_dice_result_list: list[int] = attack_result[2]
    participants: tuple[str] = attack_result[3]
    crit_occurence: bool = attack_result[4]
    if damage_dealt == 0:
        print(f"\n{participants[0].title()} rolled {attack_roll} and missed!"
              f"\n{participants[1].title()} is unscathed!")
    else:
        damage_rolls_str = ''
        if len(damage_dice_result_list) == 1:
            damage_rolls_str = damage_dice_result_list[0]
        elif len(damage_dice_result_list) >= 2:
            for damage in damage_dice_result_list[:-2]:
                damage_rolls_str += str(damage) + ', '
            damage_rolls_str += f"{damage_dice_result_list[-2]} and {damage_dice_result_list[-1]}"
        else:
            raise Exception("No damage rolls has been made!")
        print(f"\n{participants[0].title()} rolled {ColorText.green if crit_occurence else ''}{attack_roll}{ColorText.end + 'and landed a critical hit!' if crit_occurence else ' and hit!'}"
              f"\n{participants[0].title()} rolled", damage_rolls_str,
              f"for damage. \n{participants[1].title()} has lost {ColorText.red if damage_dealt >= 10 else ''}"
              f"{damage_dealt}{ColorText.end if damage_dealt >= 10 else ''} vitality points!\n")
