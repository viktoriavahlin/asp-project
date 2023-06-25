import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

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

# Animation of the spins
def animate(S,t,N):
    delx = 2/N
    def update(i):
        # Clear the previous plot and plot the new spin vector
        ax.clear()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        for j in range(N):
            ax.quiver(-1+j*delx, 0, 0, S[i,j,0], S[i,j,1], S[i,j,2], length=0.5, normalize=True)
        ax.set_title('Time = {:.2f}'.format(t[i]))

    # Create the 3D plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca(projection='3d')

    # Create the animation
    anim = FuncAnimation(fig, update, frames=range(len(t)), interval=50)

    # Show the animation
    plt.show()
