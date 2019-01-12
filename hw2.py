import math
a='My computer is acer'
b='65161681'

print a[10:18]
c=a[10:18]
print 'min char is split string=',min(c)
print a.replace('uter','uters')
d=a.replace('uter','uters')
print d.replace('is','are')

if b.isdigit():
	d=int (b)
	print math.sqrt(d)
else:
	print 'write the string value'
