import random as r
from math import ceil
from weaponry import *
from additions import *
from typing import Type


class Unit:
    name: str
    character_class: CharacterClass
    level: int
    strength: Attribute
    dexterity: Attribute
    constitution: Attribute
    intelligence: Attribute
    wisdom: Attribute
    charisma: Attribute
    armor_class: int
    vitality_points: int
    proficiency: int
    resistances: list[str] = []
    weapon: Weapon
    armor: Armor

    def __init__(self, name: str, strength: int, dexterity: int, constitution: int,
                 intelligence: int, wisdom: int, charisma: int, level: int,
                 character_class: CharacterClass):
        self.character_class = character_class
        self.level = level
        self.name = name
        self.proficiency = ceil((level + 1) / 3) + 1
        self.strength = Attribute("strength", strength)
        self.dexterity = Attribute("dexterity", dexterity)
        self.constitution = Attribute("constitution", constitution)
        self.intelligence = Attribute("intelligence", intelligence)
        self.wisdom = Attribute("wisdom", wisdom)
        self.charisma = Attribute("charisma", charisma)
        self.armor_class = 10 + self.dexterity.get_bonus()
        self.weapon = WeaponList.unarmed
        self.vitality_points = character_class.vitality_dice + level * (
                round((character_class.vitality_dice + 1) / 2) + self.constitution.get_bonus())

    def add_resistance(self, resistance):
        self.resistances.append(resistance)

    def reset_armor(self):
        self.armor_class = 10 + self.dexterity.get_bonus()

    def put_on_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def show_resistances(self):
        print(f"RESISTANCES OF {self.name}\n")
        for _resistance in self.resistances:
            print(_resistance)
        print(f"\n{'*' * 10}")

    def get_damage(self, damage_instance: DamageInstance, weapon_range, hit_value=99):
        if weapon_range > 1:
            pass  # TODO
        damage_dealt = 0
        if hit_value >= self.armor_class:
            for damage_type, damage in damage_instance.damage_dict.items():
                if damage_type in self.resistances:
                    damage_dealt += ceil(damage / 2)
                else:
                    damage_dealt += damage
            self.vitality_points -= damage_dealt
        else:
            pass

        return damage_dealt

    def attack(self, target: Type['Unit'], weapon: Weapon = None, to_hit_misc_bonus=0):
        crit_occurrence = False
        crit_damage_dice_result_list = []
        damage_dealt = 0
        participants = (self.name, target.name)
        crit_multiplier = 1
        if weapon is None:
            weapon = self.weapon
        attack_roll = r.randint(1, 20)
        if attack_roll == 1:
            hit_value = 0
            damage = 0
            crit_multiplier = 0
        elif attack_roll == 20:
            hit_value = 99
            damage = weapon.static_damage + self.strength.get_bonus()
            crit_multiplier = weapon.multiplier_crit
            crit_occurrence = True
        else:
            hit_value = self.strength.get_bonus() + self.proficiency + to_hit_misc_bonus + attack_roll
            damage = weapon.static_damage + self.strength.get_bonus()
            if attack_roll >= weapon.crit_chance:
                crit_verification = r.randint(1, 20) + self.strength.get_bonus() + self.proficiency + to_hit_misc_bonus
                if crit_verification >= target.armor_class:
                    crit_damage_dice_result_list, crit_damage = calc_weapon_damage(weapon.number_of_dice, weapon.die_max_value)
                    damage_dealt += target.get_damage(hit_value=hit_value,
                                                      damage_instance=DamageInstance({weapon.damage_type: crit_damage}),
                                                      weapon_range=weapon.normal_range)
                    crit_occurrence = True
        damage_dice_result_list, damage = calc_weapon_damage(weapon.number_of_dice * crit_multiplier, weapon.die_max_value, damage)
        # pycharm will tell you that parameter self is unfulfilled but don't listen to him, he is lying
        damage_dealt += target.get_damage(hit_value=hit_value, damage_instance=DamageInstance({weapon.damage_type: damage}),
                                                      weapon_range=weapon.normal_range)

        return attack_roll, damage_dealt, damage_dice_result_list + crit_damage_dice_result_list, participants, crit_occurrence

    # def range_attack(self, target: Type['Unit'], weapon: Weapon = None, to_hit_misc_bonus=0):
    #     crit_occurrence = False
    #     damage_dice_result_list = []
    #     participants = (self.name, target.name)
    #     crit_multiplier = 1
    #     if weapon is None:
    #         weapon = self.weapon
    #     attack_roll = r.randint(1, 20)
    #     if attack_roll == 1:
    #         hit_value = 0
    #         damage = 0
    #         crit_multiplier = 0
    #     elif attack_roll == 20:
    #         hit_value = 99
    #         damage = weapon.static_damage + self.strength.get_bonus()
    #         crit_multiplier = weapon.multiplier_crit
    #         crit_occurrence = True
    #     else:
    #         hit_value = self.strength.get_bonus() + self.proficiency + to_hit_misc_bonus + attack_roll
    #         damage = weapon.static_damage + self.strength.get_bonus()
    #         if attack_roll >= weapon.crit_chance:
    #             crit_verification = r.randint(1, 20) + self.strength.get_bonus() + self.proficiency + to_hit_misc_bonus
    #             if crit_verification >= target.armor_class:
    #                 crit_multiplier = weapon.multiplier_crit
    #                 crit_occurrence = True
    #     for dice_number in range(weapon.number_of_dice * crit_multiplier):
    #         roll_result = r.randint(1, weapon.die_max_value)
    #         damage_dice_result_list.append(roll_result)
    #         damage += roll_result
    #     damage_instance = DamageInstance({weapon.damage_type: damage})
    #     # pycharm will tell you that parameter self is unfulfilled but don't listen to him, he is lying
    #     damage_dealt = target.get_damage(hit_value=hit_value, damage_instance=damage_instance,
    #                                      attack_type="ranged")
    #
    #     return attack_roll, damage_dealt, damage_dice_result_list, participants, crit_occurrence


class UnitList:
    units_dict: dict[str, Unit] = {}
    aragorn = Unit(name='Aragorn', strength=16, dexterity=16,
                   constitution=14, intelligence=14,
                   wisdom=15, charisma=14,
                   level=12, character_class=CharacterClassList.undefined_class)

    @classmethod
    def get_classes_list(cls):
        print(f"{'*' * 10}\n")
        for unit in cls.units_dict.values():
            unit.show_status()
        print(f"{'*' * 10}")
