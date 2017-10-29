from itertools import product    #first
A=map(int,(raw_input()).split())
B=map(int,(raw_input()).split())
c=(list(product(A,B)))
for i in c:
    print i,


from itertools import permutations    #second
a=(raw_input()).split()
b=a[0]
numb=int(a[1])
l=[]
s=''
c=list(permutations(b,numb))
for element in c:
    for letter in element:
        s+=letter
        if len(s)==numb:
            l+=[s]
            s=''
l.sort()
for result in l:
    print result


from itertools import combinations    #third
a=(raw_input()).split()
string=a[0]
number=int(a[1])
l=[]
s=''
for integer in range(1,number+1):
    b=list(combinations(string, integer))
    for element in b:
        for letter in element:
            s+=letter
            if len(s)==integer:
                c=sorted(s)
                d=''.join(c)
                l+=[d]
                s=''
    l.sort()
    for i in l:
        print i
    l=[]


from itertools import combinations_with_replacement   #fourth
a=(raw_input()).split()
string=a[0]
number=int(a[1])
s=''
l=[]
b=list(combinations_with_replacement(string, number))
for element in b:
    for letter in element:
        s+=letter
    c=sorted(s)
    d=''.join(c)
    l+=[d]
    s=''
l.sort()
for i in l:
    print i


from itertools import groupby   #fifth
a=raw_input()
for k , g in groupby(a):
    b=(len(list(g)))
    c=int(k)
    print (b, c),
    

from itertools import combinations   #sixth
number_list=int(raw_input())
a=(raw_input()).split()
number_combinations=int(raw_input())
l=[]
p=[]
numb=0
count=0
if 'a' in a:
    if number_list==number_combinations:
        print float(1)
    else:
        for i in range(1,number_list+1):
            l+=[i]
        comb=list(combinations(l, number_combinations))
        lenght=float(len(comb))
        for letter in a:
            if letter=='a':
                ind=a.index(letter)
                numb+=1
                p+=[ind+numb]
        for element in comb:
            if element[0] in p:
                count+=1
        result=count/lenght
        print result
else:
    print float(0)


from itertools import product    #seventh
a=(raw_input()).split()
second_number=int(a[1])
l=[]
q=[]
z=[]
for i in range((int(a[0]))):
    b=map(int, (raw_input()).split())
    b.pop(0)
    l+=[b]
for element in product(*l):
    for p in element:
        q+=[p**2]
    x=(sum(q)) % second_number
    z+=[x]
    q=[]
print max(z)