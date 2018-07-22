import numpy as np
import petsc4py
from petsc4py import PETSc

n = 100

x = PETSc.Vec().create(comm=PETSc.COMM_WORLD)
x.setType('mpi')
x.setSizes(n)

print(x.getOwnershipRange())
