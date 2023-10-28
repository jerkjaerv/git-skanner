def getfunc(coords1, coords2): #mata in två koordinater så får man en rät funktion för dem'
    if coords1[0]==coords2[0]:
        return 0, coords1[1]
    k=(coords1[1]-coords2[1])/(coords1[0]-coords2[0])
    m=coords1[1]-k*coords1[0]
    return k, m

def getarea(coords1, coords2): #få arean för en rät linje mellan två koordinater, tar 
    return abs((getfunc(coords1, coords2)[0]/2)*coords2[0]**2+getfunc(coords1,coords2)[1]*coords2[0]-((getfunc(coords1,coords2)[0]/2)*coords1[0]**2+getfunc(coords1,coords2)[1]*coords1[0]))

def getareafull(coordinatelist): #arean mellan räta linjer för alla våra koordinater, tar en lista med tvåtuple
    n=-1
    area=0
    for x in coordinatelist:
        if n==len(coordinatelist)-2:
            return area+getarea((coordinatelist[n+1]),(coordinatelist[0]))
        n=n+1
        area=area+getarea((coordinatelist[n]), (coordinatelist[n+1]))