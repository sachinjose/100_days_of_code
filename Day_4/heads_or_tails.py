import random

print("Welcome to Virtual Coin Flipper ")

random_integer = random.randint(1,2)
if(random_integer == 1):
	print("Heads")
else:
	print("Tails")