import Players
import enemies
name = input("Welcome to my game enter your name to begin\n")
playerOne = Players.Players(name,100,0)
playerOne.fixName()

begin = ""

while playerOne.getLevel() <= 9:
  enemy = playerOne.findEnemy()
  enemyObject = enemies.enemies(enemy, playerOne.getEnHealth(enemy))
  while enemyObject.getDefHealth() > 0:
    begin = input("\n" + playerOne.getName() + " type continue when you are ready to continue forward.\n").upper()
    if begin == "CONTINUE":
      
      
      choice = input("\nUh Oh! You have encountered a " + enemy + "! Would you like to attack or sleep?\n")
      if choice == "attack":
        enemyObject.dockHealth(playerOne.attack(playerOne.getLevel()))
        print("\nYou attacked\n" + playerOne.getName() + ": " + str(playerOne.getHealth()) + "\n" + enemy + ": " + str(enemyObject.getDefHealth()))
      elif choice == "sleep":
        playerOne.setHealth(playerOne.sleep())
      if enemyObject.currTurn():
        playerOne.dockPHealth(enemyObject.attack())
        print("\n" + enemyObject.getType() + " chose to attack!\n" + playerOne.getName() + ": " + str(playerOne.getHealth()) + "\n" + enemy + ": " + str(enemyObject.getDefHealth()))
      else:
        enemyObject.setHealth(enemyObject.sleep())
        print("\n" + enemyObject.getType() + " chose to sleep!\n" + playerOne.getName() + ": " + str(playerOne.getHealth()) + "\n" + enemy + ": " + str(enemyObject.getDefHealth()))
  playerOne.levelUp()
