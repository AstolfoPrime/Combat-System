import random

class Character(object):
    def __init__(self, __name, __max_health, __armor, __max_damage, __hit_chance):
        self.__name = __name
        self.__max_health = __max_health
        self.__armor = __armor
        self.__max_damage = __max_damage
        self.__hit_chance = __hit_chance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def max_health(self):
        return self.__max_health

    @max_health.setter
    def max_health(self, value):
        self.__max_damage = value

    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = value

    @property
    def max_damage(self):
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value):
        self.__max_damage = value
    
    @property
    def hit_chance(self):
        return self.__hit_chance

    @hit_chance.setter
    def hit_chance(self, value):
        self.__hit_chance = value
    
    def print_stats(self):
        print(f"""
        Name: {self.name}
        Health: {self.max_health}
        Armor: {self.armor}
        Damage: {self.max_damage}
        Hit Chance: {self.hit_chance}
        """)

    def hit(self, enemy):
        random_number = random.randint(1, 100)
        if random_number >= self.hit_chance:
            print(f"{self.name} hits {enemy.name}")
            max_damage_number = random.randint(1, self.max_damage)
            if max_damage_number >= self.max_damage:
                max_damage_number - enemy.max_damage
def fight(hero, enemy):
    running = True
    while running:
        hero.hit(enemy)
        hero.print_stats()
        enemy.hit(hero)
        enemy.print_stats()
        input("Continue battle")
        if hero.max_health <= 0:
            print(f"{enemy.name} wins")
            running = False
        else:
            print(f"{hero.name} wins")
            running = False
