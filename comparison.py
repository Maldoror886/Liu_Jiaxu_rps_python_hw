from gameComponents import gameVars, winLost

def comparison(computer):
    print("test")
    if (computer == gameVars.player):
        print("tie")

	# always check for negative conditions first (the losing case)
    elif (computer == "rock"):
	    if (gameVars.player == "scissors"):
                gameVars.player_lives -= 1
                print("you lose! player lives: ", gameVars.player_lives)
	    else:
	        print("you win!")
	        gameVars.computer_lives -= 1

    elif (computer == "paper"):
            if (gameVars.player == "scissors"):
                gameVars.player_lives -= 1
                print("you lose! player lives: ", gameVars.player_lives)
            else:
                print("you win!")
                gameVars.computer_lives -= 1

    elif (computer == "scissors"):
            if (gameVars.player == "paper"):
                gameVars.player_lives -= 1
                print("you lose! player lives: ", gameVars.player_lives)
            else:
                print("you win!")
                gameVars.computer_lives -= 1

	  # check player lives and AI lives
    if gameVars.player_lives is 0:
          winorlost.winorlose("lost")

    elif gameVars.computer_lives is 0:
          winLost.winorlose("won")
    else:
          gameVars.player = False
