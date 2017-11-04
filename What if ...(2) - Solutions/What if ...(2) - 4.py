#Python 3 Solution

#Get the number will be checked from the user
num = int(input("Enter an integer:").strip())

#We use % operator to find if the number is 
#divisible by 2 
if (num % 2 == 0):
	#Or (not(num % 2))
	print("Even!")
else:
	print("Odd!")