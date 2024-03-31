def draw_swastika(size):
    # Define a 2D list to represent the grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Calculate the center index
    center = size // 2

    # Draw horizontal line
    for i in range(size):
        grid[center][i] = '*'

    # Draw vertical line
    for i in range(size):
        grid[i][center] = '*'

    # Draw upper-left quadrant
    for i in range(center):
        grid[i][1] = '*'
        grid[0][i] = '*'

    # Draw lower-left quadrant
    for i in range(center + 1, size):
        grid[i][1] = '*'
        grid[size - 1][i - center] = '*'

    # Draw upper-right quadrant
    for i in range(center):
        grid[i][size - 2] = '*'
        grid[0][center + i + 1] = '*'

    # Draw lower-right quadrant
    for i in range(center + 1, size):
        grid[i][size - 2] = '*'
        grid[size - 1][i] = '*'

    # Print the grid
    for row in grid:
        print(' '.join(row))

# Prompt user for size
size = int(input("Enter the size of the Swastika (odd number): "))

# Check if size is odd
if size % 2 == 0:
    print("Size must be an odd number.")
    exit(1)

# Draw Swastika
draw_swastika(size)
