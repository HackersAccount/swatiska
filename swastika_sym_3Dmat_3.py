import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to draw Swastika
def draw_swastika(ax, size, position):
    # Define Swastika pattern points
    x = [0, 0, size//2, size//2]
    y = [0, size//2, size//2, size]
    z = [0, 0, 0, 0]
    
    # Shift the Swastika to the desired position
    x = [val + position[0] for val in x]
    y = [val + position[1] for val in y]
    z = [val + position[2] for val in z]
    
    # Plot Swastika
    ax.plot3D(x, y, z, 'k')

# Function to draw 3D Swastika
def draw_3d_swastika(size):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Hide axes
    ax.axis('off')
    
    # Draw front face
    draw_swastika(ax, size, [0, 0, 0])
    
    # Draw top face
    draw_swastika(ax, size, [0, size//2, 0])
    
    # Draw right face
    ax.view_init(elev=0, azim=-90)
    draw_swastika(ax, size, [size//2, 0, 0])
    
    # Draw left face
    ax.view_init(elev=0, azim=90)
    draw_swastika(ax, size, [-size//2, 0, 0])
    
    # Draw back face
    ax.view_init(elev=180, azim=0)
    draw_swastika(ax, size, [0, 0, -size//2])
    
    # Draw bottom face
    ax.view_init(elev=90, azim=0)
    draw_swastika(ax, size, [0, -size//2, 0])
    
    # Hide grids
    ax.grid(False)
    
    plt.show()

# Prompt user for size
size = int(input("Enter the size of the Swastika (odd number): "))

# Check if size is odd
if size % 2 == 0:
    print("Size must be an odd number.")
    exit(1)

# Draw 3D Swastika
draw_3d_swastika(size)
