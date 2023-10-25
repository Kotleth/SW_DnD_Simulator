from math import floor


damage_types = [
                "Acid",
                "Bludgeon",
                "Cold",
                "Electrical",
                "Energy",
                "Fire",
                "Ion",
                "Necrotic",
                "Piercing",
                "Poison",
                "Psychic",
                "Radiation",
                "Slashing",
                "Sound",
                ]


class DamageInstance:
    damage_dict: dict

    def __init__(self, damage_dict):
        self.damage_dict = damage_dict

    def full_damage(self):
        damage_dealt = 0
        for damage in self.damage_dict.values():
            damage_dealt += damage
        return damage_dealt


class Attribute:
    name: str
    value: int

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_bonus(self):
        return floor((self.value - 10)/2)


class CharacterClass:
    name: str
    vitality_dice: int

    def __init__(self, name, vitality_dice):
        self.name = name
        self.vitality_dice = vitality_dice

    def show_status(self):
        print(f"{self.name.upper()}\nVitality die: k{self.vitality_dice}")


class CharacterClassList:
    characters_dict: dict[str, CharacterClass] = {}
    undefined_class = CharacterClass('undefined', 10)

    @classmethod
    def get_classes_list(cls):
        print(f"{'*' * 10}\n")
        for character in cls.characters_dict.values():
            character.show_status()
        print(f"{'*' * 10}")
