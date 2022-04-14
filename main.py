import random
import time


class Monster:
    def __init__(self, hair_color, age, type, hp):
        self.hp = hp
        self.hair_color = hair_color
        self.age = age
        self.type = type

    def get_hair_color(self):
        return self.hair_color

    def get_age(self):
        return self.age

    def get_type(self):
        return self.type

    def get_hp(self):
        return self.hp

    def attack(self, monster):
        damage = random.randint(1, 5)
        monster.get_attacked(damage, self)

    def get_attacked(self, damage, attacker):
        self.hp = self.hp - damage
        print(f"{ attacker.get_hair_color()} hair color monster got attacked...")

        time.sleep(2)
        if self.hp <= 0:
            print("This monster has died")
            exit()
        else:
            print(f"New hp is {self.hp}")
            print("arghhh..")
            self.attack(attacker)

m1 = Monster("Orange", 190, "Spider", 30)
print(f"This {m1.get_type()} hair color is {m1.get_hair_color()} and is {m1.get_age()} years old.")
print(f"Hp of this monster is {m1.get_hp}")
m2 = Monster("Blue", 213, "Slime", 30)
print(f"This {m2.get_type()} hair color is {m2.get_hair_color()} and is {m2.get_age()} years old.")
print(f"Hp of this monster is {m2.get_hp}")
m1.attack(m2)