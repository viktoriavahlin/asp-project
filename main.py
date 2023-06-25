import numpy as np
from solver import HeunSolver, initializeSpinGroundStateWave
from eqs import LLG
from plot import plotXYZ, animate

def run(N, parameters):
    '''Simulate N spins'''
    t0 = 0 # start time
    tEnd = 5
    delt = 0.1
    timeSteps = int((tEnd-t0)/delt)
    print("timesteps: ", timeSteps)
    t = np.linspace(t0,tEnd,timeSteps)

    # Number of spins
    num = N

    # Initilaization of spin in random directions
    S0 = initializeSpinGroundStateWave(num)

    S_solution = HeunSolver(t, delt, S0, LLG, parameters, num)
    plotXYZ(S_solution,t)
    animate(S_solution,t,num)


# ------------------------------------------------------ #
#                       CONSTANTS                        #
# Predefined constant
gamma = 1.6e11 # HzT−1  - Absolute value of the electron gyromagnetic ratio
mu = 5.8e-2 # meV/T     - Bohr magneton
ez = np.array([0,0,1]) #- Unit vector in z direction

# Input parameters
J = 10 # meV            - Heizenberg coupling constant
dz = 0.3*J # meV        - Easy axis anisotropy constant
kBT = 0 # meV, = 0.1J   - Temperature
muB = 3 # mev, 0.3J     - Homogenous magnetic field μB0(x, t) = μB0 = const. along the z-direction
alpha = 0.2 #           - Gilbet damping coefficient
muB = 3 # meV           - Magnetiv field
# ------------------------------------------------------ #

# Defining the parameters parameters
parameters = [J, dz, kBT, muB, gamma, mu, alpha]
numSpins = 50 # Number of spins to model
run(numSpins, parameters)