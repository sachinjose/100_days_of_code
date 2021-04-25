import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def points_calc(usr):
	points = 0
	for i in range(len(usr)):
		points +=usr[i]	
	if 11 in usr:
		if points > 21:
			points -= 10

	return points
		
def deal_card(usr):
	cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	random_integer = random.randint(1,12)
	usr.append(cards[random_integer])

user = []
computer = []

print(logo)

decision = 'y'
flag = True

while(decision!='n'):

	decision = input("Do you want to play a game of Blackjack. Type 'y' or 'n' ")
	deal_card(user)
	deal_card(user)
	deal_card(computer)
	deal_card(computer)
	user_score = points_calc(user)
	computer_score = points_calc(computer)
	print(f"Your cards: {user}")
	print(f"Current Score : {user_score}")
	print(f"Computer's First Card: {computer}")

	card = input(" Type 'y' to get another card, type 'n' to pass: ")

	if(computer_score < 16):
		deal_card(computer)

	if(card == 'y'):
		deal_card(user)

	user_score = points_calc(user)
	computer_score = points_calc(computer)

	print(f"Your final hand: {user}")
	print(f" final Score : {user_score}")
	print(f" Computer's final hand: {computer}")
	print(f" Computer's final Score : {computer_score}")

	if(user_score > 21):

		print("You went over. You Lose! :( ")

	elif(computer_score > 21) :
		print('You win!')

	elif(computer_score == user_score):
		print('You drew')	
	
	elif(user_score > computer_score):
		print("You Win! :) ")

	elif(user_score < computer_score) :
		print('You Loose :(')

	decision = input("Do you want to play a game of Blackjack. Type 'y' or 'n' ")
