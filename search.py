from moveGeneration import moveGeneration, notCheckIfBoardInCheck
from boardOperation import *
from evaluatePosition import evaluate


def maxi(color, piece, sideToMove, xSideToMove, move = None, depth = 0):
    moveToReturn = ""
    machineMove = None
    
    if move != None:
        color2, piece2 = generateBoard(color, piece, move)
    else:
        color2, piece2 = color.copy(), piece.copy()

    if depth == 0:
        return (evaluate(color2, piece2), "", 0)

    max = -900000000

    

    if move == None:
        enPassantSquare = -2
    else:
        enPassantSquare = move[2]

    moves = moveGeneration(color2, piece2, sideToMove, xSideToMove, enPassantSquare)
    if len(moves) == 0:
        if notCheckIfBoardInCheck(color2, piece2, sideToMove, xSideToMove):
            return (0, "", 0)
        else:
            return (-100000000, "", 0)
        
    for moveAfterGeneration in moves:
        score, returnedMove, notNeeded = mini(color2, piece2, xSideToMove, sideToMove, moveAfterGeneration, depth - 1)
        if score > max:
            max = score
            moveToReturn = getMove(moveAfterGeneration) + " " + returnedMove
            machineMove = moveAfterGeneration
            

    return (max, moveToReturn, machineMove)

def mini(colorGet, pieceGet, sideToMove, xSideToMove, move = None, depth = 0, firstCall = False):

    moveToReturn = ""
    machineMove = None

    if firstCall:
        color2, piece2 = colorGet.copy(), pieceGet.copy()
    else:
        color2, piece2 = generateBoard(colorGet, pieceGet, move)

    if depth == 0:
        return (evaluate(color2, piece2), "", 0)

    min = 900000000

    if firstCall:
        color2, piece2 = colorGet.copy(), pieceGet.copy()
    else:
        color2, piece2 = generateBoard(colorGet, pieceGet, move)


    if move == None:
        enPassantSquare = -2
    else:
        enPassantSquare = move[2]

    moves = moveGeneration(color2, piece2, sideToMove, xSideToMove, enPassantSquare)

    if len(moves) == 0:
        if notCheckIfBoardInCheck(color2, piece2, sideToMove, xSideToMove):
            return (0, "", 0)
        else:
            return (100000000, "", 0)

    for moveAfterGeneration in moves:
        score, returnedMove, notNeeded = maxi(color2, piece2, xSideToMove, sideToMove, moveAfterGeneration, depth - 1)
        if score < min:
            min = score
            moveToReturn = getMove(moveAfterGeneration) + " " + returnedMove
            machineMove = moveAfterGeneration
            

    return (min, moveToReturn, machineMove)