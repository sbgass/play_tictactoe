You can play TicTacToe in the Terminal! Play two player or against a computer with difficulty Easy or Expert. Expert computer players use an optimized AI algorithm to do a complete search of the game tree. They can't be beat. Go ahead and try. 

All computer players are stochastic, so each game will be unique.

How to Run the Program: 

This program was written in python 3 and takes two input arguments to run. The game board prints to standard output with each move each turn. 
The inputs are the player types and can be any of the following: human, random, alphabeta. 

For example, running the following command from the program's directory will start a new game between a human player as player one and a alphabeta player as player two: 

"python3 tictactoe.py human alphabeta"

Player Options: 
"Human" - requires user input to play moves. 
"Random" - Easy computer players will play random moves in each turn. 
"Alphabeta" - Expert computer players use a the alphbeta pruning extension to the MiniMax algorithm to search to the end states of the game and choose the optimal move in each turn. 






