import random

class Characters(object):
    
    def __init__(self, name = "anonmymous", hitpoint = 100, hitchance = 50, maxDamage = 10, armor = 10):
        super().__init__()
        self.name = name
        self.hitpoint = hitpoint
        self.hitchance = hitchance
        self.maxDamage = maxDamage
        self.__armor = armor
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    def sayHi(self):
        print(f"I am {self.name}.")
        print (f"Hitpoints: {self.__hitpoint}")
        print()
    
    @property
    def hitpoint(self):
        return self.__hitpoint
    
    @hitpoint.setter
    def hitpoint(self, value, min = 0, max = 100, default = 100):
        if type(value) == int:
            if value >= min:
                self.__hitpoint = value
            else:
                print("hitpoint must be positive")
                self.__hitpoint = 1
        else:
            print("hitpoint must be a number")
    @property
    def hitchance(self):
        return self.__hitchance
    
    @hitchance.setter
    def hitchance(self, value, min = 0, max = 50, default = 0):
        if type(value) == int:
            if value <= max:
                self.__hitchance = value
            if value > min:
                self.__hitchance = value
            else:
                print("You missed")
                self.__hitchance = min
        else:
            print("hit chance must be a number")
            
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value, min = 0, max = 10, default = 0):
        if type(value) == int: 
            if value > min:
                self.__maxDamage = value
            elif value <= max:
                 print("No Damage")
            else:
                self.__maxDamage = 0
        else:
            print("Damage must be a number")
            
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value, min = 0, max = 10, default = 0):
        if type(value) == int:
            if value <= max:
                self.__armor = value
            elif value >= min:
                self.__armor = value
            else:
                ""
        else:
            print("No damage")
            
            
    def hit(self, opponent):
        if random.randint(1, 100) <= self.hitchance:
            print(f"{self.name} hits {opponent.name}")
            damage = random.randint(1, self.maxDamage) - opponent.armor
            if damage < 0:
                damage = 0
            if opponent.armor > 0:
                print(f"{opponent.name}'s armor absorbs {opponent.armor} points.")
            opponent.hitpoint -= damage
            print(f"{opponent.name} takes {damage} damage. Remaining hitpoints: {opponent.hitpoint}")
        else:
            print(f"{self.name} misses {opponent.name}")
            
            
def basicFight(c1, c2):
    keepGoing = True
    while keepGoing:
        c1.hit(c2)
        if c2.hitpoint <= 0:
            print(f"{c2.name} loses.")
            keepGoing = False
            
        c2.hit(c1)
        if c1.hitpoint <= 0:
            print(f"{c1.name} loses.")
            keepGoing = False
            
        print(f"{c1.name} HP: {c1.hitpoint}")
        print(f"{c2.name} HP: {c2.hitpoint}")
        print()
        
        input("Press <ENTER> for another round")
        
        
def main():
    c1 = Characters("Chairman Fred", 50, hitchance=70, maxDamage=10, armor=5)
    c1.sayHi()
    c2 = Characters("Hoover", 100, hitchance=60, maxDamage=12, armor=0)
    c2.sayHi()
  
    basicFight(c1, c2)
    
if __name__ == "__main__":
    main()