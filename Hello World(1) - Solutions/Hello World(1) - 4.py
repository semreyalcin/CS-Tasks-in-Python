''' 
There is another input function other than input().
input() takes an integer input but it has some security problems, 
so from now on we will be using raw_input() function.
raw_input() function takes any input as string. To be able to use
this "raw" input which is string we need to change its type.
you can search typecasting for further information.
'''

x1,y1 = raw_input("Enter the coordinates for upper left(x y):").strip().split()
x2,y2 = raw_input("Enter the coordinates for upper left(x y):").strip().split()

'''
strip() function deletes the unnecessary characters at the beginning
and the end of the input which may be entered by an accident by user.
if no character is defined when you call upon the function, whitespace 
will be used by default.

split() function splits the string using a defined seperator. If no
seperator is defined when you call upon the function, whitespace will 
be used by default.
'''

# We typecast the variables to integer so we can use them.
area = (int(x2)-int(x1)) * (int(y1)-int(y2))

# While printing we changed type of our integer to string
print "Area is:" + str(area)