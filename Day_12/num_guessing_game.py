import random
print('Welcome to the number guessing game!')
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")

if difficulty == 'easy':
	turns = 10

if difficulty == 'hard':
	turns = 5

answer = random.randint(1,100)

print(f'You have {turns} turns left')

flag = False

while turns > 0:

	guess = int(input("Make a guess : "))
	if(guess == answer):
		flag = True;
		print("You've guessed the correct number! ")
		break

	else:

		print("You guessed wrong!")
		turns-=1

		if(guess > answer):
			print("You guessed higher")

		if(guess < answer):
			print("You guessed lower")

		print(f'You have {turns} turns left')


if(flag == False):
	print('You Lost!')