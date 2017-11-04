#Python 3 Solution

#Get two integers from user
num1, num2= map(int,input("Enter two integers:").strip().split())

if (num1 + num2 < 0):
	print("|(%d)+(%d)| = %d" %(num1,num2,-1*(num1+num2)))
else:
	print("|(%d)+(%d)| = %d" %(num1,num2,(num1+num2)))