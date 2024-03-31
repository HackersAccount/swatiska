#!/bin/bash

# Function to draw Swastika
draw_swastika() {
    local size=$1

    # Draw Swastika
    for ((i = 1; i <= size; i++)); do
        for ((j = 1; j <= size; j++)); do
            if ((i == size / 2 + 1)); then
                echo -n "* "
            elif ((j == size / 2 + 1)); then
                echo -n "* "
            elif ((i < size / 2 + 1 && j == 1)); then
                echo -n "* "
            elif ((i > size / 2 + 1 && j == size)); then
                echo -n "* "
            elif ((i == 1 && j > size / 2 + 1)); then
                echo -n "* "
            elif ((i == size && j < size / 2 + 1)); then
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
