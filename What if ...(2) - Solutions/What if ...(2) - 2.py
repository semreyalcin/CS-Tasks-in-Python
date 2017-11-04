#Python 3 Solution

#Get the speed from user
speed = int(input("Enter the speed:").strip())

#Check speed and calculate penalty
if(speed <= 80):
	print("There are no penalty")
else:
	penalty = (speed - 80) * 15
	print("Penalty is: %d TL" %penalty)
