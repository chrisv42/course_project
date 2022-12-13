import chess
from stockfish import Stockfish
from util.gameplay_util import (  # pylint: disable=import-error
    get_best_move,
    get_move_input,
)

stockfish = Stockfish(
    "stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe"
)
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
        else:
            move = get_move_input(board)

        board.push(move)

        print(f"{COLOUR_MAP[to_move]} makes move {move}.\n")
        print(f"{board}\n")

        if board.is_fifty_moves() or board.can_claim_threefold_repetition():
            print(board.result(claim_draw=True))
            game_in_session = False
        elif board.is_game_over():
            print(board.result())
            game_in_session = False

        to_move = chess.BLACK if to_move == chess.WHITE else chess.WHITE
