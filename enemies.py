import random
class enemies:
  def __init__(self, type, health):
    self.type = type
    self.health = health
  #mutators
  def dockHealth(self, amount):
    self.health -= amount
    if self.health < 0:
      self.health = 0
  def setHealth(self, amount):
    self.health += amount
  #non void methods
  def currTurn(self):
    return random.randint(0, 1)

  def attack(self):
    return random.randint(5, 15)

  def sleep(sleep):
    return random.randint(5, 15)
  #accessors
  def getDefHealth(self):
    return self.health

  def getType(self):
    return self.type
