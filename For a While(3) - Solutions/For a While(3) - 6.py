x = int(input("Enter an integer: "))
prime = True

for i in range(2,x-1):
  #To make this algorithm to work faster, you can check until x/2
  #To make it even faster, you can check until x**(1/2) (= sqrt(x))
  if(x % i == 0):
    prime = False
    break

if prime:
  print("PRIME")
else:
  print("NOT PRIME")