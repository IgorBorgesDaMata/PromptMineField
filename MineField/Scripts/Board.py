from BoardRenderer import *
from BoardData import *


class Board(BoardData, BoardRenderer):
    initializer = None

    def __init__(self, boardRowsCount, boardColumnCount, initializer):
        self.initializer = initializer
        BoardData.__init__(self, boardRowsCount, boardColumnCount)
        BoardRenderer.__init__(self, self)

    def ShowHouse(self, input):
        if self.integerBoard[input.x][input.y] == self.mineHouseID:
            self.initializer.gameLogic.OnGameOver()
            return
        self.OnShowClearHouse(input)

    def OnShowClearHouse(self, input):
        if self.correctShows == 0:
            self.GenerateMines(input)

        if(self.integerBoard[input.x][input.y] == self.unshowedHouseID):
            self.correctShows += 1

            self.SetHouseInBoard(input)
            wonGame = self.correctShows == self.housesToShow
            if wonGame:
                self.initializer.gameLogic.OnGameWon()
                return

            bombsAround = self.GetBombsAround(Vector2(input.x, input.y))
            if len(bombsAround) == 0:
                self.ShowAroundHouses(input)

    def GenerateMines(self, firstMarkPos):
        for i in range(self.minesCount):
            minePos = Vector2(firstMarkPos.x, firstMarkPos.y)
            while self.AroundOfFirstMarked(minePos, firstMarkPos):
                x = random.randint(0, self.rowsCount - 1)
                y = random.randint(0, self.columnsCount - 1)
                minePos = Vector2(x, y)
            self.integerBoard[minePos.x][minePos.y] = 1

    def SetHouseInBoard(self, input):
        bombsAround = self.GetBombsAround(Vector2(input.x, input.y))
        houseIcon = "[#]" if len(bombsAround) == 0 else f"[{len(bombsAround)}]"

        self.visibleBoard[input.x][input.y] = houseIcon
        self.integerBoard[input.x][input.y] = self.clearHouseID

    def ShowAroundHouses(self, house):
        housesAround = self.GetAroundHousesOfType(Vector2(house.x, house.y),
                                                  self.unshowedHouseID)
        for aroundHouse in housesAround:
            self.ShowHouse(Vector2(aroundHouse.x, aroundHouse.y))


inst = None