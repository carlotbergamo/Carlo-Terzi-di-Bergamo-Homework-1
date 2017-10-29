a=raw_input()     #first
all_size=map(int , (raw_input()).split())
money=0
for i in range(int(raw_input())):
    costumer=map(int , (raw_input()).split())
    size=costumer[0]
    if size in all_size:
        money+=costumer[1]
        all_size.remove(size)
print money


from collections import defaultdict   #second
d=defaultdict(list)
l=[]
a=map(int, (raw_input()).split())
for i in range(a[0]):
    b=(raw_input())
    d[b].append(i+1)
for t in range(a[1]):
    c=raw_input()
    l+=[c]
for element in (l):
    if element in d:
        result=' '.join(map(str, d[element]))
        print result
    else:
        print (-1)


from collections import namedtuple  #third
number_student=int(raw_input())
name_items=(raw_input())
student=namedtuple('student', name_items)
mark=0
for i in range(number_student):
    x, y, z, w=(raw_input()).split()
    t=student(x, y, z, w)
    mark+=int(t.MARKS)
avarage=float(mark)/number_student
print '%.2f' % avarage


from collections import OrderedDict    #fourth
number_items=int(raw_input())
d=OrderedDict()
for i in range(number_items):
    items=raw_input().split()
    if len(items)==3:
        if (items[0]+' '+items[1]) in d:
            d[items[0]+' '+items[1]]=int(d[items[0]+' '+items[1]])+int(items[2])
        else:
            d[items[0]+' '+items[1]]=int(items[2])
    if len(items)==2:
        if (items[0]) in d:
            d[items[0]]=int(d[items[0]])+int(items[1])
        else:
            d[items[0]]=int(items[1])

for element in d:
    print element, d[element]


from collections import OrderedDict   #fifth
number_items=int(raw_input())
d=OrderedDict()
l=[]
for i in range(number_items):
    items=raw_input()
    if (items) in d:
        d[items]=(d[items])+1
    else:
        d[items]=1
        l+=[items]
print len(l)
for element in d:
    print d[element],


from collections import deque   #sixth
number_items=int(raw_input())
d=deque()
for i in range(number_items):
    item=(raw_input()).split()
    if item[0]=='append':
        d.append(int(item[1]))
    if item[0]=='pop':
        d.pop()
    if item[0]=='popleft':
        d.popleft()
    if item[0]=='appendleft':
        d.appendleft(int(item[1]))
                 
for element in d:
    print element,


from collections import deque   #seventh
number_cubes=int(raw_input())
lst=[]
for i in range(number_cubes):
    a=int(raw_input())
    b=deque(map(int, (raw_input()).split()))
    b_sorted=sorted(b)
    while len(b)>=1:
        if b[0]>=b[-1]:
            lst+=[b[0]]
            b.popleft()
        else:
            lst+=[b[-1]]
            b.pop()
    if lst==b_sorted[::-1]:
        print 'Yes'
    else:
        print 'No'
    lst=[]


import sys                                    #eighth
from collections import Counter, OrderedDict
if __name__ == "__main__":
    s = (raw_input().strip())
    number_items=(Counter(s).items())
    i= sorted(number_items, key = lambda x: (-x[1],x[0]))
    for x, y in i[:3]:
        print x, y