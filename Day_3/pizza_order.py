print("Welcome to Pizza Order Menu")
s = input("What size do you require S,M,L: ")
add_pepperoni = input("Do you require pepperoni Y or N: ")
extra_cheese = input("Do you require cheese Y or N: ")
bill = 0

if s == 'S':

	bill+=15
	if(add_pepperoni == 'Y'):
		bill+=2

elif s == 'M':

	bill+=20
	if(add_pepperoni == 'Y'):
		bill+=3

elif s =='L':

	bill+=25
	if(add_pepperoni == 'Y'):
		bill+=3

if(extra_cheese == 'Y'):
	bill+=1

print(f"Your total bill is : {bill}")