def clear():
	print(chr(27)+'[2j')
	print('\033c')
	print('\x1bc')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

max_name = ""
auction = {}
flag = True

while(flag):

	person_name = input("Enter the name: ")
	price = int(input("What is your bid price: "))
	auction[person_name] = price;

	if(max_name == ""):
		max_name = person_name

	else:
		if(price > auction[max_name]):
			max_name = person_name

	decision = input("Does other users want to bid?: ")

	if(decision == 'no'):
		flag = False
	
	if(decision == 'yes'):
		clear()

print(f"{max_name} wins the bid")