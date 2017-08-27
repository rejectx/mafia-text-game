import random
#---
#Weapons (name, min_damage, accuracy)
weapon_pistol = ['Pistol',10,80]
weapon_shotgun = ['Shotgun',20,50]
weapon_sniper_rifle = ['Sniper Rifle',50,90]

#---

class Gangster:
    def __init__(self, gangster_name, gangster_weapon=None, gangster_health=None):
        self.name = gangster_name
        if gangster_weapon == None:
            self.weapon = Weapon(*weapon_pistol)
        else:
            self.weapon = Weapon(*gangster_weapon)
        if gangster_health == None:
            self.health = 100
        else:
            self.health = gangster_health

    def lose_health(self, amount):
        self.health -= amount

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, other):
        damage = self.weapon.calculate_damage()
        if self.isAlive():
            if damage == 0:
                print('{}({}) missed his shot against {}({})'.format(self.name, self.health, other.name, other.health))
            else:
                other.lose_health(damage)
                print('{}({}) did {} damage with {} to {}({})'.format(self.name, self.health, damage, self.weapon.name, other.name, other.health))

class Weapon:
    def __init__(self, weapon_name, weapon_damage,weapon_accuracy):
        self.name = weapon_name
        self.damage = weapon_damage
        self.accuracy = weapon_accuracy
    def calculate_damage(self):
        if self.accuracy >= random.randint(0,100):
            damage = self.damage + random.randint(0,round(self.damage/2))
            return int(damage)
        else:
            return 0

g1 = Gangster('tomas')
g2 = Gangster('lukas')
turns = 0

while g1.isAlive() and g2.isAlive():
    turns += 1
    print('--- {} ---'.format(turns))
    g1.attack(g2)
    g2.attack(g1)
