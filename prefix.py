infix=input("Enter infix:\n")
def reverse(s):
    r=""
    for i in s[::-1]:
        if i ==')':
            r+='('
        elif i=='(':
            r+=')'
        else:
            r+=i
    return r
infix=reverse(infix)

p=""
s=[]
prec={'(':-1,')':-1,"-":0,"+":0,"*":1,"/":1,"^":2}
def extra(o):
    global p
    if s==[]:
        s.append(o)
    elif s[-1]=='(':
        s.append(o)
    elif prec[s[-1]]>=prec[o]:
        p+=s.pop()
        extra(o)
    else:
        s.append(o)
for i in infix:
    if i in "+-/*^":
        extra(i)
    elif i =='(':
        s.append(i)
    elif i==')':
        t=s.pop()
        while(t!='('):
            p+=t
            t=s.pop()
    else:
        p+=i
while(s!=[]):
    p+=s.pop()
print(reverse(p))
