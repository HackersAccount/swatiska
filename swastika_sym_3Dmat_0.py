
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to draw Swastika
def draw_swastika(ax, size):
    # Define Swastika pattern points
    x = [0, 0, size//2, size//2, 0, 0, -size//2, -size//2]
    y = [0, size//2, size//2, size, size, size//2, size//2, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0]

    # Plot Swastika
    ax.plot3D(x[:2], y[:2], z[:2], 'k')
    ax.plot3D(x[2:4], y[2:4], z[2:4], 'k')
    ax.plot3D(x[4:6], y[4:6], z[4:6], 'k')
    ax.plot3D(x[6:8], y[6:8], z[6:8], 'k')
    ax.plot3D(x[1:3], y[1:3], z[1:3], 'k')
    ax.plot3D(x[3:5], y[3:5], z[3:5], 'k')
    ax.plot3D(x[5:7], y[5:7], z[5:7], 'k')
    ax.plot3D(x[7:9], y[7:9], z[7:9], 'k')

# Function to draw 3D Swastika
def draw_3d_swastika(size):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Hide axes
    ax.axis('off')

    # Draw Swastika
    draw_swastika(ax, size)

    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])

    plt.show()

# Prompt user for size
size = int(input("Enter the size of the Swastika (odd number): "))

# Check if size is odd
if size % 2 == 0:
    print("Size must be an odd number.")
    exit(1)

# Draw 3D Swastika
draw_3d_swastika(size)

