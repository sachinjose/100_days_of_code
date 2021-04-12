
## simple function
def greet():
	print('Hello! ')
	print('How do you do! ')
	print("Isn't the weather nice today ")
greet()

##Function that allows for input 

# parameter is the name of the data that is being passed through 
# the argument is the value that is being transferred

def greet(name):
	print(f"Hello! {name}")
	print(f"How do you do! {name}")
	print("Isn't the weather nice today ")

greet('Sachin')

def greet_2(name, location):
	print(f"Hello! {name}")
	print(f"What is it like in {location}")

greet_2('Sachin','Kochi') #Positional Aruguments
greet_2(location = 'Kochi',name = 'Sachin') ##Keyword Arguments

