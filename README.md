# R3-SoftwareTraining#2-AnthonyPersaud
 Software Training Task

 ## General Info
 This project is an algorithm, written in python, which randomly generates a maze for a 2 motor rover to navigate through. The code uses the pygame library and its related functions to execute to building of the maze, along with base code blocks from python syntax.

 ## Technologies
 This project was created using a Python IDLE

 ## Progress
 The program shown utilizes a square grid of user-defined size, and implements the recursive backtracking algorithm to randomly choose an edge of the grid to begin forging a random path until an end to the maze is reached. The program is set to continuously create mazes of user-defined grid size until the user decides to terminate the program. This program is the foundation of the main goal, which is having the rover navigate through any of the generated mazes with ease.
 The getPath function in this program randomly selects a starting point to make a path. The lines making up the grid squares are removed after each iteration to continue forging a pathway. The path moves through adjacent cells in the grid only if they haven't been previously altered in other iterations of the function. In the event that the adjacent cells have all been affected, the iterations must continue from the last "untouched" grid cell. While the function runs in the main code, there is a continuous check for all the adjacent cells to determine where the path should continue from.
