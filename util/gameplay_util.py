"""Helper utilities for functionalities related to gameplay"""

import random
import chess
from util.processing_util import get_valid_moves  # pylint: disable=import-error


def get_move_input(board):
    valid_moves = get_valid_moves(board)
    while True:
        move = input()
        try:
            move = chess.Move.from_uci(str(move))
            if move in valid_moves:
                return move
        except ValueError:
            pass

        print("\nInvalid move. Try again.")


def get_best_move(board, stockfish):
    stockfish.set_fen_position(board.fen())
    valid_moves = get_valid_moves(board)
    assesed = set()
    moves_to_produce = 1

    while True:
        top_moves = stockfish.get_top_moves(moves_to_produce)
        for move in top_moves:
            candidate_move = chess.Move.from_uci(move["Move"])
            if candidate_move not in assesed and candidate_move in valid_moves:
                return candidate_move
            assesed.add(candidate_move)

        moves_to_produce *= 2
