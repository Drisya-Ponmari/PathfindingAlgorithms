import numpy.matlib
import matplotlib.animation as an
import heapq as h
import matplotlib.pyplot as plt
n=int(raw_input("size of grid"))
xs=int(raw_input("x_s"))
ys=int(raw_input("y_s"))
ob=int(raw_input("number of obstacles"))
O=[]
for i in range(ob):
    x=int(raw_input("x_ob"))
    y=int(raw_input("y_ob"))
    O.append([x,y])
xd=int(raw_input("x_d"))
yd=int(raw_input("y_d"))

d=[xd,yd]
ims=[]
fig = plt.figure()
m=numpy.matlib.zeros((n,n))
m[xs,ys]=2
m[xd,yd]=3
for i in range(len(O)):
    m[O[i][0],O[i][1]]=1
def heuristic(a,b):
    E=numpy.sqrt(((a[0]-b[0])*(a[0]-b[0]))+((a[1]-b[1])*(a[1]-b[1])))
    return E
li=[]
h.heapify(li)
count=0
h.heappush(li,[0,[xs,ys]])
pa={}
p={}
p[0]=([xs,ys])
pa[0]=([-1,-1])
while(len(li)!=0):
    k=h.heappop(li)
    x=k[1][0]
    y=k[1][1]
    if(x-1 <n and x-1>=0 and m[x-1,y]==3):
        m[x-1,y]=4
        
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        break
    if(x+1 <n and x+1>=0 and m[x+1,y]==3):
        m[x+1,y]=4
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        
        break
    if(y+1 <n and y+1>=0 and m[x,y+1]==3):
        m[x,y+1]=4
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        
        break
    if(y-1 <n and y-1>=0 and m[x,y-1]==3):
        m[x,y-1]=4
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        
        break
    if(x-1 <n and y-1 <n and x-1 >=0 and y-1>=0 and m[x-1,y-1]==9):
        m[x-1,y-1]=100
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        
        break
    if(x+1 <n and y+1 <n and x+1>=0  and y+1>=0and  m[x+1,y+1]==9):
        m[x+1,y+1]=100
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        
        break
    if(x-1 <n  and y+1 <n and x-1>=0 and y+1>=0and  m[x-1,y+1]==9):
        m[x-1,y+1]=100
        im=plt.imshow(m,cmap='Spectral')
        ims.append([im])
        
        break
    if(x+1 <n and y-1<n and x+1>=0 and y-1>=0 and m[x+1,y-1]==9):
        m[x+1,y-1]=100
        #im=plt.imshow(m,cmap='Spectral')
        #ims.append([im])
        
        break
#moveup
    if(x-1 <n and x-1>=0 and m[x-1,y]!=1 and m[x-1,y]!=2):
        count=count+1
        pr=heuristic([x-1,y],d)
        h.heappush(li,[pr,[x-1,y]])
        p[count]=([x-1,y])
        pa[count]=([x,y])
        m[x-1,y]=2
#movedown
    if(x+1 <n and x+1>=0 and m[x+1,y]!=1 and m[x+1,y]!=2):
        count=count+1
        pr=heuristic([x+1,y],d)
        h.heappush(li,[pr,[x+1,y]])
        p[count]=([x+1,y])
        pa[count]=([x,y])
        m[x+1,y]=2
#left
    if(y-1 <n and y-1>=0 and m[x,y-1]!=1 and m[x,y-1]!=2):
        count=count+1
        pr=heuristic([x,y-1],d)
        h.heappush(li,[pr,[x,y-1]])
        p[count]=([x,y-1])
        pa[count]=([x,y])
        m[x,y-1]=2
#right
    if(y+1 <n and y+1>=0 and m[x,y+1]!=1 and m[x,y+1]!=2):
        count=count+1
        pr=heuristic([x,y+1],d)
        h.heappush(li,[pr,[x,y+1]])
        p[count]=([x,y+1])
        pa[count]=([x,y])
        m[x,y+1]=2
    if(x-1 <n and y-1<n and x-1>=0 and y-1>=0 and m[x-1,y-1]!=1 and m[x-1,y-1]!=2):
        count=count+1
        pr=heuristic([x-1,y-1],d)
        h.heappush(li,[pr,[x-1,y-1]])
        p[count]=([x-1,y-1])
        pa[count]=([x,y])
        m[x-1,y-1]=2
    if(x+1 <n and y+1 <n and x+1>=0 and y+1>=0 and m[x+1,y+1]!=1 and m[x+1,y+1]!=2):
        count=count+1
        pr=heuristic([x+1,y+1],d)
        h.heappush(li,[pr,[x+1,y+1]])
        p[count]=([x+1,y+1])
        pa[count]=([x,y])
        m[x+1,y+1]=2
    if(x-1 <n and y+1<n and x-1>=0 and y+1>=0 and m[x-1,y+1]!=1 and m[x-1,y+1]!=2):
        count=count+1
        pr=heuristic([x-1,y+1],d)
        h.heappush(li,[pr,[x-1,y+1]])
        p[count]=([x-1,y+1])
        pa[count]=([x,y])
        m[x-1,y+1]=2
    if(x+1 <n and y-1<n and x+1>=0 and y-1>=0 and m[x+1,y-1]!=1 and m[x+1,y-1]!=2):
        count=count+1
        pr=heuristic([x+1,y-1],d)
        h.heappush(li,[pr,[x+1,y-1]])
        p[count]=([x+1,y-1])
        pa[count]=([x,y])
        m[x+1,y-1]=2
    
    #im=plt.imshow(m,cmap='Spectral')
    #ims.append([im])
        
h=len(pa)
i=0
m[x,y]=6
while(i<h):
    j=0
    while(j<=len(p)):
        if(p[j][0]==x and p[j][1]==y):
            break
        j=j+1
    if(pa[j]==[-1,-1]):
        break
    [x,y]=pa[j]
    m[x,y]=6
    i=i+1
#im=plt.imshow(m,cmap='Spectral')
#ims.append([im])
#ani=an.ArtistAnimation(fig,ims,interval=1000)
plt.imshow(m)	        
plt.show()
