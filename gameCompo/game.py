# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

from gameComponents import gameVars


def winorlose(status):
	if status =="won":
		pre_message = "You are the yuuuuuuugest winner ever!"
	else:
		pre_message ="You done trumped it, loser!"

	print(pre_message + "Would you like to play again?")

	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":

		global player_lives
		global gameVars.computer_lives
		global player

		player_lives = 5
		gameVars.computer_lives =5
		player = False

	elif choice == "N" or "no":

		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice -Y or N")	

		choice = input("Y / N")
		
				 		


# set up our game loop
while gameVars.player is False:
	# this is the player choice
	print("===============*/ RPS /*====================")
	print("gameVars.Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
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
	gameVars.gameVars.computer = gameVars.choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + gameVars.player)

	# validate that the random choice worked for the AI
	print("AI chose: " + gameVars.computer)

	if (gameVars.computer == gameVars.player):
		print("tie")

	# always check for negative conditions first (the losing case)
	elif (gameVars.computer == "rock"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	elif (gameVars.computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1


	elif (gameVars.computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.player_lives -= 1
			print("you lose! player lives: ", gameVars.player_lives)
		else:
			print("you win!")
			gameVars.computer_lives -= 1

	# check player lives and AI lives
	if player_lives is 0:
		winorlose("lost")
		#print("You lost! Loser. Would you like to play again?")
		#choice = input("Y / N? ")

		#if choice == "Y" or choice == "y":
			# reset the game and start over again
		#	player_lives = 2
		#	gameVars.computer_lives = 2
		#	player = False

		#elif choice == "N" or choice == "n":
			# exit message and quit
		#	print("You chose to quit. Better luck next time!")
		#	exit()
		#else:
		#	print("Make a valid choice - Y or N")
			# this is generating a bug -> need to fix this check
		#	choice = input("Y / N")

	elif gameVars.computer_lives is 0:
		winorlose("won")
		
		#print("You won! Winner. Would you like to play again?")
		#choice = input("Y / N? ")

		#if choice == "Y" or choice == "y":
			# reset the game and start over again
		#	player_lives = 2
		#	gameVars.computer_lives = 2
		#	player = False

		#elif choice == "N" or choice == "n":
			# exit message and quit
		#	print("You chose to quit. Better luck next time!")
		#	exit()
		#else:
			# this is generating a bug -> need to fix this check
		#	print("Make a valid choice - Y or N")
		#	choice = input("Y / N")

	else:
		gameVars.player = False
		# gameVars.computer = choices[randint(0,2)]