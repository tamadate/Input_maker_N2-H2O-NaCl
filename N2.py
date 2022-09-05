import math
import numpy as np
import random


def N2(atoms,bonds,NN2,L):
	Lhalf=L*0.5-2.5e-10
	minDis=5e-10
	minDis2=minDis*minDis

	N1=np.array((1,1,3,0,-0.549,0,0))
	N2=np.array((2,1,3,0,0.549,0,0))
	atomsOffset=np.max(atoms.T[0])
	moleculeOffset=np.max(atoms.T[1])
	bondsOffset=np.max(bonds.T[0])
	for i in np.arange(NN2):
		flag=1
		while(flag):
			flag=0
			r=np.array([random.uniform(-Lhalf,Lhalf),random.uniform(-Lhalf,Lhalf),random.uniform(-Lhalf,Lhalf)])
			for j in atoms:
				if(np.sum((j[4:7]-r)**2)<minDis2):
					flag=1
		n1=np.zeros(7)+N1
		n1[0]+=i*2+atomsOffset
		n1[1]+=i+moleculeOffset
		n1[4:7]+=r*1e10
		n2=np.zeros(7)+N2
		n2[0]+=i*2+atomsOffset
		n2[1]+=i+moleculeOffset
		n2[4:7]+=r*1e10

		atoms=np.append(atoms,np.array([n1]),axis=0)
		atoms=np.append(atoms,np.array([n2]),axis=0)
		bonds=np.append(bonds,np.array([[i+1+bondsOffset,2,n1[0],n2[0]]]),axis=0)	
	return atoms,bonds





