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
myWord = list(myWord)
guessList = "_____"
guessList = list(guessList)

misses = []

countB = 0

tries = int(input("How many tries would you like? "))

# If a Letter is in a word
while True:
	letter = input("Enter a letter or type 'Guess' to guess the word: ")




	if letter == "Guess":
		guess = input("What is the word?")
		myWord = "hello"
		if guess == myWord:
			print("You Win! The Word Was " + str(myWord))
			break
		else:
			print("Wrong answer. Try again")

	if letter in myWord:
		count = 0
		for letterA in myWord:
			if letterA in letter:
				guessList[count] = letter
			count += 1

	print(guessList)

	if letter in myWord:
		print("The letter is in the word")
	else:
		misses.append(letter)
		print("The letter is not in the word")
		print("Misses:" + str(misses))
		tries = tries-1
		print("Tries left: " + str(tries))
		print(frameList[countB])
		countB = countB + 1
	if tries == 0:
		print("Game Over--You Lose")
		break

	countA = 0

	for letterB in myWord:
		if letterB == letter:
			print("The letter is in space " + str(countA))
		
		countA += 1
