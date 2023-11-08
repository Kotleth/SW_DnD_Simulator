from csv import writer, reader
from DnD_Tools.additions import *
from DnD_Tools.weaponry import Weapon, WeaponList, Armor, ArmorList
from DnD_Tools.character import Unit, UnitList

# TODO builder for weapons, armors and character classes

resources_dir = path.dirname(path.abspath(__file__))
# resources_dir = this_dir + "/DnD_Resources"
weapon_list_dir = f"{resources_dir}/weapon_list.csv"
armor_list_dir = f"{resources_dir}/armor_list.csv"

weapon_list_header = ['Name', 'Damage', 'Damage_type', 'Traits', 'Crit_multiplier', 'Crit_range', 'Range', 'Weapon_type', 'Price']
armor_list_header = ['Name', 'Armor_Class', 'Dex_Bonus_Limit', 'Armor_Type', 'Strength_Required', 'Traits', 'Cost']


def build_classes_list():
    """ Creates a classes list """
    CharacterClass(name='soldier', vitality_dice=12)
    CharacterClass(name='jedi knight', vitality_dice=10)
    CharacterClass(name='force adept', vitality_dice=10)
    CharacterClass(name='leader', vitality_dice=10)
    CharacterClass(name='technician', vitality_dice=10)
    CharacterClass(name='scoundrel', vitality_dice=8)


def build_armor_list():
    """ Creates a weapons list """
    with open(armor_list_dir, mode='r') as file:
        csv_reader = reader(file, delimiter=';')
        for number, row in enumerate(csv_reader):
            if number == 0:
                continue
            print(row)
            print(parse_weapon_from_csv(row))


def build_weapon_list():
    """ Creates a weapons list """
    with open(weapon_list_dir, mode='r') as file:
        csv_reader = reader(file, delimiter=';')
        for number, row in enumerate(csv_reader):
            if number == 0:
                continue
            parse_weapon_from_csv(row)


def build_units_list():
    """ Creates a units list """
    Unit(name='Aragorn', strength=16, dexterity=16,
         constitution=14, intelligence=14,
         wisdom=15, charisma=14,
         level=12, character_class=CharacterClassList.undefined_class)
    Unit(name='Legolas', strength=12, dexterity=19,
         constitution=12, intelligence=14,
         wisdom=16, charisma=12,
         level=12, character_class=CharacterClassList.undefined_class)


def parse_weapon_from_csv(csv_row):
    static_damage, number_of_dice, die_max_value = parse_weapon_damage(csv_row[1])
    return Weapon(name=csv_row[0], static_damage=int(static_damage), number_of_dice=int(number_of_dice), die_max_value=int(die_max_value),
           damage_type=csv_row[2], traits=list(csv_row[3]), multiplier_crit=int(csv_row[4]), crit_chance=int(csv_row[5]),
           weapon_range=csv_row[6], weapon_type=csv_row[7], price=int(csv_row[8]))


def _make_armor_csv():
    """Those are made in case of csv files were deleted"""
    Armor(name="Padawan Robe", armor_class=1, dex_bonus_limit=8, armor_type="robes")
    Armor(name="Jedi Robe", armor_class=2, dex_bonus_limit=8, armor_type="robes")
    Armor(name="Master Robe", armor_class=3, dex_bonus_limit=8, armor_type="robes")
    Armor(name="Republic Light Armor", armor_class=2, dex_bonus_limit=4, armor_type="light")
    Armor(name="Federation Fiber Armor", armor_class=3, dex_bonus_limit=4, armor_type="light")
    Armor(name="Federation Protective Armor", armor_class=4, dex_bonus_limit=3, armor_type="medium", strength_required=9)
    Armor(name="Republic Battle Armor", armor_class=5, dex_bonus_limit=3, armor_type="medium", strength_required=10)
    Armor(name="Republic War Armor", armor_class=6, dex_bonus_limit=2, armor_type="medium", strength_required=11)
    Armor(name="Heavy War Armor", armor_class=8, dex_bonus_limit=0, armor_type="heavy", strength_required=14)
    Armor(name="Mandalorian Armor", armor_class=9, dex_bonus_limit=0, armor_type="heavy", strength_required=15)
    Armor(name="Durasteel Weapon Armor", armor_class=10, dex_bonus_limit=0, armor_type="heavy", strength_required=15)


def _make_weapon_csv():
    """Those are made in case of csv files were deleted"""
    Weapon(name='long sword', number_of_dice=1, die_max_value=12, crit_chance=20, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range='sword')
    Weapon(name='short sword', number_of_dice=1, die_max_value=8, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range=1)
    Weapon(name='knuckle-duster', static_damage=1, number_of_dice=0, die_max_value=0, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.bludgeon, weapon_range='melee')
    Weapon(name='rocket gauntlet', static_damage=1, number_of_dice=1, die_max_value=4, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.bludgeon, weapon_range='melee')
    Weapon(name='vibroblade', number_of_dice=1, die_max_value=8, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range='sword')
    Weapon(name='bastard sword', number_of_dice=1, die_max_value=10, crit_chance=20, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range='sword')
    Weapon(name='vibrosword', number_of_dice=1, die_max_value=12, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range='sword')
    Weapon(name='twohanded vibrosword', number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range='sword')
    Weapon(name='vibroaxe', number_of_dice=2, die_max_value=8, crit_chance=20, multiplier_crit=2, damage_type=DamageTypes.slashing, weapon_range='sword')
    Weapon(name='light blaster', number_of_dice=1, die_max_value=8, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.energy, weapon_range='blaster')
    Weapon(name='blaster', number_of_dice=1, die_max_value=10, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.energy, weapon_range='blaster')
    Weapon(name='heavy blaster', number_of_dice=1, die_max_value=12, crit_chance=20, multiplier_crit=2, damage_type=DamageTypes.energy, weapon_range='blaster')
    Weapon(name='energy rifle', number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.energy, weapon_range='rifle')
    Weapon(name='heavy energy rifle', number_of_dice=2, die_max_value=8, crit_chance=20, multiplier_crit=2, damage_type=DamageTypes.energy, weapon_range='rifle')
    Weapon(name='energy crossbow', static_damage=2, number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=2, damage_type=DamageTypes.energy, weapon_range='crossbow')


if __name__ == '__main__':
    """Setting csv to default"""
    _make_weapon_csv()
    _make_armor_csv()
    with open(armor_list_dir, mode='w') as file:
        csv_writer = writer(file, delimiter=';')
        csv_writer.writerow(armor_list_header)
        for armor in ArmorList.armor_dict.values():
            csv_writer.writerow(armor.prepare_to_csv())

    with open(weapon_list_dir, mode='w') as file:
        csv_writer = writer(file, delimiter=';')
        csv_writer.writerow(weapon_list_header)
        for weapon in WeaponList.weapon_dict.values():
            csv_writer.writerow(weapon.prepare_to_csv())


def build_basics():
    build_weapon_list()
    build_classes_list()
    build_units_list()