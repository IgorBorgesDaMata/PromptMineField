from distutils.log import ERROR
import Board
from Input import *

class GameLogic:
    initializer = None

    def __init__(self, initializer):
        self.initializer = initializer

    def NewTurn(self):
        self.initializer.board.RenderCurrentBoard()

        input = self.__GetInput()
        if self.initializer.board.correctShows == 0:
            self.initializer.board.GenerateMines(input)
        self.initializer.board.ShowHouse(input)
        self.NewTurn()

    def __GetInput(self):
        inputManager = Input()
        input = inputManager.Get(self.initializer)

        happenedTypeError = input == ERROR
        if happenedTypeError:
            self.__OnTypeWithError()
            return self.__GetInput()
        return input

    def __OnTypeWithError(self):
        textToShowExcept = self.initializer.traductor.GetText(
            "Insert just one letter between A and I, without spaces ",
            "Insira apenas uma letra de A atÃ© I, sem espaÃ§os ou acentos")        
        print(textToShowExcept)

    def ShowHouse(self, inputs):
        self.__happenedTypeError = inputs == ERROR
        if not self.__happenedTypeError:
            self.initializer.board.ShowHouse(inputs)

    def OnGameOver(self):
        gameOverMessage = self.initializer.traductor.GetText("Game over!", "Você perdeu!")
        self.__OnMatchEnd(gameOverMessage)

    def OnGameWon(self):
        wonMessage = self.initializer.traductor.GetText("Game won!", "Jogo vencido!")
        self.__OnMatchEnd(wonMessage)

    def __OnMatchEnd(self, endMessage):
        self.initializer.board.RenderCompletedBoard()
        print(endMessage)
        self.initializer.RestartMatch()