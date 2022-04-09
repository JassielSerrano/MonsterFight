import random


class Monster:
    def __init__(self, hp = 30, hair_color, age, type):
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

    def attack(self, monster):
        monster.get_attacked(1, 5, self)

    def get_attacked(self, damage, attacker):
        damage = random.randint
        self.hp = self.hp - damage
        print("Monster got attacked...")
        if self.hp <= 0:
            print("This monster has died")
            exit()
        else:
            print(f"New hp is {self.hp}")
            print("arghhh..")
            self.attack()


m1 = Monster(orange, 190, spider)
m1.get_hair_color()
m2 = Monster(blue, 213, slime)
m2.get_hair_color()
m2.get_age()