import numpy as np
from solver import HeunSolver, initializeSpinRandomeDir
from eqs import LLG
from plot import plotXYZ
# -------------------------------------- #
#            DEFINE CONSTANTS            #
J = 10 # meV            - Heizenberg coupling constant
dz = 3 # meV, = 0.3J    - Uniaxial anisotropy constant
kBT = 1 # meV, = 0.1J   - Temperature
muB = 3 # mev, 0.3J     - Homogenous magnetic field μB0(x, t) = μB0 = const. along the z-direction
B = np.array([0,0,1]) # - Direction of magnetic field
gamma = 1.6e11 # HzT−1  - Absolute value of the electron gyromagnetic ratio
mu = 5.8e-2 # meV/T      - Bohr magneton
ez = B
# -------------------------------------- #


# CONSTANTS
# gamma = 1.76e11     # [Hz/T] gyromagnetic ratio
# muB = 9.274e-24     # [J/T] Bohr magneton
# kB = 1.3806-23      # [J/K] Boltzmann constant

def testOneSpin():
    '''Test simulation for one spin'''
    t0 = 0 # start time
    tEnd = 1
    delt = 0.01
    timeSteps = int((tEnd-t0)/delt)
    t = np.linspace(t0,tEnd,timeSteps)

    S0x = 0.1 
    S0y = 0.2
    S0 = np.array([S0x,S0y,np.sqrt(1-S0x**2-S0y**2)]) # initial spin

    # Number of spins
    num = 1

    # damping cases;
    alpha = 0 # undamped
    alpha1 = 0.1 # damping case 1
    alpha2 = 0.5 # damping case 2

    # Defining the parameters parameters = [J, dz, kBT, muB, gamma, mu, alpha]
    kBT = 0; J = 0; B0 = 0; dz = 1; muB = mu*B0
    parameters1 = [J, dz, kBT, muB, gamma, mu, alpha1]
    parameters2 = [J, dz, kBT, muB, gamma, mu, alpha2]

    # Temperatur case
    alpha = 0.1
    kBT = 0.1*dz
    parameters = [J, dz, kBT, muB, gamma, mu, alpha]

    # S_solution01 = HeunSolver(t, delt, S0, LLG, parameters1, num)
    # S_solution05 = HeunSolver(t, delt, S0, LLG, parameters2, num)
    S_solutionTemp = HeunSolver(t, delt, S0, LLG, parameters, num)
    # print(S_solution)
    plotXYZ(S_solutionTemp,t)
    # subPlotXYZ(S_solution01, S_solution05, t)
    # animate(S_solution,t,num)

def testTenSpins():
    '''Simulate 10 spins'''
    t0 = 0 # start time
    tEnd = 10
    delt = 0.01
    timeSteps = int((tEnd-t0)/delt)
    print("timesteps: ", timeSteps)
    t = np.linspace(t0,tEnd,timeSteps)

    # Number of spins
    num = 10

    # Initilaization of spin in random directions
    S0 = initializeSpinRandomeDir(1, num)
    print("S0:")
    print(S0)
    # damping cases;
    alpha = 0.3

    # Defining the parameters parameters = [J, dz, kBT, muB, gamma, mu, alpha]
    kBT = 0; J = -10; B0 = 0; dz = 0.3*J; muB = mu*B0
    parameters = [J, dz, kBT, muB, gamma, mu, alpha]

    S_solution = HeunSolver(t, delt, S0, LLG, parameters, num)
    print("S solution:")
    print(S_solution[-1])
    plotXYZ(S_solution,t)
    # subPlotXYZ(S_solution01, S_solution05, t)

testTenSpins()