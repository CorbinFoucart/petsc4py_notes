from petsc4py import PETSc

rank = PETSc.COMM_WORLD.Get_rank()
size = PETSc.COMM_WORLD.Get_size()

print('Hello, from process {rank} of {size} procs'.format(rank=rank, size=size))
