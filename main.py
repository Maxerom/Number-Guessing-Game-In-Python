# Importing important Libraries
import random
import math

lower_bound = int(input("Enter Lower bound = ")) # Taking integer type lower bound input from user

upper_bound = int(input("Enter Upper bound = ")) # Taking integer type upper bound input from user

x = random.randint(lower_bound, upper_bound) # Taking any random integer to guess

chances = math.log(upper_bound - lower_bound + 1, 2) # Taking log to check how many tries user is needed for this

print("\n\t You have only ", round(chances), " chances to guess the integer!\n")

counter = 0

while counter < chances:
    counter += 1

    guess = int(input("Guess a number = "))  # Taking guess from user

    if x == guess:                                                           # If user guessed right then this condition will run
        print("Congratulations you did it in ", counter, " try.")   
        break
    elif x > guess:                            # If user guessed a lower number then the real answer then this condition will run
        print("You guessed too small!")
    elif x < guess:                            # If user guessed a higher number then the real answer then this condition will run
        print("You guessed too high!")


if counter >= chances:                         # If user is unable to guess any right answer then this condition will run
    print("\nThe number is %a" % x)
    print("\tBetter Luck Next Time!")