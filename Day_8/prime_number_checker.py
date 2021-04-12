def prime_checker(number):
	flag = True
	for i in range(2,int(number/2)):
		if number%i == 0 :
			print("Non Prime")
			flag = False
			break;
	if(flag == True):
		print("Prime")



n = int(input('Enter the number '))
prime_checker(n)