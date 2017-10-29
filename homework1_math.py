# -*- coding: utf-8 -*-
import cmath    #first
complex_number=complex(raw_input())
r=abs(complex_number)
sigma=cmath.phase(complex_number)
print ('%.3f' % r)
print ('%.3f' % sigma)


import math    #second
AB=int(raw_input())
BC=int(raw_input())
final= (math.degrees(math.atan2(AB,BC)))
final_angle=str(int(round(final)))+'°'
print final_angle


for i in range(1,int(raw_input())+1):     #third
    print [0,1,121,12321,1234321,123454321,12345654321,1234567654321,123456787654321,12345678987654321][i]


a=int(raw_input())     #fourth
b=int(raw_input())
print a//b
print a%b
print divmod(a, b)


a=int(raw_input())   #fiveth
b=int(raw_input())
m=int(raw_input())
print pow(a, b)
print pow(a, b, m)


a=int(raw_input())  #sixth
b=int(raw_input())
c=int(raw_input())
d=int(raw_input())
print (pow(a,b))+(pow(c,d))


for i in range(1,input()):   #seventh
    print [0,1,22,333,4444,55555,666666,7777777,88888888,999999999][i]