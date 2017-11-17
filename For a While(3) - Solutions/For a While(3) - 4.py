x = int(input("Enter an integer: "))
rev = 0

while(x != 0):
  lastdigit = x%10
  rev *= 10 
  rev = rev + lastdigit
  x = x // 10
   
  
print("The new number is: %d" %rev)