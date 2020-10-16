# PyCrossNought
![banner](https://papergames.io/images/tic-tac-toe/thumbnail.png)


Tic Tac Toe Python Bot

## Features:
- This Python Script uses naive algorithms to maximise winning probability for player 1
- After every move it asks user to input a integer between 1 and 9 (to mark your move)
- After the game concludes (Victory, Defeat, Tie) A message would be displayed

## Requirements:
- [Python3](https://www.python.org/downloads/)
- [PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=windows)

## Game Play:
-   Run [PyCrossNought.py](PyCrossNought.py):
    ```bash
    python PyCrossNought.py
    ```
-  Computer always plays first (In one of the 4 corner blocks)
-  Input any number from (1 to 9) indicating the position on the board where you want to mark 'O'
-  After your move the board is updated with your current move and computer's move


## Probability Calculation:
- The winning probability of algorithm is 91.20%
- The probability is calculated assuming that player 2 enters random moves.

## Explination
- The main program considers all possible cases to ensure victory
### print_board()
- This functions thakes the current values of the board and prints the board in given format when called

### tie_algorithm()
- When there is no more chances of forming a definite winning combination
then tie_algorithm is called
- The tie algorithm just focuses on the list with the priority as follows::

   1) completing 3 'X' row
   2) completing 3 'X' column
   3) completing 3 'X' diagonal

   4) blocking 3 'O' row
   5) blocking 3 'O' column
   6) blocking 3 'O' diagonal
 
 ### ask_to_play()
 - Asks user to input his next move
 

 ## To Do :
 - PyGame Based Ui for the game
 - Maximing winning Probability for Player 2
