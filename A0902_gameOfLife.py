# Name: Akshat Gaur
# Student ID: 2176685
# Date :11/17/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/fo8iCVHruNs

import numpy as np
import random

def conway(s, p=0.1):
    """
    Generates a conway board and fills it with random values based on probablity
    Returns the board
    """
    
    print("Size:", s)
    board = np.zeros((s, s), dtype=int)         # Create an empty s x s NumPy array
    
    # Populate the board randomly with probability p
    for i in range(s):
        for j in range(s):
            if random.random() < p:             
                board[i, j] = 1

    return board

def count_neighbors(board, i, j):
    """
    Counts the number of live neighbors for a given cell.
    Returns the sum of live neighbors.
    """
    # Calculate the indices of the cell's neighbors, considering Torus Topology
    size = len(board)
    neighbors = [
        board[(i-1) % size, (j-1) % size], board[(i-1) % size, j], board[(i-1) % size, (j+1) % size],
        board[i, (j-1) % size], board[i, (j+1) % size],
        board[(i+1) % size, (j-1) % size], board[(i+1) % size, j], board[(i+1) % size, (j+1) % size]
    ]
    return sum(neighbors)

def advance(board, t=1, display=True):
    """
    Advances the Conway board through a specified number of time steps.
    Returns board after t steps
    """
    s = board.shape[0]                                      # Size of the board
    for _ in range(t):
        new_board = np.copy(board)                          # Create a copy of the board for the next generation
        for i in range(s):
            for j in range(s):
                neighbors = count_neighbors(board, i, j)    # Counting neighbors for each cell

                if board[i, j] == 1:                        # Apply the Conway's Game of Life rules
                    if neighbors < 2 or neighbors > 3:
                        new_board[i, j] = 0
                elif board[i, j] == 0:
                    if neighbors == 3:
                        new_board[i, j] = 1

        board = new_board                                   # Update board with next generation

        if display:
            display_board(board)                            # Display board after each step

        if np.all(board == 0):                              # Check if all board elements are 0
            print("All cells are dead. Game over.")
            return board                                    # Stop the game

    return board

def display_board(board):
    """
    Display the board
    """
    s = board.shape[0]
    for i in range(s):
        row = ''.join([str(cell) for cell in board[i]])     # Converts each cell value to string
        print(row)
    print("\n")

# Different Cases
print("Case 1\n")
s1 = 5
p1 = 0.2
t1 = 5

board = conway(s1, p1)
print("Initial state:")
display_board(board)

print(f"Advancing state for {t1} steps:")
board = advance(board, t1)

print("Case 2\n")
s2 = 6
p2 = 0.8
t2 = 3

board = conway(s2, p2)
print("Initial state:")
display_board(board)

print(f"Advancing state for {t2} steps:")
board = advance(board, t2)

print("Case 3\n")
s3 = 7
p3 = 0.6
t3 = 4

board = conway(s3, p3)
print("Initial state:")
display_board(board)

print(f"Advancing state for {t3} steps:")
board = advance(board, t3)