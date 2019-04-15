#!/usr/bin/python


def GetPerimeterRectangle(side_x, side_y):
	#return side_x + side_y + side_x + side_y
	# p = x + x + y + y
	# p = 2x + 2y
	# p = 2(x+y)
	return 2*(int(side_x) + int(side_y))

def GetPerimeterSquare(side_x):
	return side_x + side_x + side_x + side_x

def GetAreaRectangle(side_x, side_y):
	# a = x * y
	return side_x * side_y

def GetAreaSquare(side_x, side_y):
	# a = x * y
	return side_x * side_y

def GetSideLength(Ax, Ay, Bx, By):
	if Ax == Bx:
		return abs(Ay - By)
	else:
		return abs(Ax - Bx)

def GetOtherSides(Ax, Ay, Dx, Dy):
	'''
		A(x,y) ------- B(x,y)
                  |               |
                  |               |
                C(x,y) ------- D(x,y)
	
	'''
	Bx = Dx
        By = Ay
	Cx = Ax
        Cy = Dy

	return Bx, By, Cx, Cy
       

if __name__ == "__main__":
	print("GetPerimeterRectangle of side x=10 y=20 is %d\n" %(GetPerimeterRectangle(10, 20)))
	
