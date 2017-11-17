x = int(input("Enter an integer: "))
summ = 0
counter = 0
while (x != -1):
  summ += x
  counter += 1
  x = int(input("Enter an integer: "))

print("Sum is : %d\tAverage is : %.2f" %(summ,(summ/counter)))