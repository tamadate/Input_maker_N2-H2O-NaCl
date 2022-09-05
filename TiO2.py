import math
import numpy as np

a=4.5922
c=a*0.644005052045
x2=0.30496
x=np.array((0,0,0,a,0,0))
y=np.array((0,0,0,0,a,0))
z=np.array((0,0,0,0,0,c))
Ti=np.array((0,1,2.196,0,0,0))
O=np.array((0,2,-1.098,0,0,0))

TiO2=np.zeros((6,6))
TiO2[0]=(0,0,0,0,0,0)+Ti
TiO2[1]=0.5*x+0.5*y+0.5*z+Ti
TiO2[2]=x2*x+x2*y+O
TiO2[3]=-x2*x-x2*y+O
TiO2[4]=(0.5-x2)*x+(0.5+x2)*y+0.5*z+O
TiO2[5]=(0.5+x2)*x+(0.5-x2)*y+0.5*z+O

Crystal=np.zeros((0,6))
for i in np.arange(0,20):
	for j in np.arange(20):
		for k in np.arange(20):
			Crystal=np.append(Crystal,(i*x+j*y+k*z+TiO2),axis=0)

cut=6
cut2=cut*cut
cluster=np.zeros((0,6))
center=np.array((np.average(Crystal.T[3]),np.average(Crystal.T[4]),np.average(Crystal.T[5])))
for i in Crystal:
	if(np.sum((i[3:]-center)**2)<cut2):
		cluster=np.append(cluster,[i],axis=0)

No=0
NoO=0
for i in cluster:
	No+=1
	i[0]=No
	i[3:]=i[3:]-center
	if i[1]==2:
		NoO+=1

print (NoO)
NoTi=No-NoO

for loop in np.arange(NoO-NoTi*2):
	maxdistance=0
	for i in np.arange(np.size(cluster.T[0])):
		if(cluster[i][1]==2 and maxdistance<np.sum(cluster[i][3:]**2)):
			maxdistance=np.sum(cluster[i][3:]**2)
			removei=i
	cluster=np.delete(cluster,removei,axis=0)

No=0
NoO=0
for i in cluster:
	No+=1
	i[0]=No
	if i[1]==2:
		NoO+=1

print (NoO)
print (No-NoO)




with open("test.data","w") as f:
	for i in cluster:
		f.write(str(int(i[0]))+"\t"+str(int(i[1]))+"\t"+str((i[2]))+"\t"+str(i[3])+"\t"+str(i[4])+"\t"+str(i[5])+"\n")


##np.savetxt("test.data",cluster)
