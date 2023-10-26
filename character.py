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
        print(f"\n{'*'*10}")

    def get_damage(self, hit_chance, damage_instance: DamageInstance, attack_type):
        if attack_type.lower() == "ranged":
            pass  # TODO
        attack_roll = r.randint(1, 20)
        damage_dealt = 0
        if attack_roll + hit_chance >= self.armor_class:
            for damage_type, damage in damage_instance.damage_dict.items():
                if damage_type in self.resistances:
                    damage_dealt += ceil(damage/2)
                else:
                    damage_dealt += damage
            self.vitality_points -= damage_dealt
        else:
            pass

        return attack_roll, damage_dealt

    def range_attack(self):
        # TODO
        return 0, 0, [0]

    def melee_attack(self, target: Type['Unit'], weapon: Weapon = None, to_hit_bonus=0):
        damage_dice_result_list = []
        participants = (self.name, target.name)
        if weapon is None:
            weapon = self.weapon
        hit_chance = self.strength.get_bonus() + self.proficiency + to_hit_bonus
        damage = weapon.damage + self.strength.get_bonus()
        for dice_number in range(weapon.number_of_dice):
            roll_result = r.randint(1, weapon.die_max_value)
            damage_dice_result_list.append(roll_result)
            damage += roll_result
        damage_instance = DamageInstance({weapon.damage_type: damage})
        # pycharm will tell you that parameter self is unfulfilled but don't listen to him, he is lying
        attack_roll, damage_dealt = target.get_damage(hit_chance=hit_chance, damage_instance=damage_instance, attack_type="melee")

        return attack_roll, damage_dealt, damage_dice_result_list, participants





