import copy
import unittest
from DnD_Resources.content_builder import *


class TestMain(unittest.TestCase):
    """For now, it's only a one test, but it's simple enough to not split it."""
    def test_building_resources(self):
        build_basics()
        print("Testing lists building...")
        self.assertTrue(any(list(WeaponList.weapon_dict.values())), msg="Weapon list is empty!")
        self.assertTrue(any(list(CharacterClassList.character_classes_dict.values())), msg="Character class list is empty!")
        self.assertTrue(any(list(UnitList.units_dict.values())), msg="Units list is empty!")
        self.assertTrue(any(list(ArmorList.armor_dict.values())), msg="Armor list is empty!")
        print("Testing lists building: DONE")
        print("Testing a unique value protection in lists...")
        Weapon(name='~~dummy sword 3000~~', number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=3,
               damage_type=DamageTypes.slashing, weapon_range='sword')
        with self.assertRaises(Exception):
            Weapon(name='~~dummy sword 3000~~', number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=3,
               damage_type=DamageTypes.slashing, weapon_range='sword')
        print("Testing a unique value protection in weapon list: DONE")
        hero_name = "~~Arnold Schwarzenegger~~"
        hero_strength = 27
        expected_bonus = 8
        hero_unit = Unit(name=hero_name, strength=hero_strength, dexterity=12,
             constitution=14, intelligence=14,
             wisdom=14, charisma=16,
             level=15, character_class=CharacterClassList.undefined_class)
        with self.assertRaises(Exception):
            Unit(name=hero_name, strength=hero_strength, dexterity=12,
                 constitution=14, intelligence=14,
                 wisdom=14, charisma=16,
                 level=15, character_class=CharacterClassList.undefined_class)
        print("Testing a unique value protection in unit list: DONE")
        self.assertEqual(UnitList.units_dict[hero_name].strength.get_bonus(), expected_bonus, 'Wrong strength bonus calculation!')
        Armor(name="~~dummy suite 3000~~", armor_class=1, dex_bonus_limit=8, armor_type="robes")
        with self.assertRaises(Exception):
            Armor(name="~~dummy suite 3000~~", armor_class=1, dex_bonus_limit=8, armor_type="robes")
        print("Testing a unique value protection in armor list: DONE")
        print("Testing a unique value protection in lists: DONE")
        print("Testing an attack method for a unit...")
        villain_unit = copy.copy(hero_unit)
        attack_roll, damage, damage_rolls, participants, crit = UnitList.units_dict[hero_name].attack(villain_unit)
        self.assertTrue(1 <= attack_roll <= 20, msg='Attack roll is out of bonds.')
        self.assertFalse(damage_rolls, msg="There were some damage dice rolled without a weapon!")
        self.assertIs(crit, attack_roll == 20, msg="Critical hit didn't work properly!")
        self.assertEqual((hero_unit.name, villain_unit.name), participants, msg="Wrong participants has been returned from attack!")
        print("Testing an attack method for a unit: DONE")


if __name__ == '__main__':
    unittest.main()
