from additions import *
from csv import writer


class Weapon:
    name: str
    number_of_dice: int
    static_damage: int
    crit_chance: int
    multiplier_crit: int
    die_max_value: int
    damage_type: str
    normal_range: int
    long_range: int
    weapon_type: str
    price: int
    traits: list[str]

    initializer = False

    def __init__(self, name, damage_type, weapon_type='Unknown', weapon_range=None, die_max_value=1, number_of_dice=0,
                 static_damage=0, crit_chance=20,
                 multiplier_crit=2, add_to_list=True, price=0, traits=None):
        if weapon_range is None:
            weapon_range = 1
        if traits is None:
            self.traits = ['None']
        self.name = name
        self.number_of_dice = number_of_dice
        self.static_damage = static_damage
        self.crit_chance = crit_chance
        self.multiplier_crit = multiplier_crit
        self.die_max_value = die_max_value
        self.damage_type = damage_type
        self.weapon_type = weapon_type
        self.normal_range, self.long_range = range_parse(weapon_range)
        self.price = price

        if self.initializer:
            if name in WeaponList.weapon_dict.keys():
                raise Exception(f"'{name.title()}'There is already a weapon with that name!")
        else:
            Weapon.initializer = True
        if add_to_list:
            WeaponList.weapon_dict[self.name] = self

    def add_traits(self, *args: str):
        if 'None' in self.traits:
            self.traits.clear()
        for arg in args:
            self.traits.append(arg)

    def prepare_to_csv(self):
        return [self.name, f'{self.static_damage} + {self.number_of_dice}k{self.die_max_value}', self.damage_type, self.traits,
                self.multiplier_crit, self.crit_chance, f'{self.normal_range}|{self.long_range}', self.weapon_type,
                self.price]

    def show_status(self):
        print(
            f"\n{ColorText.green}{self.name.upper()}{ColorText.end}\nDamage: {str(self.static_damage) + ' + ' if self.static_damage > 0 else ''}"
            f"{f'{self.number_of_dice}k{self.die_max_value}' if self.number_of_dice * self.die_max_value != 0 else ''}"
            f"\nDamage type: {self.damage_type.title()}",
            f"\nTraits:", *[trait for trait in self.traits],
            f"\nCritical: {20 - self.crit_chance}-20x{self.multiplier_crit}\n"
            f"Range: {'melee' if self.normal_range == 1 else f'{self.normal_range}|{self.long_range}'}\n"
            f"Weapon type: {self.weapon_type.title()}")


class WeaponList:
    """
    It may be unnecessary to use __new__ and have everything as a class method,
    as some people may want to create different lists.
    However, I'm not sure why anyone would want to do that. For now, it stays like this.
    """
    weapon_dict: dict[str, Weapon] = {}
    unarmed = Weapon(name='unarmed', number_of_dice=0, die_max_value=0, static_damage=1, damage_type='bludgeoning',
                     weapon_range=1, add_to_list=False)

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeaponList, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_weapon_list(cls):
        print(f"{'*' * 10}\n")
        for weapon in cls.weapon_dict.values():
            weapon.show_status()
        print(f"\n{'*' * 10}")

    @classmethod
    def save_to_csv(cls, file_name):
        with open(this_dir + file_name + 'csv', mode='w') as file:
            csv_writer = writer(file, delimiter=';')
            for weapon in cls.weapon_dict.values():
                csv_writer.writerow(weapon.prepare_to_csv())

    # def get_by_name(cls, name) -> Weapon:
    #     for weapon in cls.weapon_list:
    #         if weapon.name == name:
    #             return weapon
    #     return Weapon(name='Fist', number_of_dice=1, die_max_value=1, damage_type='bludgeoning', range=1)


class Armor:
    name: str
    armor_class: int
    dex_bonus_limit: int
    armor_type: str
    strength_required: int
    traits: list

    def __init__(self, name, armor_class, dex_bonus_limit=99, armor_type=ArmorType.unknown, strength_required=-99, traits=None):
        self.name = name
        self.armor_class = armor_class
        self.dex_bonus_limit = dex_bonus_limit
        self.armor_type = armor_type
        self.strength_required = strength_required
        if traits:
            self.traits = traits
        else:
            self.traits = ["None"]

    def prepare_to_csv(self):
        return [self.name, self.armor_class, self.dex_bonus_limit, self.armor_type, self.strength_required, self.traits]

    def show_status(self):
        print(
            f"\n{ColorText.green}{self.name.upper()}{ColorText.end}"
            f"\nArmor class: {self.armor_class}"
            f"\nDex max bonus: {self.dex_bonus_limit}",
            f"\nArmor type: {self.armor_type}",
            f"\nStrength required: {self.strength_required}",
            f"\nTraits:", *[trait for trait in self.traits])


class ArmorList:
    """
    It may be unnecessary to use __new__ and have everything as a class method,
    as some people may want to create different lists.
    However, I'm not sure why anyone would want to do that. For now, it stays like this.
    """
    armor_dict: dict[str, Armor] = {}
    armorless = Armor(name="armorless", armor_class=0)

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ArmorList, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_armor_list(cls):
        print(f"{'*' * 10}\n")
        for weapon in cls.armor_dict.values():
            weapon.show_status()
        print(f"\n{'*' * 10}")

    @classmethod
    def save_to_csv(cls, file_name):
        with open(this_dir + file_name + 'csv', mode='w') as file:
            csv_writer = writer(file, delimiter=';')
            for armor in cls.armor_dict.values():
                csv_writer.writerow(armor.prepare_to_csv())

    # def get_by_name(cls, name) -> Weapon:
    #     for weapon in cls.weapon_list:
    #         if weapon.name == name:
    #             return weapon
    #     return Weapon(name='Fist', number_of_dice=1, die_max_value=1, damage_type='bludgeoning', range=1)
