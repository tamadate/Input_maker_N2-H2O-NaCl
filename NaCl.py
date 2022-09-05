import math
import numpy as np
import random


def NaCl(atoms,iL,L):
	minDis=5e-10
	minDis2=minDis*minDis

	a=5.63*0.5

	nacl=np.array(((1,1,4,1,0,0,0),(1,1,5,-1,0,0,0)))
	loop=0
	for ix in np.arange(iL):
		for iy in np.arange(iL):
			for iz in np.arange(iL):
				add=(nacl[int(loop%2)]+np.array((loop,loop,0,0,ix*a,iy*a,iz*a)))
				atoms=np.append(atoms,np.array([add]),axis=0)
				loop+=1
	return atoms





