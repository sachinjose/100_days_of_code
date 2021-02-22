student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0

for i in student_heights:
	sum+=i

average = sum/(len(student_heights))

print(average)