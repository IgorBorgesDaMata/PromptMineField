from Traductor import *
from GameLogic import *
from Board import *


class Initializer:
    boardRows = 10
    boardColumns = 10
    traductor = None

    def StartGame(self):
        self.__CreateObjects()

        self.traductor.GetLanguageInput()

        self.gameLogic.NewTurn()

    def __CreateObjects(self):
        self.board = Board(self.boardRows, self.boardColumns, self)
        self.gameLogic = GameLogic(self)
        self.traductor = Traductor()

    def RestartMatch(self):
        textToShow = self.traductor.GetText("Press enter to restart...",
                                            "Aperte enter para recomecar...")
        input(textToShow)
        self.__ResetBoard()
        self.gameLogic.NewTurn()

    def __ResetBoard(self):
        for x in range(self.board.rowsCount):
            for y in range(self.board.columnsCount):
                self.board.integerBoard[x][y] = self.board.unshowedHouseID
                self.board.visibleBoard[x][y] = self.board.defaultHouseIcon
        self.board.correctShows = 0
        self.board.SetMatchValues()


_initializer = Initializer()
_initializer.StartGame()
