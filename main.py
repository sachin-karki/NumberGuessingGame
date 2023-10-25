# Sachin Karki
# Purpose: Assignment 8, Number Guessing Game

import os

# Clearing the Screen
os.system('clear')

# Welcome Screen
print("Welcome to Number Guessing Game")
print()

# Setting up condition
correctNumber = 10

while True:
    try:
        numberInput = input("Choose a number between 1 to 100 (or Q/q to Quit): ")

        if numberInput.lower() == 'q': # Ensures the input 'q' works with both uppercase and lowercase
            print("Quitting the game.")
            break  # This quits the program

        numberInput = int(numberInput)  # Converts input to an integer

        if numberInput == correctNumber:
            print("Good Job! Your Guess is Correct")
            break  # Stops the program if correct input is given
        elif numberInput > correctNumber:
            print("Wrong Guess, It's less than", numberInput, "Please Try Again")
        elif numberInput < correctNumber:
            print("Your Guess is Wrong, It's more than", numberInput, "Please Try Again")

    except ValueError: # This throws an error message if a non-numeric input is given
        print("Invalid input. Please enter a valid number between 1 and 100.")
