logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calc(first_no,second_no,operation):
	if(operation == 1):
		return first_no+second_no
	if(operation == 2):
		return first_no - second_no
	if(operation == 3):
		return first_no * second_no
	if(operation == 4):
		return first_no/second_no
	else:
		return False

loop_var = True

while(loop_var):

	first_no = int(input("What's the first number: "))
	second_no = int(input("What's the second number: "))
	operation = int(input(" + \n - \n * \n / \nPick an operation from the line above: "))

	ans = calc(first_no,second_no,operation)

	print(ans)

	dec = input("Do you want to continue(y/n): ")

	if(dec == "n"):
		break

