n = int(input("Enter n: "))

for i in range(n): #Controls lines
  for j in range(n-i-1): #Controlds spaces
    print(" ",end='') 
  for k in range(i+1): #Controls stars
    print("*",end='')
  print() #Going to the next line
  
#Easier way of doing this :)
#for i in range(n):
#  print(" "*(n-i-1) + "*"*(i+1))