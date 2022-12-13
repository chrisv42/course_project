# Usage

* Set the execution permissions by running `chmod 777 stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2.exe`
* Run the script with `python3 main.py white` or `python3 main.py black`. The colour specified is the colour the program will play as. Inputs will be playing as the opposite colour.

# References

* This program uses [`python-chess`](https://python-chess.readthedocs.io/en/latest/) for the chess interface
* This program uses [`stockfish`](https://pypi.org/project/stockfish/) for move decision making