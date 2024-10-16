class Character(object):
    def __init__(self, __name, max_health, armor, damage, hit_chance):
        self.__name = __name
        self.max_health = max_health
        self.armor = armor
        self.damage = damage
        self.hit_chance = hit_chance

    @property
    def name(self):
        return self.__name

    def print_stats(self):
        print(f"""
        Name: {self.name}
        Health: {self.max_health}
        Armor: {self.armor}
        Damage: {self.damage}
        Hit Chance: {self.hit_chance}
        """)