def swap_case(s): #first exercize of string
    news=s.swapcase()
    return news
    
    
def split_and_join(line): #second
    line=line.split(' ')
    line='-'.join(line)
    return line
    

def print_full_name(a, b): #third
    print 'Hello '+ a +' '+ b +'! You just delved into python.'
    

def mutate_string(string, position, character): #fourth
    l=list(string)
    l[position]=character
    newst=''.join(l)
    return newst
    

def count_substring(string, sub_string): #fifth
    n=0
    lun=len(sub_string)
    for let in range(len(string)):
        if string[let]==sub_string[0]:
            if string[let:let+lun]==sub_string:
                n+=1
    return n
    

if __name__ == '__main__': #sixth
    s = raw_input()
    print any(let.isalnum() for let in s)
    print any(let.isalpha() for let in s)
    print any(let.isdigit() for let in s)
    print any(let.islower() for let in s)
    print any(let.isupper() for let in s)
    

thickness = int(raw_input()) #This must be an odd number #seventh
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)


import textwrap #eighth
def wrap(string, max_width):
    f=textwrap.fill(string, max_width)
    return f


N, M = map(int,raw_input().split()) #nineth
for i in xrange(1,N,2): 
    print ('.|.'*i).center(M, "-")
print ((M-7)/2)*'-'+'WELCOME'+((M-7)/2)*'-'
for i in xrange(N-2,-1,-2): 
    print ('.|.'*i).center(M, '-')


def print_formatted(number): #tenth
    lun=len(bin(number)[2:])
    for i in range(1,number+1):
        o=oct(i)[1:]
        h=(hex(i)[2:]).upper()
        b=bin(i)[2:]
        print '{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(i,o,h,b,width=lun)


def print_rangoli(size):        #11
    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v=[]
    for element in range(len(l)):
        if element<=(size-1):
            v+=[l[element]]
    q=range(size)
    z=q[::-1]
    for i in (z):
        h='-'.join(l[i:(size)])
        print (h[::-1]+h[1:]).center((size*4)-3, '-')
    for i in range(size):
        if i==0:
            continue
        else:
            h='-'.join(l[i:(size)])
            print (h[::-1]+h[1:]).center((size*4)-3, '-')


def capitalize(string):   #12
    a=string.split(' ')
    cap=''
    for element in a:
        d=element.capitalize()
        cap+=d+' '
        
    return cap
    
    
def minion_game(string):   #13
    stuart=0
    kevin=0 #vowel
    vowels=['A','E','I','O','U']
    for single_letter in range(len(string)):
        if string[single_letter] in vowels:
            kevin+=(len(string)-single_letter)
        else:
            stuart+=len(string)-single_letter
    
    if kevin<stuart:
        print 'Stuart', stuart
    elif stuart<kevin:
        print 'Kevin', kevin
    elif stuart==kevin:
        print 'Draw'


def merge_the_tools(string, k):   #14
    l=[]
    s=''
    for letter in string:
        l+=[letter]
        if len(l)==k:
            for i in l:
                if l.count(i)>=2:
                    l=l[::-1]
                    l.remove(i)
                    l=l[::-1]
            for element in l:
                s+=element
            print s
            l=[]
            s=''