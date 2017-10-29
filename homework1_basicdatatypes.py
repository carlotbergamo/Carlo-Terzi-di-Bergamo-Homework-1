if __name__ == '__main__':       #first
    N = int(raw_input())
    newl=[]
    for ins in range((N)):
        a=raw_input()
        b=a.split()
        if b[0]=='insert':
            newl.insert(int(b[1]),int(b[2]))
        if b[0]=='print':
            print newl
        if b[0]=='remove':
            newl.remove(int(b[1]))
        if b[0]=='append':
            newl.append(int(b[1]))
        if b[0]=='pop':
            newl.pop()
        if b[0]=='sort':
            newl.sort()
        if b[0]=='reverse':
            newl.reverse()
            

if __name__ == '__main__':     #second
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print hash(t)


if __name__ == '__main__':    #third
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    l=[]
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                d=[a,b,c]
                if a+b+c!=n:
                    l+=[d]
    print l
    

if __name__ == '__main__':    #fourth
    n = int(raw_input())
    arr = map(int, raw_input().split())
    ma=max(arr)
    newarr=set(arr)
    arr=list(newarr)
    arr.remove(ma)
    print max(arr)
    

l=[]                           #fifth
l_score=[]
final=[]
for _ in range(int(raw_input())):
    name=raw_input()
    score=float(raw_input())
    l_score+=[score]
    l+=[[name,score]]
min_score=min(l_score)
while min_score in l_score:
    l_score.remove(min_score)
second_min_score=min(l_score)
for element in l:
    if element[1]==second_min_score:
        final+=[element[0]]
end=sorted(final)
for player in end:
    print player


if __name__ == '__main__':     #sixth
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    mark=student_marks[query_name]
    percent='%.2f'%((sum(mark))/(len(mark)))
    print percent