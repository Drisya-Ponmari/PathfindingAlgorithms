import numpy.matlib
import os
import time
import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as an
#fetching input
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

ims=[]
fig = plt.figure()
#creating matrix
m=numpy.matlib.zeros((n,n))
m[xs,ys]=2
m[xd,yd]=9
for i in range(len(O)):
	m[O[i][0],O[i][1]]=1
	
#bfs initialisation and bfs algorithm
li=[-1]
counter=1
p={}
p[-1]=([xs,ys])
heapq.heapify(li)
pa={}
pa[-1]=([-1,-1])
while(len(li)!=0):
	k=heapq.heappop(li)
	x=p[k][0]
	y=p[k][1]
	if(x-1<n and x-1>=0 and m[x-1,y]==9):
		m[x-1,y]=100
		im=plt.imshow(m,cmap='Spectral')
        	ims.append([im])
		break
	if(x+1<n and x+1<=0 and m[x+1,y]==9):
		m[x+1,y]=100
		im=plt.imshow(m,cmap='Spectral')
        	ims.append([im])
		break
	if(y+1<n and y+1>=0 and  m[x,y+1]==9):
		m[x,y+1]=100
		im=plt.imshow(m,cmap='Spectral')
        	ims.append([im])
		break
	if(y-1<n and y-1>=0 and m[x,y-1]==9):
		m[x,y-1]=100
		im=plt.imshow(m,cmap='Spectral')
        	ims.append([im])
		break
#moveup
	if(x-1<n and x-1>=0 and m[x-1,y]!=1 and m[x-1,y]!=2):
		counter=counter+1
		heapq.heappush(li,-counter)
		p[-counter]=([x-1,y])
		pa[-counter]=([x,y])
		m[x-1,y]=2
#movedown
	if(x+1<n and x+1>=0 and m[x+1,y]!=1 and m[x+1,y]!=2):
		counter=counter+1
		heapq.heappush(li,-counter)
		p[-counter]=([x+1,y])
		pa[-counter]=([x,y])
		m[x+1,y]=2

#moveleft
	if(y-1<n and y-1>=0 and m[x,y-1]!=1 and m[x,y-1]!=2):
		counter=counter+1
		heapq.heappush(li,-counter)
		p[-counter]=([x,y-1])
		pa[-counter]=([x,y])
		m[x,y-1]=2


#moveright
	if(y+1<n and y+1>=0 and m[x,y+1]!=1 and m[x,y+1]!=2):
		counter=counter+1
		heapq.heappush(li,-counter)
		p[-counter]=[x,y+1]
		pa[-counter]=([x,y])
		m[x,y+1]=2
	im=plt.imshow(m,cmap='Spectral')
        ims.append([im])
	#os.system("sleep 1")
	#os.system("clear")
	#print(m)
h=len(pa)
i=0
m[x,y]=8
while(i<h):
	j=1
	while(j<=len(p)):
		if(p[-j][0]==x and p[-j][1]==y):
			break
		j=j+1
	if(pa[-j]==[-1,-1]):
		break
	[x,y]=pa[-j]
	m[x,y]=8
	i=i+1
im=plt.imshow(m,cmap='Spectral')
ims.append([im])
ani=an.ArtistAnimation(fig,ims,interval=100)
plt.show()	
