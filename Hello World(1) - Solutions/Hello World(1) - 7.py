radius = float(raw_input("Enter The radius:").strip())

'''
While working with floats better use other numbers as floats aswell
Try calculating volume like this:
volume = 4/3*3.14*radius*radius*radius
You can check the 4th answer for further information
https://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-division-keeps-rounding-down-to-0
'''
volume = 4.0/3.0*3.14*radius*radius*radius
print "Volume is:%.2f" %(volume)

'''
%f means there will be a float in there. And the .2 means i want only 2
digits after the dot in the float.
'''