#4.1
a=5.08 #2004
b=5.33 #2014
c=5.55 #2024
d=b-a #2014-2004
e=c-b #2024-2014
print("The increase from 2004 to 2014 is",d)
print("The increase from 2014 to 2024 is",e)
if d>e:
    print("The increase from 2004 to 2014 is greater than the increase from 2014 to 2024")
elif d<e:
    print("The increase from 2014 to 2024 is greater than the increase from 2004 to 2014")
else:
    print("The increase from 2004 to 2014 is equal to the increase from 2014 to 2024")
#d is larger. Population growth is decelerating in Scotland.

#4.2
X=True
Y=False
W=X or Y
print(W)  #True
# X=True, Y=False  W=True
# X=True, Y=True   W=True
# X=False, Y=True  W=True
# X=False, Y=False  W=False
