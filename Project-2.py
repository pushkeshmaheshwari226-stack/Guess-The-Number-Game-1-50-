# # We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.

# Hint: Use the random module.

import random
number=random.randint(1,50)
print("GUESS BETWEEN 1 TO 50")
guess=0
tries=0


while (guess!= number):
    guess=int(input("Enter your guess"))
    tries+=1

    if tries>=10:
        print("MAXIMUM TRIES REACHED")
    if(guess==0):
        print("EXITED")
        break
    
    if (guess>number):
        print("GUESS LOWER !")

    elif(guess<number):
        print("GUESS HIGHER")

    else:
        print("YOU GOT IT RIGHT !")
        print(f"Attempts taken {tries}")
