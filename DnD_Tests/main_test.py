import unittest
from DnD_Resources.content_builder import *


class TestMain(unittest.TestCase):
    """For now, it's only a one test, but it's simple enough to not split it."""
    def test_building_resources(self):
        build_basics()
        self.assertTrue(any(list(WeaponList.weapon_dict.values())), msg="Weapon list is empty!")
        self.assertTrue(any(list(CharacterClassList.character_classes_dict.values())), msg="Character class list is empty!")
        self.assertTrue(any(list(UnitList.units_dict.values())), msg="Units list is empty!")

        Weapon(name='~~dummy sword 3000~~', number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=3,
               damage_type=DamageTypes.slashing, weapon_range='sword')
        with self.assertRaises(Exception):
            Weapon(name='~~dummy sword 3000~~', number_of_dice=2, die_max_value=6, crit_chance=19, multiplier_crit=3,
               damage_type=DamageTypes.slashing, weapon_range='sword')
        the_hero = "~~Arnold Schwarzenegger~~"
        hero_strength = 27
        expected_bonus = 8
        Unit(name=the_hero, strength=hero_strength, dexterity=12,
             constitution=14, intelligence=14,
             wisdom=14, charisma=16,
             level=15, character_class=CharacterClassList.undefined_class)
        with self.assertRaises(Exception):
            Unit(name=the_hero, strength=hero_strength, dexterity=12,
                 constitution=14, intelligence=14,
                 wisdom=14, charisma=16,
                 level=15, character_class=CharacterClassList.undefined_class)
        self.assertEqual(UnitList.units_dict[the_hero].strength.get_bonus(), expected_bonus, 'Wrong strength bonus calculation!')
        Armor(name="~~dummy suite 3000~~", armor_class=1, dex_bonus_limit=8, armor_type="robes")
        with self.assertRaises(Exception):
            Armor(name="~~dummy suite 3000~~", armor_class=1, dex_bonus_limit=8, armor_type="robes")


if __name__ == '__main__':
    unittest.main()
