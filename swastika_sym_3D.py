# Function to draw Swastika
def draw_swastika(size):
    # Draw Swastika
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i == size // 2 + 1:
                print("* ", end="")
            elif j == size // 2 + 1:
                print("* ", end="")
            elif i < size // 2 + 1 and j == 1:
                print("* ", end="")
            elif i > size // 2 + 1 and j == size:
                print("* ", end="")
            elif i == 1 and j > size // 2 + 1:
                print("* ", end="")
            elif i == size and j < size // 2 + 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

# Function to draw 3D Swastika
def draw_3d_swastika(size):
    # Draw front face
    draw_swastika(size)
    print()
    
    # Draw top face
    for _ in range(size):
        print(" " * (size * 2) + "* " * size)
    
    print()
    
    # Draw back face
    draw_swastika(size)
    print()
    
    # Draw bottom face
    for _ in range(size):
        print(" " * (size * 2) + "* " * size)

# Prompt user for size
size = int(input("Enter the size of the Swastika (odd number): "))

# Check if size is odd
if size % 2 == 0:
    print("Size must be an odd number.")
    exit(1)

# Draw 3D Swastika
draw_3d_swastika(size)
