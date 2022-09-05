import math
import numpy as np
import random


def H2O(atoms,bonds,angles,NH2O,L):
	minDis=5e-10
	minDis2=minDis*minDis
	Lhalf=L*0.5-2.5e-10

	O=np.array((1,1,1,-0.83,0,0,0))
	H1=np.array((2,1,2,0.415,0.757,0.5859,0))
	H2=np.array((3,1,2,0.415,-0.757,0.5859,0))
	if(len(atoms)==0):
		atomsOffset=0
		moleculeOffset=0
	else:
		atomsOffset=np.max(atoms.T[0])
		moleculeOffset=np.max(atoms.T[1])
	for i in np.arange(NH2O):
		flag=1
		while(flag):
			flag=0
			r=np.array([random.uniform(-Lhalf,Lhalf),random.uniform(-Lhalf,Lhalf),random.uniform(-Lhalf,Lhalf)])
			for j in atoms:
				if(np.sum((j[4:7]-r)**2)<minDis2):
					flag=1
		o=np.zeros(7)+O
		o[0]+=i*3+atomsOffset
		o[1]+=i+moleculeOffset
		o[4:7]+=r*1e10
		h1=np.zeros(7)+H1
		h1[0]+=i*3+atomsOffset
		h1[1]+=i+moleculeOffset
		h1[4:7]+=r*1e10
		h2=np.zeros(7)+H2
		h2[0]+=i*3+atomsOffset
		h2[1]+=i+moleculeOffset
		h2[4:7]+=r*1e10

		atoms=np.append(atoms,np.array([o]),axis=0)
		atoms=np.append(atoms,np.array([h1]),axis=0)
		atoms=np.append(atoms,np.array([h2]),axis=0)
		bonds=np.append(bonds,np.array([[i*2+1,1,i*3+1+atomsOffset,i*3+2+atomsOffset]]),axis=0)	
		bonds=np.append(bonds,np.array([[i*2+2,1,i*3+1+atomsOffset,i*3+3+atomsOffset]]),axis=0)	
		angles=np.append(angles,np.array([[i+1,1,i*3+2+atomsOffset,i*3+1+atomsOffset,i*3+3+atomsOffset]]),axis=0)	
	return atoms,bonds,angles




