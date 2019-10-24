import time
import os
import random


frameList = ['''
  +--+
     |
     |
     |
    ***
''','''
  +--+
  O  |
     |
     |
    ***
''','''
  +--+
  O  |
  |  |
     |
    ***
''','''
  +--+
  O  |
  |\ |
     |
    ***
''','''
  +--+
  O  |
 /|\ |
     |
    ***
''','''
  +--+
  O  |
 /|\ |
 /   |
    ***
''','''
  +---+
 \O/  |
  |   |
  \\\  |
      ***
''']

myWord = "hello"

misses = []




tries = int(input("How many tries would you like? "))





choice = input("Type a word: ")


if choice == myWord:
	print("It's a match")
else:
	print("Not a match")

# If a Letter is in a word
while True:
	letter = input("Enter a letter or type 'Guess' to guess the word: ")




	if letter == "Guess":
		guess = input("What is the word?")
		if guess == myWord:
			print("You Win!")
			break
		else:
			print("Wrong answer. Try again")

	if letter in myWord:
		print("The letter is in the word")
	else:
		misses.append(letter)
		print("The letter is not in the word")
		print("Misses:" + str(misses))
		tries = tries-1
		print("Tries left: " + str(tries))
	if tries == 0:
		print("Game Over-You Lose")
		break

	if misses == "10":
		print("You Lose")
		break

	count = 0

	for letter2 in myWord:
		if letter2 == letter:
			print("The letter is in space " + str(count))
		
		count += 1
