import random


x = 1
s = int(input("How many numbers would you like:"))
while x <= s:
	print(random.randint(1,6))
	x += 1