import numpy as np
from eqs import randomMatrix, thermalConstant, normalizeMat

# Define the Heun solver algorithm for vectors
def HeunSolver(t, delt, S0, f, parameters, num):
    ''' Heun Solver for 2D chain
        - t: time array for to run the Haun Solver over
        - delt: time step size
        - S0: inital state of the spins
        - f; function for the right hand side of the differential equaion
        - parameters; chosen values of the parameters used in the LLG equation
        - num; number of spins in the chain
    '''
    timeSteps = len(t)

    S = np.zeros((timeSteps,num,3)) # 3D array;
                                    # timesteps number of matrices, where each vector in the matrix
                                    # is a spin vector of 3 dimensions
    if (num == 1): S[0][0] = S0
    else: S[0] = S0

    Fp = np.empty((num,3))
    F1 = np.empty((num,3))
    
    xi = thermalConstant(delt, parameters)*randomMatrix(timeSteps,num) # random vector matrix used for random thermal constant, one for each spin for each timestep
    

    for i in range(1, timeSteps):
        # Sp = S[i-1] + delt*f(S[i-1], delt, parameters, xi[i]) # denne vektoren har høy verdi
        # temp = S[i-1] + 0.5*delt*(f(S[i-1],delt,parameters,xi[i]) + f(Sp,delt,parameters,xi[i]))

        # S[i] = normalizeMat(temp)

        F1 = f(S[i-1], delt, parameters, xi[i])
        Fp = f(S[i-1] + delt*F1,delt,parameters,xi[i])
        S[i] = S[i-1] + 0.5*delt*(F1 + Fp)
        temp = S[i-1] + 0.5*delt*(F1 + Fp)
        S[i] = normalizeMat(temp)
        if(i%10 == 0): print(i, "- norm:",np.linalg.norm(S[i][0])) 
    
    return S


# -------------- INITIALIZATION -------------- #
# Initialize a tilted spin
def initializeOneTiltedSpin():
    S0x = 0.1 # hva skal jeg sette disse til?
    S0y = 0.2
    S0 = np.array([S0x,S0y,np.sqrt(1-S0x**2-S0y**2)]) # initial spin
    return S0

# Initialize FM ground state, one tilted
def initializeSpinGroundStateWave(N):
    S0 = np.zeros((N,3))
    mid = int(N/2) # the mid election
    S0[:,2] = 1 # All spins are (0,0,1)
    S0[mid] = initializeOneTiltedSpin() # mid spin tiled
    return S0

# Initilizes spins in random directions for testing sovler
def initializeSpinRandomeDir(S_amp, N):
    S0 = np.zeros((N,3))
    for i in range(N):
        theta = np.random.uniform(0,2*np.pi)
        phi = np.random.uniform(0,2*np.pi)
        S0[i] = S_amp*np.array([np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])
    return S0
