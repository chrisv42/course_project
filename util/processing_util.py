"""Helper utilities for functionalities related to processing information for the board or moves."""
import chess


def get_valid_moves(board):
    MOVES, CAPTURES = "moves", "captures"
    move_map = {MOVES: [], CAPTURES: []}
    legal_moves = board.legal_moves

    for move in legal_moves:
        if board.is_capture(move):
            move_map[CAPTURES].append(move)
        move_map[MOVES].append(move)

    return move_map[MOVES] if not move_map[CAPTURES] else move_map[CAPTURES]


def is_valid_move(move, board):
    return move in get_valid_moves(board)
