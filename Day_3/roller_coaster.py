bill =0
height = int(input("What is your height?: "))
if(height >= 120):
	print("You can ride the roller coaster")
	age = int(input("What is your age: "))
	if(age<12):
		bill = 5
		print("You pay 5 Dollars")
	elif(age<18):
		bill = 7
		print("You pay 7 Dollars")
	elif(age>=45 and age <=55 ):
		print("Its going to be okay, Free ride on US!")
	else:
		bill = 12
		print("You pay 12 Dollars")
	choice = input("Do you want a photo(Y/N): ")
	if(choice == 'Y'):
		bill+=5

	print(f"Your final bill is : {bill}")

else:
	print("Grow taller and come back later")
