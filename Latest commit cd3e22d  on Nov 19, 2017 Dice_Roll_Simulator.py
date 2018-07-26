import random
# This is a simple dice rolling game
print("Welcome to Dice Rolling Simulator \n")

# create initial random variable
rand = random.randint(1, 6)
print("Dice Roll Number: " + str(rand))

# Ask if user wants to play again
rollAgain = str(input("Want to roll again? (yes or no): "))

# Game logic
while rollAgain.lower() == "yes":
    newRand = random.randint(1, 6)
    print("Dice Roll Number: " + str(newRand))

    rollAgain = str(input("Want to roll again? (yes or no): "))

if rollAgain.lower() == "no":
    print("Goodbye, the until next time")




