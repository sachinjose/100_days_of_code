import random

print("Welcome to the PyPassword Generator")

no_letters = int(input("How many letters would you like in your password: "))
no_symbols = int(input("How many symbols would you like: "))
no_number = int(input("How many numbers would you like: "))

total_length = no_number + no_symbols + no_letters;

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

for i in range(no_letters):
	password.append(random.choice(letters))

for i in range(no_symbols):
	password.append(random.choice(symbols))

for i in range(no_number):
	password.append(random.choice(numbers))

random.shuffle(password)

password = "".join(password)

print(f" Here is your Password : {password}")