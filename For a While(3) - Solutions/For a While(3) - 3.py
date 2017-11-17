x = int(input("Enter an integer: "))
digit = 0

while(x != 0):
  x = x//10
  digit += 1
  
print("%d digit(s)" %digit)