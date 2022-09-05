import math
import numpy as np
import random
import lammpsInput
import H2O
import N2
import NaCl

T=300
kb=1.38e-23
NH2O=100
S=10
ps=3170
p=S*ps
V=kb*T*NH2O/p
L=V**(1/3.0)

pgas=1e3
NN2=int(pgas*V/kb/T)
print(NN2)
print(NH2O)

atoms=np.zeros((0,7))
bonds=np.zeros((0,4))
angles=np.zeros((0,5))
#masses=np.array((15.999,1.008,14.00))
masses=np.array((15.999,1.008,14.00,22.99,35.453))

atoms=NaCl.NaCl(atoms,3,L)
atoms,bonds,angles=H2O.H2O(atoms,bonds,angles,NH2O,L)
atoms,bonds=N2.N2(atoms,bonds,NN2,L)

lammpsInput.inputLAMMPS(masses,atoms,bonds,angles,0,L*1e10,"tip3p.atom")



