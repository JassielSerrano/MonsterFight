import random


class Monster:
    def __init__(self, hp = 10):
        self.hp = hp

    def attack(self, monster):
        monster.get_attacked(3, self)

    def get_attacked(self, damage, attacker):
        self.hp = self.hp - damage
        print("Monster got attacked...")
        if self.hp <= 0:
            print("This monster has died")
            exit()
        else:
            print(f"New hp is {self.hp}")
            print("argggh..")
            self.attack(attacker)


