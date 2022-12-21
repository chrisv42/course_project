import chess
from stockfish import Stockfish
from util.gameplay_util import (  # pylint: disable=import-error
    get_best_move,
    get_move_input,
)

stockfish = Stockfish()
COLOUR_MAP = {0: "Black", 1: "White"}


def begin_game(argv):
    colour = chess.BLACK if argv[1] == "black" else chess.WHITE
    board = chess.Board()
    move = ""
    to_move = chess.WHITE
    game_in_session = True
    stockfish.set_depth(20)
    stockfish.set_skill_level(20)

    while game_in_session:
        if to_move == colour:
            move = get_best_move(board, stockfish)
            print(move)
        else:
            move = get_move_input(board)

        board.push(move)

        if board.is_fifty_moves() or board.can_claim_threefold_repetition():
            print(board.result(claim_draw=True))
            game_in_session = False
        elif board.is_game_over():
            print(board.result())
            game_in_session = False

        to_move = chess.BLACK if to_move == chess.WHITE else chess.WHITE
