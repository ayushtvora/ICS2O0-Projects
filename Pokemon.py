import random    # Imports Random functions


# Definitions:
def select(p):    # Defines what move the Player or the AI will use
    if p == pUser:    # If the person using this function is a player, do the following
        print("Moves:")    # Ask them to do one of the following moves
        print("1. Special Attack: %s" % pSpAttack[p])
        print("2. Physical Attack: %s" % pPhAttack[p])
        print("3. Normal Attack: %s" % pNmAttack[p])
        print("4. Status Attack: %s" % pStAttack[p])
        pM = int(input("Select which move you would like to do (1-4): "))    # Ask which move you want them to do
        return pM - 1    # Tell the main code what move the player has chosen
    else:
        pM = random.randint(1, 4)    # If the AI is using this, choose a random move to attack with
        return pM - 1    # Tell the main code what move the AI has chosen


def attack(p, o):
    if move == 0:    # If the player chose a special attack
        damage = random.randint(spMin, spMax)    # Choose damage dealt between 10 and 50
        if (pType[p] == "FIRE" and pType[o] == "GRASS") or (pType[p] == "GRASS" and pType[o] == "WATER") or (pType[p] == "WATER" and pType[o] == "FIRE"):    # If they have a type advantage...
            damage *= 2    # Multiply the damage by 2
            print("%s used %s, and dealt %i Damage. ITS SUPER EFFECTIVE!" % (pName[p], pSpAttack[p], int(damage)))    # Print what move the player used, how much damage it dealt, and that the move is super effecctive
            print()
            return int(damage)
        elif (pType[p] == "GRASS" and pType[o] == "FIRE") or (pType[p] == "WATER" and pType[o] == "GRASS") or (pType[p] == "FIRE" and pType[o] == "WATER"):    # If they have a type advantage
            damage /= 2    # Divide the damage in half
            print("%s used %s, and dealt %i Damage. It's not very effective." % (pName[p], pSpAttack[p], int(damage)))    # Print what move the player used, how much damage it dealt, and that the move is not very effective
            print()
            return int(damage)
        else:
            print("%s used %s, and dealt %i Damage." % (pName[p], pSpAttack[p], damage))    # Print what move the player usedand how much damage it dealt.
            print()
            return int(damage)
    elif move == 1:    # Nearly the same thing, but with different numbers
        damage = random.randint(phMin, phMax)
        if (pType[p] == "FIRE" and pType[o] == "GRASS") or (pType[p] == "GRASS" and pType[o] == "WATER") or (pType[p] == "WATER" and pType[o] == "FIRE"):
            damage *= 2
            print("%s used %s, and dealt %i Damage. ITS SUPER EFFECTIVE!" % (pName[p], pPhAttack[p], int(damage)))
            print()
            return int(damage)
        elif (pType[p] == "GRASS" and pType[o] == "FIRE") or (pType[p] == "WATER" and pType[o] == "GRASS") or (pType[p] == "FIRE" and pType[o] == "WATER"):
            damage /= 2
            print("%s used %s, and dealt %i Damage. It's not very effective." % (pName[p], pPhAttack[p], int(damage)))
            print()
            return int(damage)
        else:
            print("%s used %s, and dealt %i Damage." % (pName[p], pPhAttack[p], int(damage)))
            print()
            return int(damage)
    elif move == 2:    # Same thing as above but without type advantages.
        damage = nm
        print("%s used %s, and dealt %i Damage." % (pName[p], pNmAttack[p], int(damage)))
        print()
        return int(damage)


def heal(p):    # If the opponent decides to heal...
    h = random.randint(hMin, hMax)    # Randomly choose how much the player should heal
    print("%s used %s, and healed %i HP." % (pName[p], pStAttack[p], h))
    return h


# Define everything about each Pokemon
pType =     ["FIRE",         "WATER",      "GRASS"]
pName =     ["CHARIZARD",    "BLASTOISE",  "VENUSAUR"]
pSpAttack = ["FLAMETHROWER", "HYDRO PUMP", "SOLAR BEAM"]
pPhAttack = ["FIRE BLITZ",   "AQUA JET",   "RAZOR LEAF"]
pNmAttack = ["SLASH",        "SKULL BASH", "DOUBLE-EDGE"]
pStAttack = ["DRAGON RAGE",  "PROTECT",    "GROWTH"]

# Define the starting HP for each player
userHp = 100
aiHp = 100

# Define the Minimum and Maximum damage each move can do (Allows for easier game balancing)
spMin = 10
spMax = 50
phMin = 25
phMax = 35
nm = 35
hMin = 0
hMax = 50

print("WELCOME TO PYTHON POKEMON BATTLES")    # Welcome message
print()
if input("Do you want to see the list of Pokemon, and their Moves? This is recommended for the first time. (y/n): ") == "y":    # Ask if they want to see the different moves
    for i in range(0, len(pType)):    # This loop prints out all the Pokemon options with the different moves they have
        print("Pokedex #%i: %s type: %s" % (i, pType[i], pName[i]))
        print("  Special Attack: %s" % pSpAttack[i])
        print("  Physical Attack: %s" % pPhAttack[i])
        print("  Normal Attack: %s" % pNmAttack[i])
        print("  Status Attack: %s" % pStAttack[i])
        print()

pUser = int(input("Please enter the Pokedex number of the Pokemon you want to use (0-2): "))    # Ask the player which Pokemon they want to use
pAi = random.randint(0, 2)    # Randomly pick what Pokemon the AI will use
print()

# Prints the names of the characters, officially starting the battle
print("You: I choose you, %s!" % pName[pUser])
print("Enemy: I choose you, %s!" % pName[pAi])
print()

if input("Do you want to read the rules? (y/n): ") == "y":    # Ask to state the rules of the game
    print("- Each Pokemon starts off with %i HP" % userHp)
    print("- Special Attacks deal between %i and %i HP" % (spMin, spMax))
    print("- Each Physical Attack will deal between %i and %i HP" % (phMin, phMax))
    print("- Each Normal Attack will deal %i damage" % nm)
    print("- Status Attacks will heal the user between %i - %i health" % (hMin, hMax))
    print("- Special and Physical attacks can be affected with type advantages and disadvantages")
    print("  - Water is stronger than Fire, Fire is stronger than Grass, and Grass is stronger than Fire")
    print("- First one to get the opponent down to 0 health is the winner")
    print()

turnPicker = random.randint(0, 1)    # Since the "speed" element of the original game is not in this, I created a randomizer to choose who goes first.
while userHp > 0 and aiHp > 0:    # While both are still alive...
    if turnPicker == 0:    # If the randomizer chooses 0, the User will go first
        move = select(pUser)    # Tell the User to choose their move
        if move in range(0, 3):    # If they chose an attack move...
            aiHp -= attack(pUser, pAi)    # Take out the amount of health from the AI's HP that you dealt
            if aiHp <= 0:
                print("%s has %i HP Left. %s has %i HP Left" % (pName[pUser], userHp, pName[pAi], 0))  # After both characters have gone, state how much health each user has
                print("CONGRATULATIONS!!! YOU WON!!!")
                quit()
        else:    # If they did not attack, they chose to heal, so the else is a substitute for "elif move == 3:"
            userHp += heal(pUser)    # Heal the User for the amount they decided to heal
        move = select(pAi)    # Now its the AI's turn to go. The rest of this until the outer else is the same as above, but the players are switched
        if move in range(0, 3):
            userHp -= attack(pAi, pUser)
            if userHp <= 0:
                print("%s has %i HP Left. %s has %i HP Left" % (pName[pUser], 0, pName[pAi], aiHp))
                print("You lost! Try again next time!")
                quit()  # End the program
        else:
            aiHp += heal(pAi)
    else:    # If the randomizer chooses 1, the AI will go first. The rest of this else statement is the same as above, except the AI will go before the User
        move = select(pAi)
        if move in range(0, 3):
            userHp -= attack(pAi, pUser)
            if userHp <= 0:
                print("%s has %i HP Left. %s has %i HP Left" % (pName[pUser], 0, pName[pAi], aiHp))
                print("You lost! Try again next time!")
                quit()
        else:
            aiHp += heal(pAi)
        move = select(pUser)
        if move in range(0, 3):
            aiHp -= attack(pUser, pAi)
            if aiHp <= 0:
                print("%s has %i HP Left. %s has %i HP Left" % (pName[pUser], userHp, pName[pAi], 0))
                print("CONGRATULATIONS!!! YOU WON!!!")
                quit()
        else:
            userHp += heal(pUser)
    print("%s has %i HP Left. %s has %i HP Left" % (pName[pUser], userHp, pName[pAi], aiHp))
