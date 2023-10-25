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
    bonus: int

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.bonus = floor((value - 10)/2)

