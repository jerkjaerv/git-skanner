#import plotly.express as px
#import pandas as pd
import math

coordinatelist=[]
dict={"x":[], "y":[]}

def distcoord(coord):#förvandla distans och vinkel till koordinater, ger först x sedan y
    y=coord[1]*math.sin(math.radians(coord[0]))
    x=coord[1]*math.cos(math.radians(coord[0]))
    return x,y

def distlist(coordlist, rawdata):#förvandla lista med distans och vinkel till lista med koordinater
    n=-1
    for x in rawdata:
        n=n+1
        coordlist.append(distcoord(rawdata[n]))
    return coordlist

def coordtoplot(plotlycoord, coordlist): #funktion som omvandlar vår koordinatlista till en dictionary som plotly kan använda, index 0 är x, index 1 är y
    n=-1
    for i in coordlist:
        n=n+1
        plotlycoord["x"].append(coordlist[n][0])
        plotlycoord["y"].append(coordlist[n][1])
    return(plotlycoord)

#dataframeformulering nedan
#df=pd.DataFrame(coordtoplot(dict, distlist(coordinatelist,raw)))
#fig = px.line(df, x="x", y="y", title="test") 
#fig.show()