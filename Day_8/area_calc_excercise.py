
import math

def paint_calc(height, width, cover):
	area = (height*width)
	numOfCans = math.ceil(area/cover);
	print(numOfCans)


test_h = int(input("Enter the height of the wall "))
test_w = int(input("Enter the width of the wall "))
coverage = 5 #area covered by a can of paint
paint_calc(height = test_h,width = test_w, cover = coverage)