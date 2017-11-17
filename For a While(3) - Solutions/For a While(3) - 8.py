n,m = map(int,input("Enter n: ").strip().split())

if(n>m):
  minimum = m
else:
  minimum = n

gcd = 1

for i in range(2,minimum+1):
  while(m%i == 0 and n%i == 0):
    gcd *= i
    m = m // i
    n = n // i
    
print("GCD is: %d" %gcd)