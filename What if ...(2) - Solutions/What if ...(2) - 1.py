#Python 3 Solution

#We get user's age
age = int(input("Enter your age:").strip())

#Compare the age of the user to 50 
if(age < 50):
	print("You are under 50")
elif(age > 50):
	print("You are over 50")
else: #Since there are no posibilities than user being 50, it okay to use else
	print("You are 50")