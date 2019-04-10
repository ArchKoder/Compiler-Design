productions=[]
first={}
follow={}
V=[]
def next(s,c):
    l=[]
    for i in range(len(s)-1):
        if s[i]==c:
            l.append(s[i+1])
    return l

def find_first(c,rules=productions):
    for r in rules:
        if r[2]=='#':
            if(len(r)>3):
                r=r[:2]+r[3:]
                find_first(c,rules)
            else:
                first[c].append('#')
        else:
            if (r[2].islower()) | (not(r[2].isalpha())):
                first[c].append(r[2])
            else:
                if r[2] in first:
                    first[c]=first[r[2]]
                else:
                    first[r[2]]=[]
                    find_first(r[2],[p for p in productions if p[0]==r[2]])
                    first[c]=first[r[2]]
def find_follow(c):
    if c==productions[0][0]:
        follow[c].append('$')
    rules=[p for p in productions if c in p[2:]]
    for r in rules:
        if len(r)>3:
            t=next(r[2:],c)
            for i in t:
                if i.isalpha():
                    follow[c]+=first[i]
                else:
                    if i!='#':
                        follow[c].append(i)
            if '#' in follow[c]:
                follow[c].remove('#')
        if (r[-1]==c) & (r[0]!=c):
            if r[0] in follow:
                follow[c]+=follow[r[0]]
            else:
                follow[r[0]]=[]
                find_follow(r[0])
                follow[c]+=follow[r[0]]

if __name__=="__main__":
    s=input("Enter the production rules!\nEnter #### when finished!\n")
    while(s!="####"):
        productions.append(s)
        s=input()
    V=list(set([i[0] for i in productions]))
    for v in V:
        rules=[p for p in productions if p[0]==v]
        first[v]=[]
        find_first(v,rules)
    for v in V:
        if v not in follow:
            follow[v]=[]
        find_follow(v)
    print("First:")
    for i,j in first.items():
        print(i,j)
    print("Follow:")
    for i,j in follow.items():
        j=list(set(j))
        print(i,j)
