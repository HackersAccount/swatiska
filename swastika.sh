#!/bin/bash

# Function to draw Swastika
draw_swastika() {
    local size=$1
    local half=$((size / 2))

    # Loop through rows
    for ((i = 1; i <= size; i++)); do
        # Loop through columns
        for ((j = 1; j <= size; j++)); do
            # Check if it's in the middle or at the edges
            if ((i == half || j == half || (i == 1 && j > half) || (i == size && j <= half) || (j == 1 && i <= half) || (j == size && i > half))); then
                echo -n "* "
            else
                echo -n "  "
            fi
        done
        echo
    done
}

# Prompt user for size
read -p "Enter the size of the Swastika (odd number): " size

# Check if size is odd
if ((size % 2 == 0)); then
    echo "Size must be an odd number."
    exit 1
fi

# Draw Swastika
draw_swastika $size
