import os
import string

class BoardRenderer:
    board = None

    __alphabetUpper = list(string.ascii_uppercase)
    rowLetters = []
    columnLetters = []
    rowLettersInverted = []
    columnLettersInverted = []

    def __init__(self, board):
        self.board = board
        self.__SetLetters()

    def __SetLetters(self):
        for i in range(self.board.rowsCount - 1):
            self.rowLetters.append(self.__alphabetUpper[i])
        for i in range(self.board.columnsCount - 1):
            self.columnLetters.append(self.__alphabetUpper[i])

        self.rowLettersInverted = list(reversed(self.rowLetters))
        self.columnLettersInverted = list(reversed(self.columnLetters))

    def RenderCurrentBoard(self):
        self.__RenderBoard(self.board.visibleBoard)

    def RenderCompletedBoard(self):
        boardToRender = self.board.visibleBoard
        for x in range(self.board.rowsCount - 1):
            for y in range(self.board.columnsCount - 1):
                houseID = self.board.integerBoard[x][y]
                houseIcon = "[*]" if houseID == self.board.mineHouseID else "[#]"
                boardToRender[x][y] = houseIcon
        self.__RenderBoard(boardToRender)

    def __RenderBoard(self, boardToRender):
        self.ClearConsole()
        print("\n-------------------------------------\n")
        boardStr = ""
        for x in range(self.board.rowsCount - 1):
            boardStr += str(self.rowLettersInverted[x]) + " "
            for y in range(self.board.columnsCount - 1):
                boardStr += str(boardToRender[x][y]) + " "
            boardStr += "\n"
        for i in range(self.board.columnsCount - 1):
            boardStr += "   " + self.columnLetters[i]
        boardStr += "\n"
        print(boardStr)

    def ClearConsole(self):
        windows = "nt"
        os.system("cls" if os.name == windows else "clear")