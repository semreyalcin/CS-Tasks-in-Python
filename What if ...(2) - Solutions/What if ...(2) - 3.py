#Python 3 Solution

#Get how many hours the user worked
hours = int(input("Enter how many hours you worked:").strip())

#Calculate the salary according to hours worked
if(hours < 0):
	print("Invalid input!")
elif(hours <= 90):
	salary = 20 * hours
elif(hours <= 160): 
	#If hours > 90 then it will check this condition,
	#otherwise it will enter the first if condition.
	#Therefore, we don't need to check if hours is
	#bigger than 90 in this condition. (90<hours<=160)
	salary = (20 * 90) + (30 * (hours - 90))
else:
	salary = (hours)**2

#Print salary if input is valid
if(not(hours < 0)): 
	#If (hours < 0) condition is wrong it will print salary
	print("Your salary is: %d TL" %salary)