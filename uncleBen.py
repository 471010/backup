
# Imports
import random
# Variables
playerScore = -0
computerScore = 0
ties = 0
# Make a list
cChoices = ["r", "p", "s"]
print("Welcome back Uncle Ben")
start = input("This is Rock Paper Scissors. Press Enter to start")
# Main loop
while True:
	# Print Score
	print("Score:")
	print("Flint Marko: " + str(computerScore))
	print("Uncle Ben: " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit:")
	computerChoice = random.choice(cChoices)

	if choice == "q":
		print("Uncle Ben Died")
		break
	if choice == "r":
		print("Uncle Ben Picked Rock")
		if computerChoice == "r":
			print("Flint Marko picked Gun")
			print("Gun beats Rock")
			computerScore += 1
		elif computerChoice == "p":
			print("Flint Marko picked Gun")
			print("Gun beats Rock")
			computerScore += 1
		else:
			print("Flint Marko picked Gun")
			print("Gun beats Rock")
			computerScore += 1
	elif choice == "p":
		print("Uncle Ben Picked Paper")
		if computerChoice == "r":
			print("Flint Marko picked Gun")
			print("Gun beats Paper")
			computerScore += 1
		elif computerChoice == "p":
			print("Flint Marko picked Gun")
			print("Gun beats Paper")
			computerScore +=1
		else:
			print("Flint Marko picked Gun")
			print("Gun beats Paper")
			computerScore += 1
	elif choice == "s":
		print("Uncle Ben Picked Scissors")
		if computerChoice == "p":
			print("Flint Marko picked Gun")
			print("Gun beats Scissors")
			computerScore += 1
		elif computerChoice == "r":
			print("Flint Marko picked Gun")
			print("Gun beats Scissors")
			computerScore += 1
		else:
			print("Flint Marko picked Gun")
			print("Gun beats scissors")
			computerScore +=1
	elif choice == "g":
		print("Uncle Ben Fights back")
		print("Uncle Ben Wins and Lives!")
		print("Live a nice life Uncle Ben")
		break
	else:
			print("Uncle Ben has been shot, and killed and it's all your fault")
			break