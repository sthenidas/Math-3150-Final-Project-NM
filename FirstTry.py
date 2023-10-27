import numpy as np

U[1] = 1.0/A[1];

for i in range(N):
  U[i] = 1.0/(A[i] - U[i-1])

R[1] = B[1]*U[1];
for i in range(N):
  R[i] = (B[i] - R[i-1]*U[i])

psi[N} = R[N]
for i in range(N-1,0,-1):
  psi[i] = R[i] - U[i]*psi[i+1]
