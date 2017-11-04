#Python 3 Solution

f1, f2, f3= map(int,input("Enter the first line of the matrix:").strip().split())
s1, s2, s3= map(int,input("Enter the second line of the matrix:").strip().split())
t1, t2, t3= map(int,input("Enter the third line of the matrix:").strip().split())

print("Result is:%d" %((f1 * s2 * t3) + (f3 * s2 * t1) ) )