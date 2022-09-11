from DataTypes import *
from distutils.log import ERROR

class InputLetter:
    x = ""
    y = ""
    board = None

    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board

    def ToInt(self):
        typedCorrectly = (self.x.upper() in self.board.rowLetters and
                          self.y.upper() in self.board.columnLetters)
        if typedCorrectly:
            xInt = self.board.rowLettersInverted.index(self.x.upper())
            yInt = self.board.columnLetters.index(self.y.upper())
            return Vector2(xInt, yInt)
        else:
            return ERROR


class Input:
    def Get(self, initializer):
        textToShowInputY = initializer.traductor.GetText(
            "Insert the column: ", "Insira a coluna: ")
        textToShowInputX = initializer.traductor.GetText(
            "Insert the row: ", "Insira a linha: ")

        inputY = input(textToShowInputY)
        inputX = input(textToShowInputX)

        return InputLetter(inputX, inputY, initializer.board).ToInt()
