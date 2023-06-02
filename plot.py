import matplotlib.pyplot as plt
import numpy as np

# Plot the change of the x, y and z components of S
def plotXYZ(S,t):
    plt.figure()
    plt.title("Components of the spin vector")
    plt.plot(t,S[:,0,0],'seagreen', label = "Sx")
    plt.plot(t,S[:,0,1],'mediumaquamarine', label = "Sy")
    plt.plot(t,S[:,0,2],'r', label = "Sz")
    for i in range(1,len(S[0])):
        plt.plot(t,S[:,i,0],'seagreen') #, label = "Sx")
        plt.plot(t,S[:,i,1],'mediumaquamarine') #, label = "Sy")
        plt.plot(t,S[:,i,2],'r') #, label = "Sz")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Magnitude")
    plt.show()
