logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message,shift):
	list1 = list(message)
	for i in range(len(list1)):
		if(list1[i].isalpha()):
			pos = alphabet.index(list1[i])
			new_pos = (pos + shift)%26;
			list1[i] = alphabet[new_pos]
	message = ''.join(list1)
	print(message)


def decode(message,shift):
	list1 = list(message)
	for i in range(len(list1)):
		if(list1[i].isalpha()):
			pos = alphabet.index(list1[i])
			new_pos = (pos - shift)%26;
			list1[i] = alphabet[new_pos]
	message = ''.join(list1)
	print(message)

print(logo)
exitVar = 'yes'

while(exitVar!='no'):

	decision = input("Type 'encode' to encrypt, 'decode' to decrypt : ")
	message = input("Type your message : ").lower()
	shift = int(input("Type shift number : "))

	if(decision == 'encode'):
		output = encode(message,shift)

	if(decision == 'decode'):
		output = decode(message,shift)


	exitVar = input("Type 'yes' if you want to go again. Otherwise enter 'no'. ")
