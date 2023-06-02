import numpy as np

# Unit vector in z direction
ez = np.array([0,0,1])

def normalizeVec(S):
    '''Normalizes a given vector S '''
    if (np.sqrt(np.sum(S**2)) == 0 ):
        return np.zeros(len(S))
    return S/(np.sqrt(np.sum(S**2)))

def normalizeMat(S):
    ''' Normalizes all the spin vectors in one timestep matrix'''
    r = np.zeros((len(S),len(S[0])))
    for i in range(len(S)):
        r[i] = normalizeVec(S[i])
    return r

def randomMatrix(timeSteps, num):
    ''' Generates a random matrix of size timeSteps x num'''
    x = np.empty((timeSteps,num,3))
    for i in range(timeSteps):
        for j in range(num):
            x[i][j] = randomVec()
    return x

def random5DParam(N):
    ''' Creates a 5D parameter with random values '''
    x = np.empty((N,N,N,3))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                x[i][j][k] = randomVec()
    return x

def randomVec():
    ''' Creates a vector with random numbers with a mean of 0 and a deviation of 1'''
    a = np.random.normal()
    b = np.random.normal()
    c = np.random.normal()
    return normalizeVec(np.array([a,b,c]))

def thermalConstant(delt,parameters):
    ''' Calculates the thermal constant for simlation
        This reamains the same throughout the simultaion
    '''
    J, dz, kBT, muB, gamma, mu, alpha = parameters
    return np.sqrt((2*alpha*kBT)/(gamma*mu*delt))

def LLG(S, delt, parameters, xi):
    ''' Landau-Lifshitz-Gilbert equation:
    Left hand side in the differential equation describing the motion
    of the spins of the atoms.
    
    - S; N*3 matrix, one timestep of the spin
    - delt; stepsize in time
    - parameters = [J, dz, kBT, muB, gamma, mu, alpha]
    - xi; the thermal noise
    '''
    J, dz, kBT, muB, gamma, mu, alpha = parameters

    N = len(S) # number of particles
    f = np.zeros((N,3)) # tror ikke det går fortere med denne npr det ikke er for loop

    if N == 1:
        Hmat = np.copy(xi)
    else:
        Hmat = 1/mu * (J*(np.roll(S,-1,axis=0) + np.roll(S,1,axis=0))) + xi

    Hmat[:,2] += 1/mu * (2*dz*S[:,2] + muB)
    f = -gamma/(1+alpha**2) * (np.cross(S, Hmat) + np.cross(alpha*S, np.cross(S, Hmat))) 
    f = normalizeMat(f) # kan evt skrive om denne til call by ret

    return f