if __name__ == '__main__':  #first
    print "Hello, World!"


if __name__ == '__main__':    #second
    n = int(raw_input())
    if n%2!=0:
        print 'Weird'
    else:
        if 2<n<5 or n>20:
            print 'Not Weird'
        else:
            print 'Weird'


if __name__ == '__main__':   #third
    a = int(raw_input())
    b = int(raw_input())
    su=a+b
    div=a-b
    mol=a*b
    print su
    print div
    print mol


from __future__ import division   #fourth
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a//b
    print a/b


if __name__ == '__main__':   #fifth
    n = int(raw_input())
    for i in range(n):
        print i**2


def is_leap(year):    #sixth
    leap = False
    if year%4==0:
        leap = True
    if year%100==0:
        leap = False
    if year%400==0:
        leap = True
    
    return leap
    

from __future__ import print_function     #seventh
if __name__ == '__main__':
    n = int(raw_input())
    p = range(1,n+1)
    print (*p,sep='')