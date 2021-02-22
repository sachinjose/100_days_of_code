import random

names_string = input("Enter the names. Seperated by a comma : ").split(',')
random_integer = random.randint(0,len(names_string)-1)

print(f"The bill will be paid by {names_string[random_integer]}")

print(f"The bill will be paid by {random.choice(names_string)}")