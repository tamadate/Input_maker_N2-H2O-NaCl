import math
import numpy as np
import random

def inputLAMMPS(masses,atoms,bonds,angles,dihedrals,L,fileName):
	with open(fileName, "w") as f:
		f.write("\n")
		Nat=int(len(atoms.T[0]))
		f.write(str(Nat)+"\tatoms\n")
		Nb=int(len(bonds.T[0]))
		f.write(str(Nb)+"\tbonds\n")
		Nan=int(len(angles.T[0]))
		f.write(str(Nan)+"\tangles\n")
		if(dihedrals==0):
			Ndi=0
		else:
			Ndi=int(len(dihedrals.T[0]))
		f.write(str(Ndi)+"\tdihedrals\n\n")

		Nat=int(np.max(atoms.T[2]))
		f.write(str(Nat)+"\tatom types\n")
		Nb=int(np.max(bonds.T[1]))
		f.write(str(Nb)+"\tbond types\n")
		Nan=int(np.max(angles.T[1]))
		f.write(str(Nan)+"\tangle types\n")
		if(dihedrals==0):
			f.write("0\tdihedral types\n\n")
		else:
			f.write(str(len(dihedrals.T[1]))+"\tdihedral types\n\n")
		f.write(str(-L*0.5)+" "+str(L*0.5)+" xlo xhi\n")
		f.write(str(-L*0.5)+" "+str(L*0.5)+" ylo yhi\n")
		f.write(str(-L*0.5)+" "+str(L*0.5)+" zlo zhi\n\n")
		f.write("Masses\n\n")
		for i in np.arange(len(masses)):
			f.write(str(i+1)+"\t"+str(masses[i])+"\n")
		f.write("\nAtoms\n\n")
		for i in atoms:
			f.write(str(int(i[0]))+"\t"+str(int(i[1]))+"\t"+str(int(i[2]))+"\t"+str(i[3])+"\t"+str(i[4])+"\t"+str(i[5])+"\t"+str(i[6])+" 0 0 0\n")
		f.write("\nBonds\n\n")
		for i in bonds:
			f.write(str(int(i[0]))+" "+str(int(i[1]))+" "+str(int(i[2]))+" "+str(int(i[3]))+"\n")
		f.write("\nAngles\n\n")
		for i in angles:
			f.write(str(int(i[0]))+" "+str(int(i[1]))+" "+str(int(i[2]))+" "+str(int(i[3]))+" "+str(int(i[4]))+"\n")


