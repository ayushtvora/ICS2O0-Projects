import random

# Welcome message
print("\033[1;36;0mWelcome to Blackjack Python, created by Ayush Vora.")

# Rules (optional)
if input("\033[0;0;0mWould you like to read the rules? (y/n): ") == "y":
    print("- The Goal of the game is to get closer to 21 than the dealer, without going over 21.")
    print("- Firstly, you and the dealer will draw a card. Then, you will both draw a card again,")
    print("  but the dealers second")
    print("  card will remain hidden.")
    print("- For the first 2 cards, Ace is worth 11, and face cards (J, Q, K) are worth 10. Number cards are worth 21.")
    print("- If the first 2 cards you draw are an Ace and a face card, you get a blackjack and automatically win.")
    print("- If not, you have the option to “stand” or to “hit”. If you stand, you are keeping your current")
    print("  value the same.")
    print("- If you hit, you are drawing a card in an attempt to higher ur total card value. Watch out, because if you")
    print("  draw a card and your total goes above 21, you lose")
    print("- During the hitting phase for both people, Aces are worth 1")
    print("- Once you are satisfied with your total, you can stand, and then the dealer will draw cards")
    print("- First, the dealer will open his other card. If he gets a blackjack, he wins, and you lose.")
    print("- If he has a total of less than 17, the dealer must hit. Otherwise, he must stand.")
    print("- If the dealer goes over 21, he loses, and you will win")
    print("- Once both people stand, whoever has the higher total wins. If both people have the same total,")
    print("  the game is a tie.")

print("---------------------------------------------------------------------------------------------------------------")
print()

print()

# Initialize the variables for the sum of all the cards
playerTotal = 0
dealerTotal = 0

# Dealer and player draw a card
playerCard1 = random.randint(2, 14)
dealerCard1 = random.randint(2, 14)

# If the player/dealer draws a face card (11-13), give it the value of 10. If it is an Ace (14), give it the
# value of 11
if playerCard1 in range(11, 14):
    playerCard1Value = 10
elif playerCard1 == 14:
    playerCard1Value = 11
else:
    playerCard1Value = playerCard1

if dealerCard1 in range(11, 14):
    dealerCard1Value = 10
elif dealerCard1 == 14:
    dealerCard1Value = 11
else:
    dealerCard1Value = playerCard1

# Create a string value to to the cards so printing is more user-friendly
if playerCard1 == 11:
    playerCard1 = "J (10)"
elif playerCard1 == 12:
    playerCard1 = "Q (10)"
elif playerCard1 == 13:
    playerCard1 = "K (10)"
elif playerCard1 == 14:
    playerCard1 = "A (11)"

if dealerCard1 == 11:
    dealerCard1 = "J (10)"
elif dealerCard1 == 12:
    dealerCard1 = "Q (10)"
elif dealerCard1 == 13:
    dealerCard1 = "K (10)"
elif dealerCard1 == 14:
    dealerCard1 = "A (11)"

# Add the value of the cards the player and dealer drew and add them to their respective "Total" variable
playerTotal += playerCard1Value
dealerTotal += dealerCard1Value

# Repeat the card-drawing process for a second card
playerCard2 = random.randint(2, 14)
dealerCard2 = random.randint(2, 14)

# If the player/dealer draws a face card (11-13), give it the value of 10. If it is an Ace (14), give it the
# value of 11
if playerCard2 in range(11, 14):
    playerCard2Value = 10
elif playerCard2 == 14:
    playerCard2Value = 11
else:
    playerCard2Value = playerCard2
if dealerCard2 in range(11, 14):
    dealerCard2Value = 10
elif dealerCard2 == 14:
    dealerCard2Value = 11
else:
    dealerCard2Value = dealerCard2

# Create a string value to to the cards so printing is more user-friendly
if playerCard2 == 11:
    playerCard2 = "J (10)"
elif playerCard2 == 12:
    playerCard2 = "Q (10)"
elif playerCard2 == 13:
    playerCard2 = "K (10)"
elif playerCard2 == 14:
    playerCard2 = "A (11)"
if dealerCard2 == 11:
    dealerCard2 = "J (10)"
elif dealerCard2 == 12:
    dealerCard2 = "Q (10)"
elif dealerCard2 == 13:
    dealerCard2 = "K (10)"
elif dealerCard2 == 14:
    dealerCard2 = "A (11)"

# Add ONLY THE PLAYER'S card value. The dealer's card should be hidden at this point.
playerTotal += playerCard2Value

# Print the cards drawn, and let them know if they got a blackjack. In this version, if they get a blackjack,
# they win. If they did not get a blackjack, the have the option to stand or hit.
print("Card 1: You drew a %s. The dealer drew a %s." % (str(playerCard1), str(dealerCard1)))
print("Card 2: You drew a %s. The dealer's second card is still face down." % str(playerCard2))
print()
if playerTotal == 21:
    print("You got a Blackjack, and won!")
    quit()
print("Your total is %i. Would you like to stand (do nothing) or hit (draw another card)?" % playerTotal)
choice = input("Type 's' to stand, and 'h' to hit: ")

# If the player hits...
while choice == "h":

    # Start the card-drawing process, but in a loop. After the first 2 cards, if the player draws an Ace, the Ace is
    # worth 1.
    playerCardLoop = random.randint(2, 14)
    if playerCardLoop in range(11, 14):
        playerCardLoopValue = 10
    elif playerCardLoop == 14:
        playerCardLoopValue = 1
    else:
        playerCardLoopValue = playerCardLoop

    # Create a string value to to the cards so printing is more user-friendly
    if playerCardLoop == 11:
        playerCardLoop = "J (10)"
    elif playerCardLoop == 12:
        playerCardLoop = "Q (10)"
    elif playerCardLoop == 13:
        playerCardLoop = "K (10)"
    elif playerCardLoop == 14:
        playerCardLoop = "A (1)"

    # Add the player's card value to the 'Total' variable.
    playerTotal += playerCardLoopValue

    # Let the player know what card they drew, and if they bust. If they bust, end the game.
    print()
    print("You drew a %s." % str(playerCardLoop))
    if playerTotal > 21:
        print("You Busted (total was %i)! Please try again." % playerTotal)
        quit()

    # Ask them if they want to continue to stand or hit. If they choose hit, the loop will continue.
    print("Your total is %i. Would you like to stand (do nothing) or hit (draw another card)?" % playerTotal)
    choice = input("Type 's' to stand, and 'h' to hit: ")

# The Dealer will now open their card. If dealer and player got a blackjack, the game is a tie. If only the dealer
# gets a blackjack, the dealer wins.
dealerTotal += dealerCard2Value
print()
print("The Dealer opened his card, and opened a %s" % str(dealerCard2))
print("The Dealer has a total of %i. Remember, your total is %i" % (dealerTotal, playerTotal))
if dealerTotal == 21:
    print()
    print("The dealer has a Blackjack, and won! :( Better luck next time.")
    quit()

# If the deal was less than 17...
while dealerTotal < 17:

    # The dealer draws a new card. After the first 2 cards, if the dealer draws an Ace, the Ace is worth 1.
    dealerCardLoop = random.randint(2, 14)
    if dealerCardLoop in range(11, 14):
        dealerCardLoopValue = 10
    elif dealerCardLoop == 14:
        dealerCardLoopValue = 1
    else:
        dealerCardLoopValue = dealerCardLoop

    # Create a string value to to the cards so printing is more user-friendly
    if dealerCardLoop == 11:
        dealerCardLoop = "J (10)"
    elif dealerCardLoop == 12:
        dealerCardLoop = "Q (10)"
    elif dealerCardLoop == 13:
        dealerCardLoop = "K (10)"
    elif dealerCardLoop == 14:
        dealerCardLoop = "A (1)"

    # Add the dealer's card value to the 'Total' variable
    dealerTotal += dealerCardLoopValue

    # Print the value of what the dealer draws
    print()
    print("The Dealer drew a card, and opened a %s" % str(dealerCardLoop))
    print("The Dealer has a total of %i. Remember, your total is %i" % (dealerTotal, playerTotal))

# Ending the Dealer's card draws, and display their total, along with a remind of your total
print()
print("The Dealer has to Stand. His total was %i" % dealerTotal)
print("Your total was %i" % playerTotal)

# If the dealer went over 21 in an attempt to reach 17, the dealer should break and lose. Otherwise,
# highest number wins
if dealerTotal > 21:
    print("The dealer busted, and you won!")
    quit()
elif dealerTotal > playerTotal:
    print("The Dealer won! :( Try again next time.")
    quit()
elif playerTotal > dealerTotal:
    print("Congratulations! :) You won!")
    quit()
elif playerTotal == dealerTotal:
    print("It is a tie. :/ Try again next time.")
    quit()
