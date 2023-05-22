import numpy as np

# HEISENBERG MODEL
def heisenberg(N: int, S, parameters):
    J, dz, kBT, muB, gamma, mu, alpha = parameters
    Hmat = 1/mu * (J*(np.roll(S,-1,axis=0) + np.roll(S,1,axis=0)))
    Hmat[:,2] += 1/mu * (2*dz*S[:,2] + muB)
    return Hmat