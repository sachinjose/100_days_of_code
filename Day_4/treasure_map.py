# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
left,right = input("Where do you want to put the treasure? ").split()
map[int(left)][int(right)]='X'

print(f"{row1}\n{row2}\n{row3}")