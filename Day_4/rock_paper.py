import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]
turn = input("What do you choose?. 0 for Rock, 1 for Paper, 2 for Scissors ")
turn = int(turn)
print(f"You played {game[turn]}")

random_int = random.randint(0,2)

print(f"Computer Played {game[random_int]}")

if(turn == 0 and random_int == 2):
	print(" You win ")
elif(turn == 1 and random_int == 0):
	print(" You win ")
elif(turn ==2 and random_int ==1):
	print("You win")
else:
	print("You loose")