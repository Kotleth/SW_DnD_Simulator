
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

