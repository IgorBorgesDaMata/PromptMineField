import numpy as np
import random
from BoardRenderer import *
from DataTypes import *


class BoardData:
    rowsCount = 10
    columnsCount = 10
    totalSize = 0
    housesToShow = 0

    minMinesCount = 15
    maxMinesCount = 35
    minesCount = 0
    correctShows = 0

    unshowedHouseID, mineHouseID, clearHouseID = (-1, 1, 2)
    defaultHouseIcon = "[ ]"

    integerBoard = None
    visibleBoard = None

    def __init__(self, boardRowsCount, boardColumnCount):
        self.rowsCount = boardRowsCount
        self.columnsCount = boardColumnCount
        self.totalSize = self.rowsCount * self.columnsCount
        self.__SetBoards()
        self.SetMatchValues()

    def __SetBoards(self):
        self.integerBoard = np.array([[-1] * self.rowsCount] *
                                     self.columnsCount)
        self.visibleBoard = np.array([["[ ]"] * self.rowsCount] *
                                     self.columnsCount)

    def SetMatchValues(self):
        self.__SetMinesCount(self.minMinesCount, self.maxMinesCount)
        self.housesToShow = self.totalSize - self.minesCount

    def __SetMinesCount(self, minMinesCount, maxMinesCount):
        self.minesCount = random.randint(minMinesCount, maxMinesCount)

    def GetAroundHousesOfType(self, house, houseType):
        housesAround = []
        for aroundX in range(3):
            for aroundY in range(3):
                xValue = house.x + aroundX - 1
                yValue = house.y + aroundY - 1

                valuesAreInsideBoard = xValue >= 0 and xValue < 9 and yValue >= 0 and yValue < 9
                if valuesAreInsideBoard:
                    if self.integerBoard[xValue][yValue] == houseType:
                        housesAround.append(Vector2(xValue, yValue))
        return housesAround

    def GetBombsAround(self, house):
        return self.GetAroundHousesOfType(Vector2(house.x, house.y),
                                          self.mineHouseID)

    def AroundOfFirstMarked(self, minePos, firstMarkPos):
        return (abs(minePos.x - firstMarkPos.x) <= 1
                or abs(minePos.y - firstMarkPos.y) <= 1)