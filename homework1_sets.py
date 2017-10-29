def average(array): #first
    s=set(array)
    somma=sum(s)
    lun=len(s)
    avarage=somma/lun
    return avarage


a=raw_input()  #second
firstset=(raw_input()).split()
newfset = list(map(int, firstset))
b=raw_input()
secondset=(raw_input()).split()
newsset = list(map(int, secondset))
l=[]
for element1 in newfset:
    if element1 not in newsset:
        l+= [element1]
for element2 in newsset:
    if element2 not in newfset:
        l+= [element2]
finalset=set(l)
setsort=sorted(finalset)
for i in setsort:
    print i
    

nm=raw_input()   #third
array=(map(int, (raw_input().split())))
seta=set(map(int, (raw_input().split())))
setb=set(map(int, (raw_input().split())))
happiness=0
for number in array:
    if number in seta:
        happiness+=1
    elif number in setb:
        happiness-=1
print happiness


N=int(raw_input()) #fourth
s=set([])
for numb in range(N):
    country=raw_input()
    s.add(country)
l=len(s)
print l


n = raw_input()    #fiveth
s = set(map(int, raw_input().split()))
numb=int(raw_input())
for elem in range(numb):
    b=(raw_input()).split()
    if b[0]=='pop':
        s.pop()
    if b[0]=='remove':
        s.remove(int(b[1]))
    if b[0]=='discard':
        s.discard(int(b[1]))
tot=sum(s)
print tot


english=raw_input()    #sixth
student_english=(raw_input()).split()
french=raw_input()
student_french=(raw_input()).split()
neweng=[]
newfre=[]
for studeng in student_english:
    neweng+=[int(studeng)]
for studfre in student_french:
    newfre+=[int(studfre)]
final_english=set(neweng)
final_french=set(newfre)
total=final_english.union(final_french)
final=len(total)
print final


english=raw_input()   #seventh
student_english=set(map(int,(raw_input().split())))
french=raw_input()
student_french=set(map(int,(raw_input().split())))
total_student=student_english.intersection(student_french)
tot=len(total_student)
print tot


english=raw_input()    #eighth
student_english=set(map(int,(raw_input().split())))
french=raw_input()
student_french=set(map(int,(raw_input().split())))
only_english= student_english.difference(student_french)
tot=len(only_english)
print tot


english=raw_input()    #nineth
student_english=set(map(int,(raw_input().split())))
french=raw_input()
student_french=set(map(int,(raw_input().split())))
french_english=student_english.symmetric_difference(student_french)
tot=len(french_english)
print tot


a=raw_input()     #tenth
first_set=set(map(int, (raw_input().split())))
N=int(raw_input())
for i in range(N):
    operation=(raw_input()).split()
    second_set=set(map(int, (raw_input().split())))
    if operation[0]=='intersection_update':
        first_set.intersection_update(second_set)
    if operation[0]=='update':
        first_set.update(second_set)
    if operation[0]=='symmetric_difference_update':
        first_set.symmetric_difference_update(second_set)
    if operation[0]=='difference_update':
        first_set.difference_update(second_set)
final_sum=sum(first_set)
print final_sum


n=int(raw_input())    #eleventh
rooms=((map(int, (raw_input().split()))))
set_room=set(rooms)
a=sum(set_room)*n
b=sum(rooms)
c=(a-b)/(n-1)
print c


for i in range(int(raw_input())):    #twelveth
    a = int(raw_input()); A = set(raw_input().split())
    b = int(raw_input()); B = set(raw_input().split())
    print not bool(A.difference(B))


A=set(map(int, (raw_input().split())))  #thirteenth
numb=0
result=False
for i in range(int(raw_input())):
    B=set(map(int, (raw_input().split())))
    if not bool(B.difference(A))==False:
        numb+=1
    if A==B:
        numb+=1
if numb==0:
    result=True
print result