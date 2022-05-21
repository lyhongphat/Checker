import pygame
from copy import deepcopy
from numpy import Infinity

from CHECKER.const import BLACK, WHITE

def findTheWay(state, depth_limit, max_player, myGame):
    if depth_limit <= 0 \
            or myGame.winner():
        return state.score(), state
    
    if max_player:
        maxEval = -Infinity
        best_move = None
        for move in get_all_moves(myGame, state, WHITE):
            score = findTheWay(move, depth_limit - 1, False, myGame)[0]
            maxEval = max(maxEval, score)
            if maxEval == score:
                best_move = move
        return maxEval, best_move

    else:
        minEval = Infinity
        best_move = None
        for move in get_all_moves(myGame, state, BLACK):
            evaluation = findTheWay(move, depth_limit - 1, True, myGame)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

def get_all_moves(myGame, thisBoard, color):
    moves = []
    for piece in thisBoard.get_all_pieces(color):
        valid_moves = thisBoard.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(thisBoard)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, myGame, skip)
            moves.append(new_board)
    return moves

def simulate_move(piece, move, board, myGame, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board