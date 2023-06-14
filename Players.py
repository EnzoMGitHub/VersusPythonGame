import random
class Players:
  def __init__(self, name, health, level):
    self.name = name
    self.health = health
    self.level = level

  def __str__(self):
    return "" + self.name + " is a player who has " + self.health + " and is level "  + self.level

  #Mutators
  def fixName(self):
    fixed = ""
    i = 0
    if self.name[0:1] != self.name[0:1].upper():
      for x in self.name:
        if i == 0:
          fixed += self.name[0:1].upper()
        else:
          fixed += self.name[i:i+1]
        i+=1

    self.name = fixed

  def attack(self, level):
    if level == 0:
      damage = random.randint(10, 50)
    else:
      damage = random.randint(level * 10, level * 100)
    
    return damage

  def sleep(self):
    return random.randint(10, 25)

  def setHealth(self, number):
    self.health += number

  def dockPHealth(self, number):
    self.health -= number
  
  def levelUp(self):
    self.level+=1
    print("Congratulations " + self.name + ", you have leveled up!")
  #For Gameplay
  def findEnemy(self):
    enemies = ["Goomba","Koopa","Hammer Bro","Koopa Paratroopa","Boo","Kamek","Bullet Bill","Big Boo","Bowser Jr","Bowser"]
    return enemies[random.randint(0, self.level)]
  # Accessors
  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getHealth(self):
    return self.health

  def getEnHealth(self, enemy):
    enemies = ["Goomba","Koopa","Hammer Bro","Koopa Paratroopa","Boo","Kamek","Bullet Bill","Big Boo","Bowser Jr","Bowser"]
    i = 0
    for x in enemies:
      if enemies[i] == enemy:
        return i * 100 + 100
      i+=1
    return 100
