import random

alphabetUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
alphabetUpperInverted = ["I", "H", "G", "F", "E", "D", "C", "B", "A"]
board = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
]

visibleBoard = [
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
]

minMinesCount = 10
maxMinesCount = 30
minesCount = random.randint(minMinesCount, maxMinesCount)
correctMarks = 0
language = 0


def SetLanguage():
    global language
    print("Insira o número da linguagem desejada (0 = inglês; 1 = português)")
    print("Insert the number of wished language (0 = english; 1 = portugues")
    languageInput = input()
    if languageInput.isnumeric() and (int(languageInput) == 0 or int(languageInput) == 1):
        language = int(languageInput)
    else:
        print("\nInsira um número válido...")
        print("Insert a valid number...")
        SetLanguage()


SetLanguage()


def ResetGame():
    global correctMarks
    a = input("Press enter to restart..." if language == 0 else "Aperte enter para recomeçar...")
    for x in range(9):
        for y in range(9):
            board[x][y] = -1
            visibleBoard[x][y] = "[ ]"
    minesCount = random.randint(minMinesCount, maxMinesCount)
    correctMarks = 0
    GetInput(False)


def GenerateMines(firstDigX, firstDigY):
    for i in range(minesCount):
        x = firstDigX
        y = firstDigY
        while abs(x - firstDigX) <= 1 or abs(y - firstDigY) <= 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        board[x][y] = 1


def MarkBoard(x, y):
    global correctMarks
    if board[x][y] == 1:
        visibleBoard[x][y] = "[*]"
        RenderCompletedBoard()
        print("Game over!" if language == 0 else "Você perdeu!")
        ResetGame()
    else:
        if correctMarks == 0:
            GenerateMines(x, y);
        correctMarks += 1
        board[x][y] = 2
        bombsAround = 0
        for aroundX in range(3):
            for aroundY in range(3):
                xValue = x + aroundX - 1
                yValue = y + aroundY - 1
                if xValue >= 0 and xValue < 9 and yValue >= 0 and yValue < 9:
                    if board[x + aroundX - 1][y + aroundY - 1] == 1:
                        bombsAround += 1
        visibleBoard[x][y] = "[#]" if bombsAround == 0 else f"[{bombsAround}]"
        if bombsAround == 0:
            for aroundX in range(3):
                for aroundY in range(3):
                    xValue = x + aroundX - 1
                    yValue = y + aroundY - 1

                    if xValue >= 0 and xValue < 9 and yValue >= 0 and yValue < 9:
                        if board[xValue][yValue] != 2:
                            MarkBoard(xValue, yValue)
        if correctMarks == 81 - minesCount:
            RenderCompletedBoard()
            print("Game won!" if language == 0 else "Jogo vencido!")
            ResetGame()


def RenderBoard():
    print("\n-------------------------------------")
    boardStr = "\n"
    for x in range(9):
        boardStr += str(alphabetUpperInverted[x]) + " "
        for y in range(9):
            boardStr += str(visibleBoard[x][y]) + " "
        boardStr += "\n"
    boardStr += "   A   B   C   D   E   F   G   H   I"
    boardStr += "\n"
    print(boardStr)


def RenderCompletedBoard():
    print("\n-------------------------------------")
    boardStr = "\n"
    for x in range(9):
        boardStr += str(alphabetUpperInverted[x]) + " "
        for y in range(9):
            if board[x][y] == 1:
                boardStr += "[*]"
            else:
                boardStr += "[#]"
            boardStr += " "
        boardStr += "\n"
    boardStr += "   A   B   C   D   E   F   G   H   I"
    boardStr += "\n"
    print(boardStr)


def GetInput(stoppedInExcept):
    RenderBoard()
    if stoppedInExcept == True:
        if language == 0:
            print("Insert just one letter between A and I, without spaces")
        else:
            print("Insira apenas uma letra de A até I, sem espaços ou acentos")
    playerInputY = input("Insert the column: " if language == 0 else "Insira a coluna: ")
    playerInputX = input("Insert the line: " if language == 0 else "Insira a linha: ")
    if playerInputX.upper() in alphabetUpper and playerInputY.upper() in alphabetUpper:
        playerInputX = (alphabetUpperInverted.index(playerInputX.upper()))
        playerInputY = (alphabetUpper.index(playerInputY.upper()))
        MarkBoard(playerInputX, playerInputY)
        GetInput(False)
    else:
        GetInput(True)


GetInput(False)