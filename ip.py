infix=input("Enter infix:\n")
s=[]
prec={'(':-1,')':-1,"-":0,"+":0,"*":1,"/":1,"^":2}
def extra(o):
    if s==[]:
        s.append(o)
    elif s[-1]=='(':
        s.append(o)
    elif prec[s[-1]]>=prec[o]:
        print(s.pop())
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
            print(t)
            t=s.pop()
    else:
        print(i)
while(s!=[]):
    print(s.pop())
