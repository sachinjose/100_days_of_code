def letter_add(password,letters):
			random_int = random.randint(0,len(letters)-1)
			password.append(letters[random_int])

def number_add(password,numbers):
			random_int = random.randint(0,len(numbers)-1)
			password.append(numbers[random_int])

def symbol_add(password,symbols):
			random_int = random.randint(0,len(symbols)-1)
			password.append(symbols[random_int])


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

letter_no = 0
symbol_no = 0
number_no = 0

for i in range(total_length):

	turn = random.randint(0,2)

	if(turn == 0):

			if(letter_no < no_letters):
				letter_no+=1
				letter_add(password,letters)

			elif(symbol_no < no_symbols):
				symbol_no+=1
				symbol_add(password,symbols)

			elif(number_no < no_number):
				number_no+=1
				number_add(password,symbols)

			else:
				pass


	elif(turn == 1): 

			if(number_no < no_number):
				number_no+=1
				number_add(password,symbols)

			elif(letter_no < no_letters):
				letter_no+=1
				letter_add(password,letters)

			elif(symbol_no < no_symbols):
				symbol_no+=1
				symbol_add(password,symbols)

			else:
				pass

	else:
			if(symbol_no < no_symbols):
				symbol_no+=1
				symbol_add(password,symbols)

			elif(letter_no < no_letters):
				letter_no+=1
				letter_add(password,letters)

			elif(number_no < no_number):
				number_no+=1
				number_add(password,symbols)

			else:
				pass



password = "".join(password)

print(f" Here is your Password : {password}")