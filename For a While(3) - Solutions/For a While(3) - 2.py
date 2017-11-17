x = int(input("Enter an integer: "))
binary = 0
digit = 0

while(x != 0):
  remainder = x%2
  binary = binary + remainder*10**digit
  digit += 1
  x = x // 2
  
print("The binary value is: %d" %binary)