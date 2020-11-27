# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLost

import comparison

# set up our game loop
while gameVars.player is False:
# this is the player choice
    print("===============*/ RPS /*====================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("===================================")
    print("Choose your weapon! or type quit to exit\n")


    gameVars.player = input("Choose rock, paper or scissors: \n")

# if the player chooses to quit, then don't do anything else
# just exit the process (kill Python) and quit the game
    if gameVars.player == "quit":
            print("You chose to quit, quitter!")
            exit()

# this will be the AI choice -> a random pick from the choices array
    computer = gameVars.choices[randint(0, 2)]

# check to see what the user input

# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
    print("user chose: " + gameVars.player)

# validate that the random choice worked for the AI
    print("AI chose: " + computer)

    comparison.comparison(computer)
