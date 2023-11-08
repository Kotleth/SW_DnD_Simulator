from math import ceil
from DnD_Tools.weaponry import *


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
    current_vitality_points: int
    proficiency: int
    resistances: list[str] = []
    feats_list: list[str] = []
    weapon: Weapon
    armor: Armor
    unit_id: int = None

    def __init__(self, name: str, strength: int, dexterity: int, constitution: int,
                 intelligence: int, wisdom: int, charisma: int, level: int,
                 character_class: CharacterClass, vitality_points: int = None, add_to_list=True):
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
        self._misc_modifiers = []  # is cleared after a long rest
        if vitality_points is None:
            self.vitality_points = character_class.vitality_dice + level * (
                    round((character_class.vitality_dice + 1) / 2) + self.constitution.get_bonus())
        else:
            self.vitality_points = vitality_points
        self.current_vitality_points = self.vitality_points

        if add_to_list:
            if name in UnitList.units_dict.keys():
                raise Exception(f"'{name.title()}'There is already a unit with that name!")
            else:
                UnitList.update_dict(self)

    def __copy__(self):
        new_instance = Unit(name=self.name, strength=self.strength.value, dexterity=self.dexterity.value,
                            constitution=self.constitution.value, intelligence=self.intelligence.value,
                            wisdom=self.wisdom.value, charisma=self.wisdom.value,
                            level=self.level, character_class=self.character_class, add_to_list=False)
        return new_instance

    def add_resistances(self, *resistances):
        for _resistance in resistances:
            self.resistances.append(_resistance)

    def add_feats(self, *feats):
        for _feat in feats:
            self.feats_list.append(_feat)

    def long_rest(self):
        self.current_vitality_points = self.vitality_points
        self._misc_modifiers.clear()

    def show_status(self):
        print("/\\" * 10)
        print(f"Name: {self.name}"
              f"\nClass: {self.character_class.name}\tLevel: {self.level}"
              f"\nAttributes:"
              f"\n\tStrength [STR]: {self.strength.value} [{'+' if self.strength.get_bonus() >= 0 else '-'}{(self.strength.get_bonus())}]"
              f"\n\tDexterity [DEX]: {self.dexterity.value} [{'+' if self.dexterity.get_bonus() >= 0 else '-'}{(self.dexterity.get_bonus())}]"
              f"\n\tConstitution [CON]: {self.constitution.value} [{'+' if self.constitution.get_bonus() >= 0 else '-'}{(self.constitution.get_bonus())}]"
              f"\n\tIntelligence [INT]: {self.intelligence.value} [{'+' if self.intelligence.get_bonus() >= 0 else '-'}{(self.intelligence.get_bonus())}]"
              f"\n\tWisdom [WIS]: {self.wisdom.value} [{'+' if self.wisdom.get_bonus() >= 0 else '-'}{(self.wisdom.get_bonus())}]"
              f"\n\tCharisma [CHA]: {self.charisma.value} [{'+' if self.charisma.get_bonus() >= 0 else '-'}{(self.charisma.get_bonus())}]"
              f"\nProficiency: {self.proficiency}"
              f"\nArmor class: {self.armor_class}\t Vitality points: {self.current_vitality_points}/{self.vitality_points}"
              )
        print("\\/" * 10)

    def take_off_armor(self):
        self.armor = None
        self.armor_class = 10 + self.dexterity.get_bonus()

    def put_on_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def put_on_armor(self, armor: Armor):
        if self.strength.value >= armor.strength_required:
            self.armor = armor
            self.armor_class = self.armor.armor_class + min(self.dexterity.get_bonus(), self.armor.dex_bonus_limit)
            return True
        else:
            print("You have not enough strength to wear this armor!")
            return False

    def show_resistances(self):
        print(f"RESISTANCES OF {self.name}\n")
        for _resistance in self.resistances:
            print(_resistance)
        print(f"\n{'*' * 10}")

    def get_initiative_roll(self):
        return self.dexterity.get_bonus() + r.randint(1, 20)

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
            self.current_vitality_points -= damage_dealt
        else:
            pass

        return damage_dealt

    def attack(self, target, weapon: Weapon = None, to_hit_misc_bonus=0):
        crit_occurrence = False
        crit_damage_dice_result_list = []
        damage_dealt = 0
        attacker_name = self.name
        defender_name = target.name
        if self.unit_id is not None:
            attacker_name += f" [{self.unit_id}]"
        if target.unit_id is not None:
            defender_name += f" [{target.unit_id}]"
        participants = (attacker_name, defender_name)
        crit_multiplier = 1
        if weapon is None:
            weapon = self.weapon
        if weapon.normal_range == 1:
            stat_bonus_damage = self.strength.get_bonus()
        else:
            stat_bonus_damage = 0
        attack_roll = r.randint(1, 20)
        # critical failure
        if attack_roll == 1:
            hit_value = 0
            damage = 0
            crit_multiplier = 0
        # critical success
        elif attack_roll == 20:
            hit_value = 99
            damage = weapon.static_damage + stat_bonus_damage
            crit_multiplier = weapon.multiplier_crit
            crit_occurrence = True
        # normal attack
        else:
            hit_value = stat_bonus_damage + self.proficiency + to_hit_misc_bonus + attack_roll
            damage = weapon.static_damage + stat_bonus_damage
            # in the critical threat range but not 20, for d&d5 just remove this
            if attack_roll >= weapon.crit_chance:
                crit_verification = r.randint(1, 20) + stat_bonus_damage + self.proficiency + to_hit_misc_bonus
                if crit_verification >= target.armor_class:
                    crit_damage_dice_result_list, crit_damage = calc_weapon_damage(weapon.number_of_dice,
                                                                                   weapon.die_max_value)
                    damage_dealt += target.get_damage(hit_value=hit_value,
                                                      damage_instance=DamageInstance({weapon.damage_type: crit_damage}),
                                                      weapon_range=weapon.normal_range)
                    crit_occurrence = True
        damage_dice_result_list, damage = calc_weapon_damage(weapon.number_of_dice * crit_multiplier,
                                                             weapon.die_max_value, damage)
        # pycharm will tell you that parameter self is unfulfilled but don't listen to him, he is lying
        damage_dealt += target.get_damage(hit_value=hit_value,
                                          damage_instance=DamageInstance({weapon.damage_type: damage}),
                                          weapon_range=weapon.normal_range)

        return attack_roll, damage_dealt, damage_dice_result_list + crit_damage_dice_result_list, participants, crit_occurrence


class UnitList:
    units_dict: dict[str, Unit] = {}
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UnitList, cls).__new__(cls)
        return cls._instance

    @classmethod
    def update_dict(cls, unit: Unit):
        cls.units_dict[unit.name] = unit

    @classmethod
    def get_unit(cls, unit_name):
        return cls.units_dict[unit_name]

    @classmethod
    def get_classes_list(cls):
        print(f"{'*' * 10}\n")
        for unit in cls.units_dict.values():
            unit.show_status()
        print(f"{'*' * 10}")
