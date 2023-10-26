from additions import *


class Weapon:
    name: str
    number_of_dice: int
    damage: int
    crit_chance: int
    multiplier_crit: int
    die_max_value: int
    damage_type: str
    normal_range: int
    long_range: int
    weapon_type: str
    price: int
    traits: list[str]

    def __init__(self, name, damage_type, weapon_type='Unknown', weapon_range=None, die_max_value=1, number_of_dice=0, damage=0, crit_chance=1,
                 multiplier_crit=2, add_to_list=True, price=0, traits=None):
        if weapon_range is None:
            weapon_range = 1
        if traits is None:
            self.traits = ['None']
        self.name = name
        self.number_of_dice = number_of_dice
        self.damage = damage
        self.crit_chance = crit_chance
        self.multiplier_crit = multiplier_crit
        self.die_max_value = die_max_value
        self.damage_type = damage_type
        self.weapon_type = weapon_type
        self.normal_range, self.long_range = range_parse(weapon_range)
        self.price = price

        # if name in WeaponList.weapon_dict.keys():
        #     raise Exception("There is already a weapon with that name!")
        if add_to_list:
            WeaponList.weapon_dict[self.name] = self

    def add_traits(self, *args: str):
        if 'None' in self.traits:
            self.traits.clear()
        for arg in args:
            self.traits.append(arg)

    def show_status(self):
        print(f"\n{ColorText.green}{self.name.upper()}{ColorText.end}\nDamage: {str(self.damage) + ' + ' if self.damage > 0 else ''}"
              f"{f'{self.number_of_dice}k{self.die_max_value}' if self.number_of_dice * self.die_max_value != 0 else ''}"
              f"\nDamage type: {self.damage_type.title()}",
              f"\nTraits:", *[trait for trait in self.traits],
              f"\nCritical: {20 - self.crit_chance}-20x{self.multiplier_crit}\n"
              f"Range: {'melee' if self.normal_range == 1 else f'{self.normal_range}|{self.long_range}'}\n"
              f"Weapon type: {self.weapon_type.title()}")


class WeaponList:
    weapon_dict: dict[str, Weapon] = {}
    unarmed = Weapon(name='unarmed', number_of_dice=0, die_max_value=0, damage=1, damage_type='bludgeoning', weapon_range=1, add_to_list=False)

    @classmethod
    def get_weapon_list(cls):
        print(f"{'*' * 10}\n")
        for weapon in cls.weapon_dict.values():
            weapon.show_status()
        print(f"\n{'*' * 10}")

    # def get_by_name(self, name) -> Weapon:
    #     for weapon in self.weapon_list:
    #         if weapon.name == name:
    #             return weapon
    #     return Weapon(name='Fist', number_of_dice=1, die_max_value=1, damage_type='bludgeoning', range=1)


def build_weapon_list():
    """ Creates a weapon list """
    Weapon(name='long sword', number_of_dice=1, die_max_value=10, damage_type='slashing', weapon_range='sword')
    Weapon(name='short sword', number_of_dice=1, die_max_value=8, damage_type='slashing', weapon_range=1)
    Weapon(name='blaster', number_of_dice=1, die_max_value=10, damage_type='energy', weapon_range='blaster')
    Weapon(name='energy crossbow', damage=2, number_of_dice=2, die_max_value=6, damage_type='energy', weapon_range='crossbow')
    WeaponList.get_weapon_list()


class Armor:
    name: str
    armor_class: int
    dex_bonus_limit: int
    type: str
    strength_required: int
    traits: list

