x = int(input("Enter an integer: "))
fact = 1

while(x > 0):
  fact *= x
  x -= 1

print("Factorial is: %d" %fact)