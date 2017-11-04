#Python 3 Solution

#Get the point from user
x, y= map(int,input("Enter the coordinates(x y):").strip().split())

if(x < 0):
	if(y < 0):
		print("3rd Quadrant")
	elif(y > 0):
		print("2nd Quadrant")
	else:
		print("X-axis")
elif(x > 0):
	if(y < 0):
		print("4th Quadrant")
	elif(y > 0):
		print("1st Quadrant")
	else:
		print("X-axis")
else:
	if(y):
		print("Y-axis")
	else:
		print("Origin")