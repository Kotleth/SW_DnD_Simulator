from character import Unit
from additions import ColorText


def duel_series(duelist_1: Unit, duelist_2: Unit, duels_number=100, max_rounds=100, show_fight_description=False):
    duel_result = 0
    for i in range(duels_number):
        duel_result += start_duel(duelist_1, duelist_2, max_rounds, show_fight_description)
        duelist_1.long_rest()
        duelist_2.long_rest()
    if duel_result == 0:
        print("A series of duels ended in a draw!")
    else:
        print(f"{duelist_1.name.title() if duel_result > 0 else duelist_2.name.title()} has won by {abs(duel_result)} duels!")


def start_battle(team_even, team_odd, max_rounds=100):
    current_round = 0
    fallen_list = []
    battle_report = []
    attack_order: list[Unit] = sorted(team_even + team_odd, key=lambda x: x.get_initiative_roll())
    team_even_hp = sum(unit.current_vitality_points for unit in team_even)
    team_odd_hp = sum(unit.current_vitality_points for unit in team_odd)
    for member in attack_order:
        print(f"{member.name} has {member.weapon.name} as a weapon. Damage = {member.weapon.static_damage}. Crit = {member.weapon.crit_chance}")
    while (max_rounds >= current_round and
            team_even_hp > 0 and
            team_odd_hp > 0):
        for attacking_unit in attack_order:
            if attacking_unit.current_vitality_points < 1:
                continue
            if is_odd(attacking_unit.unit_id):
                battle_finished, attack_order, battle_report, fallen_list = \
                    make_attack_action(attacking_unit, attack_order, battle_report, fallen_list, is_even)
            else:
                battle_finished, attack_order, battle_report, fallen_list = \
                    make_attack_action(attacking_unit, attack_order, battle_report, fallen_list, is_odd)
            if battle_finished:
                break
        current_round += 1
        team_even_hp = sum(unit.current_vitality_points for unit in team_even)
        team_odd_hp = sum(unit.current_vitality_points for unit in team_odd)
    battle_report.append(f"THE BATTLE HAS ENDED<br>")
    for fallen in fallen_list:
        battle_report.append(f"{fallen.name} [{fallen.unit_id}] has fallen!")
    for winner in attack_order:
        battle_report.append(f"{winner.name} [{winner.unit_id}] has survived!")

    if all([is_odd(unit.unit_id) for unit in attack_order]):
        battle_report.append("<br>Team Odd has won!")
    elif all([is_even(unit.unit_id) for unit in attack_order]):
        battle_report.append("<br>Team Even has won!")
    elif max_rounds <= current_round or not attack_order:
        battle_report.append("<br>Fight ended with a draw!")
    else:
        battle_report.append("Fight ended with an unexpected result! Check code!<br>")
        raise Exception("Fight ended with an unexpected result! Check code!")
    return battle_report


def make_attack_action(attacking_unit, attack_order, battle_report, fallen_list, enemy_id_func):
    battle_finished = False
    if any([enemy_id_func(unit.unit_id) for unit in attack_order]):
        for defending_unit in attack_order:
            if enemy_id_func(defending_unit.unit_id):
                battle_report.append(perform_attack(attacking_unit.attack(defending_unit)))
                if defending_unit.current_vitality_points < 1:
                    attack_order = [fighter for fighter in attack_order if fighter != defending_unit]
                    fallen_list.append(defending_unit)
                    battle_report.append(f"{ColorText.red}{defending_unit.name} [{defending_unit.unit_id}] has fallen!{ColorText.end}<br>")
                break
    else:
        battle_finished = True
    return battle_finished, attack_order, battle_report, fallen_list


def start_duel(duelist_1: Unit, duelist_2: Unit, max_rounds: int, show_fight_description=False):
    current_round = 0
    attack_order: [Unit] = sorted([duelist_1, duelist_2], key=lambda x: x.get_initiative_roll())
    while (max_rounds >= current_round and
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
        current_round += 1
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
        final_message = f"<p>{participants[0].title()} has rolled {attack_roll} and missed!<br>{participants[1].title()} is unscathed!<br></p>"
    else:
        damage_rolls_str = ''
        if len(damage_dice_result_list) == 1:
            damage_rolls_str = damage_dice_result_list[0]
        elif len(damage_dice_result_list) >= 2:
            for damage in damage_dice_result_list[:-2]:
                damage_rolls_str += str(damage) + ', '
            damage_rolls_str += f"{damage_dice_result_list[-2]} and {damage_dice_result_list[-1]}"
        else:
            damage_rolls_str += 'no dice'
        final_message = f"<p>{participants[0].title()} has rolled {ColorText.green if crit_occurence else ''}{attack_roll}{ColorText.end + ' and landed a critical hit!' if crit_occurence else ' and hit!'}<br>"\
                        + f"{participants[0].title()} has rolled " + str(damage_rolls_str) \
                        + f" for damage.<br>{participants[1].title()} has lost {ColorText.red if damage_dealt >= 10 else ''}"\
                        + f"{damage_dealt}{ColorText.end if damage_dealt >= 10 else ''} vitality points!<br></p>"
    return final_message


def is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
