# MineField
That project it is a Minefield game in prompt, using Python 3 as programming language. To naming convention, it's used PascalCase for class and files names, and camelCase for anything else.


*How to run the game
To game runs, the file Initializer.py must be the first code to run

*Initializer:
File that starts the game (creating the objects of main classes), and starts the matches.

*Board
The code Board.py have some functions of board (like show a house), and inherites the codes BoardData.py (which have some datas like the size of board and mines count), and BoardRenderer.py (which have the renderer functions of board).

*DataTypes
This file have classes used as DataTypes. Fow now, it have only one class: Vector2, which works as a cartesian point.

*Traductor
File used to set the game language and return the texts in the chosen language.

*Input
File that get the inputs of player in game (the column and row position). Besides, this file converts the letter inputs (Like A, B, C...) to number inputs (Like 0, 1, 2...), returning a Vector2 value using the numbers (the column number is X axis, and the row number is the Y axis).

*Game Logic
File that commands the turn logic (calling the Input methods), the game won logic, and the game over logic.

Credits:
Igor B. da Mata