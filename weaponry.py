from additions import DamageInstance


class Weapon:
    name: str
    number_of_dice: int
    damage: int
    crit_chance: int
    multiplier_crit: int
    die_max_value: int
    damage_type: str
    range: int

    def __init__(self, name, damage_type, range=1, die_max_value=1, number_of_dice=0, damage=0, crit_chance=1,
                 multiplier_crit=2):
        self.name = name
        self.number_of_dice = number_of_dice
        self.damage = damage
        self.crit_chance = crit_chance
        self.multiplier_crit = multiplier_crit
        self.die_max_value = die_max_value
        self.damage_type = damage_type
        self.range = range
        WeaponList.weapon_dict[self.name] = self

    def show_status(self):
        print(f"{self.name.upper()}\nDamage: {self.damage} + "
              f"{f'{self.number_of_dice}k{self.die_max_value}' if self.number_of_dice * self.die_max_value != 0 else ''} \n"
              f"Damage type: {self.damage_type.title()}\n"
              f"Critical: {20 - self.crit_chance}-20x{self.multiplier_crit}\n"
              f"Range: {'melee' if self.range == 1 else f'{self.range}|{self.range * 2}'}\n")

class WeaponList:
    weapon_dict: dict[str, Weapon] = {}

    @staticmethod
    def get_weapon_list():
        print(f"{'*' * 10}\n")
        for weapon in WeaponList.weapon_dict.values():
            weapon.show_status()
        print(f"{'*' * 10}")

    # def get_by_name(self, name) -> Weapon:
    #     for weapon in self.weapon_list:
    #         if weapon.name == name:
    #             return weapon
    #     return Weapon(name='Fist', number_of_dice=1, die_max_value=1, damage_type='bludgeoning', range=1)


def build_weapon_list():
    """ Creates a weapon list """
    Weapon(name='Long sword', number_of_dice=1, die_max_value=10, damage_type='slashing', range=1)
    Weapon(name='Short sword', number_of_dice=1, die_max_value=8, damage_type='slashing', range=1)
    Weapon(name='Fist', number_of_dice=0, die_max_value=0, damage=1, damage_type='bludgeoning', range=1)
    WeaponList.get_weapon_list()

