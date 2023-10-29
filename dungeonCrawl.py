import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999
playerHealth = 10
maxHealth = 10
playerAccuracy = 6
playerDamage = 1
maxEnemyHealth = 2
enemyHealth = 2
enemyAccuracy = 5
enemyDamage = enemyHealth - 1


# Functions to represent dungeon rooms
# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def diversion():
    direction = input("[n] [s]?: ")
    while direction != "n" and direction != "s":
        print("Invalid input...")
        direction = input("[n] [s]?: ")
    
    roomChoice = -1
    if direction == "n":
        roomChoice = FINAL_ROOM
    elif direction == "s":
        roomChoice = 1

    return roomChoice

def direction():
    roomChoice = -1        # HINT: Once this section is encapsulated into a function, it would be wise to have a default roomChoice value outside that function.
    direction = input("[n] [s] [e] [w] [ne] [sw]?: ")
    while direction != "n" and direction != "s" and direction != "e" and direction != "w" and direction != "ne" and direction != "sw":
        print("Invalid input...")
        direction = input("[n] [s] [e] [w] [ne] [sw]?: ") 

    if direction == "n":
        roomChoice = 2
    elif direction == "s":
        roomChoice = 1
    elif direction == "e":
        roomChoice = 3
    elif direction == "w":
        roomChoice = 4
    elif direction == "ne":
        roomChoice = 5
    elif direction == "sw":
        roomChoice = 6

    
    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice

def combat(combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage,roomChoice):
    enemyName = ""
    enemyHealth = 0
    enemyAccuracy = 0
    enemyDamage = 0
    # Check to see if we should engage in combat
    if combatChance > random.randint(0, 9):
        print("You have engaged in combat!")
        print()

        # Randomly select an enemy
        monsterSelection = random.randint(0, 0)
        if monsterSelection == 0: # SLIME monster
            enemyName = "SLIME"
            maxEnemyHealth = 2
            enemyHealth = maxEnemyHealth
            enemyAccuracy = 5
            enemyDamage = 1
            print("You have encountered an enemy {0} monster...".format(enemyName))
            print()
            print("It has {0} HP and {1} ATTACK strength...".format(enemyHealth, enemyDamage))
            print()
        else:
            print("Error - 'combat' function: 'monsterSelection' value is invalid:", monsterSelection)

        # Choose a random turn to go first
        currentTurn = random.randint(0, 1)
        if currentTurn == 0:
            print("You have taken the initiative!")
        else:
            print("The enemy {0} monster has struck first!".format(enemyName))
        print()

        # Take turns
        while playerHealth > 0 and enemyHealth > 0:
            if currentTurn == 0: # Human Turn
                # Get the action the human wants to take
                action = input("COMBAT: [a]ttack, [f]lee: ")
                while action != "a" and action != "f":
                    print("Invalid combat choice...")
                    action = input("COMBAT: [a]ttack, [f]lee: ")
                print()

                # Engage in combat depending on the action
                if action == "a":
                    if random.randint(0, 9) < playerAccuracy:
                        enemyHealth -= playerDamage
                        print("You have HIT the enemy monster! Its HP is: {0} / {1}".format(enemyHealth, maxEnemyHealth))
                        print()
                    else:
                        print("You have MISSED the enemy monster...")
                        print()
                elif action == "f":
                    #if random.randint(0, 9) < playerDamage:
                        print("You have escaped from combat!")
                        print()
                        roomChoice = diversion() # FINAL_ROOM
                        break
                else:
                    print("Error - 'combat' function: 'action' value is invalid:", action)

            else: # Computer Turn 
                if random.randint(0, 9) < enemyAccuracy:
                    playerHealth -= enemyDamage
                    print("You have been HIT by the the enemy {0} monster! Your HP is: {1} / {2}".format(enemyName, playerHealth, maxHealth))
                    print()
                else:
                    print("The enemy {0} monster has MISSED you...".format(enemyName))
                    print()
            # switch turns
            currentTurn += 1
            currentTurn %= 2
        
        # Announce the winner
        if playerHealth > 0 and enemyHealth <= 0:
            print("Congratulations! You have defeated the enemy {0} monster...".format(enemyName))
            print()
        elif playerHealth > 0 and enemyHealth > 0:
            print("That was a close one! The enemy {0} monster almost got you!".format(enemyName))
            print()
        else:
            print("Sadly, the enemy {0} monster was victorious...".format(enemyName))
            print()
    else:
        print("Fortunately, there were no monsters in this room...")
        print()
    
                        
    return roomChoice,playerHealth

def magicalshop(goldAmount):
    global playerHealth
    if goldAmount > 15 and playerHealth != maxHealth:
        print("You have encountered with a magical shop ! You have ",playerHealth, " /",maxHealth ,". Will you pay 15/",goldAmount," gold to restore your health and heal the wounds ? :")
        schoice = input("[y]es  [n]o : ") 
        while schoice != "y" and schoice != "n":
            print("Invalid input...")
            schoice = input("[y]es [n]o ?: ")

        if schoice == "y":
            playerHealth = maxHealth
            goldAmount = goldAmount - 15 
            print("You have healed yourself! You currently have", playerHealth, "/",maxHealth ,"HP, and", goldAmount, " gold.")
        elif schoice == "n":
            print("Please proceed to the next room")

    else:
        goldAmount = goldAmount
        print("Please proceed ahead to the next dungeon room.")
    return goldAmount

def story(roomChoice):
    if roomChoice == 1:
        print("This room does not have a combat anymore. Move ahead to the next room")
    elif roomChoice == 2:
        print("You are lucky enough. You have reached this room safely once again.")
    elif roomChoice == 3:
        print("Proceed to the next room. You have alreay won in this room")
    elif roomChoice == 4:
        print("This room is safe. Go Ahead and try to escape from the Dungeon to win the complete Game")
    elif roomChoice == 5:
        print("Once upon a time, there lived a stronger and powerful MONSTER in this room. But now onwards, we understand that YOU are the most powerful Monster in this planet as you have already deferated this MONSTER. Try to escape from this Dungeon as there are much more Stronger MONSTERS in the dungeon for you to defeat.")
    else:
        print("This room not having a combat. Go ahead and collect the Gold, Try to escape from the dungeon rooms, otherwise your dead")


def room1(goldAmount, visited_room):
    global playerHealth
    global playerDamage
    global maxHealth
    global playerAccuracy

    roomChoice = 1

    # TODO: In at least two of your rooms, make up a fun story for the player to read. Create a 'story' function which contains
    # text that you will print out, depending on which room the player enters. (1 pt.)
    #
    # HINT: The 'story' should probably only print out when the player has never visited to room before.

    # TODO: Create a function which implements a simple combat system for the game where the player fights monsters. Players and
    # monsters should take turns against one another. Not every room has to have combat in it. (1 pt.)

    # HINT: You can accomplish this any way you want - use your imagination. However, it will have to print out/ take input for
    # whatever you want to have happen.
    #
    # HINT: You should at least have 'player total health'/ 'player current health'/ 'player damage' variables initially created 
    # in the 'main()' function. You can pass these into the room functions, and then into the combat function.
    #
    # HINT: Whatever stats for whatever monsters you want to implement should likely exist inside the 'combat' function.
    #
    # HINT: Your combat function can, itself, call other sub-functions as well.

    # TODO: Create a function which implements a simple 'shop' for the player to pay some amount of gold to restore their health.
    # Not every room has to have a shop. (1 pt.)
    #
    # HINT: You can accomplish this any way you want - use your imagination. However, it will have to print out/ take input for
    # whatever you want to have happen.
    #
    # HINT: Perhaps players can also pay gold to upgrade their maximum possible health or their attack power.
    #
    # HINT: Whatever stats for shopping you want to implement should likelyh exist inside the 'shop' function.
    #
    # HINT: Your 'shop' function can, itself, call other sub-functions as well.

    # TODO: Create a function which accepts parameters representing the player's 'goldAmount' value, a 'gold' value representing 
    # the amount of gold that the room contains, and a boolean flag indicating whether the room has been visited or not. 
    #
    # This function will operate in a manner similar to the code below, and should return the new 'goldAmount' value that the 
    # player has after adding the gold from the room to their total 'goldAmount'. It should also mark the 'room visited' boolean 
    # flag as 'True', and return that value as well. When returning, assign the new amount of gold to the 'goldAmount' variable, and
    # assign the 'room visited' return value to the 'visited_room' variable. If the room has already been visited before, print
    # out a string indicating this. 
    #
    # This function should be used in all subsequent room functions. (1 pt.)
    #
    # HINT: If the player's health is less than zero, they shouldn't be able to visit rooms anymore.
    #
    # HINT: Study how the 'visited_room' variable is returned at the bottom of this function, and how it interacts with the 
    # 'visited_roomX' variables in the main() function.
    if visited_room == False:
        gold = 10 # This is the amount of gold the room contains.
    
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()
        roomChoice, playerHealth = combat(10, playerHealth, maxHealth, playerAccuracy, playerDamage,roomChoice)

        # Mark the room as 'visited'
        visited_room = True
        
    else:
        print()
        print("You have already visited this room before...")
        story(roomChoice)
        print()

    # TODO: Create a function which takes in input for the directions the player can go in the dungeon.
    # This function will control how the player moves around the dungeon.
    # This function should replace the following code below this TODO and before the 'return' statement.
    # This function should be used in all subsequent room functions. 
    # This function should return a valid 'roomChoice' value. (1 pt.)
    #
    # HINT: You can do this any way you want. However, it might be an easy solution to take in arguments that 
    # specify valid directions for the player to move, and which rooms they can move to.
    # For example, arguments for N, S, E, W => 2, -1, 3, -1 might allow the player to move north to room 2, 
    # and east to room 3. The values of -1 indicate that the player cannot move that direction.
    #
    # HINT: If you want to give the player fewer than four directions to go, how would you accomplish this in the command print-out? 
    # There are multiple ways to go about this. You don't have to print all the commands on one line. Perhaps you could print out 
    # each command on a different line, and then have the final prompt for the 'input' function just read "What is our choice?: " 
    # or something like that.
    #
    # HINT: If the player's health is less than zero, they shouldn't be able to move to different rooms anymore
    
    #combat(10, maxHealth, playerAccuracy, playerDamage)
    
    if playerHealth > 0 and roomChoice != FINAL_ROOM :
        roomChoice = direction()
    
    return roomChoice, goldAmount, visited_room


# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def room2(goldAmount, visited_room):
    print("You have moved deeper into the dungeon... You sense this is a central crossroads of the dungeon! ")
    print("Fortunately, there were no monsters in this room...")

    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        #gold = 20 # This is the amount of gold the room contains.

        print()
   #print("The room has", gold, "gold pieces in it...")
        # goldAmount += gold
        print("You currently have ", goldAmount, " gold pieces in your posession...")
        print()
        goldAmount = magicalshop(goldAmount)

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        story(2)
        print()
  

    roomChoice = direction()
    return roomChoice, goldAmount, visited_room


def room3(goldAmount, visited_room):
    global playerHealth
    global playerDamage
    global maxHealth
    global playerAccuracy

    roomChoice = 3


    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold =  30 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()
        roomChoice, playerHealth = combat(10, playerHealth, maxHealth, playerAccuracy, playerDamage,roomChoice)


        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        story(roomChoice)
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    if playerHealth > 0 and roomChoice != FINAL_ROOM:
        roomChoice = direction()
    
    return roomChoice, goldAmount, visited_room   
    

def room4(goldAmount, visited_room):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 40 # This is the amount of gold the room contains.

        print()
        print("The room has ", gold, " gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have ", goldAmount, " gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        story(4)
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    roomChoice = direction()

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return roomChoice, goldAmount, visited_room


def room5(goldAmount, visited_room):
    global playerHealth
    global playerDamage
    global maxHealth
    global playerAccuracy

    roomChoice = 5

    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 50 # This is the amount of gold the room contains.

        print()
        print("The room has ", gold, " gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have ", goldAmount, " gold pieces in your posession...")
        print()
        roomChoice, playerHealth = combat(10, playerHealth, maxHealth, playerAccuracy, playerDamage,roomChoice)


        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        story(roomChoice)
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    if playerHealth > 0 and roomChoice != FINAL_ROOM : 
        roomChoice = direction()
    
    return roomChoice, goldAmount, visited_room

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.



def room6(goldAmount, visited_room):
    print("You have moved deeper into the dungeon... You sense this is a central crossroads of the dungeon! ")
    print("Fortunately, there were no monsters in this room...")

    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        #gold = 60 # This is the amount of gold the room contains.

        print()
   # print("The room has", gold, "gold pieces in it...")
        # goldAmount += gold
        print("You currently have ", goldAmount, " gold pieces in your posession...")
        print()
        goldAmount = magicalshop(goldAmount)

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        story(6)
        print()
   

    roomChoice = direction()
    return roomChoice, goldAmount, visited_room

# Main function
def main():
    # Set to 'True' when the game is over.
    gameOver = False

    # Player status variables/ constants. 
    # HINT: If you have other player variables to use, such as health, damage, etc. add them here.
    START_GOLD = 0 # HINT: This is a 'constant' value. Notice how it is used to set/ reset the goldAmount value.
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    playerHealth = 10
    maxHealth = 10
    playerAccuracy = 6
    playerDamage = 0


    print("Welcome to Dungeon Crawl...")
    print()

    
    #print("By: <Subrahmanya Sree Pranava Sai Maganti>")
    #print("[COM S 127 <section F & Lab Section 1>]")
    #print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
            visited_room1 = False # HINT: Carefully study how these 'visited room' variables are used.
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
            visited_room6 = False
            visited_allrooms = False

            # TODO: Add at least four (4) additional rooms to the dungeon - creating a new 'room' function for each of them (1 pt.)
            #
            # HINT: This will require planning out the layout of your dungeon so that all the 'rooms' connect together correctly.
            #
            # HINT: Study this code carefully to see how the rooms connect, and which room the player is currently inside.
            #
            # NOTE: The other TODO tasks for this assignment can be found in the 'room1' function above.
            
            currentRoom = direction()
            while currentRoom != FINAL_ROOM: # HINT: When implmenting combat, if the player's health is <= 0, this loop should not execute.
                if currentRoom == 1:
                    currentRoom, goldAmount, visited_room1 = room1(goldAmount, visited_room1)
                elif currentRoom == 2:
                    currentRoom, goldAmount, visited_room2 = room2(goldAmount, visited_room2)
                elif currentRoom == 3:
                    currentRoom, goldAmount, visited_room3 = room3(goldAmount, visited_room3)
                elif currentRoom == 4:
                    currentRoom, goldAmount, visited_room4 = room4(goldAmount, visited_room4)
                elif currentRoom == 5:
                    currentRoom, goldAmount, visited_room5 = room5(goldAmount, visited_room5)
                elif currentRoom == 6:
                    currentRoom, goldAmount, visited_room6 = room6(goldAmount, visited_room6)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
                if visited_room1 == True and visited_room2 == True and visited_room3 == True and visited_room4 == True and visited_room5 == True and visited_room6 == True:
                    visited_allrooms = True
                    break
            # HINT: If the player's health is > 0 when they escape the dungeon print a message like this one. 
            # Otherwise print a message stating that they perished in the dungeon.
            print()
            if visited_allrooms == True:
                print("You have visited all the rooms. Congratulations. Game Over !!! ")
            elif playerHealth > 0 :
                print("You have escaped with ", goldAmount, " gold from the dungeon!")
            else:
                print("The player has perished in the dungeon. Better luck next time.")
            print()

            # Reset player values back to their original state
            # HINT: If you add other player values, you will have to reset them to their original values to restart the game.
            #
            # HINT: You can create 'constants' that you can assign to these variables. Doing so means you will only need to 
            # change the values you want to use in one place if you wish to change them.
            # goldAmount = START_GOLD
            # currentRoom = START_ROOM
            # visited_room1 = False
            # visited_room2 = False
        elif choice == "i": # (**"i" Section Tasks**)
            print("Traverse the dangerous dungeon and collect all the gold....")
        elif choice == "q": # (**"q" Section Tasks**)
            print("Goodbye!")
            break
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()
