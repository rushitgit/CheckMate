from chess import Board
import os
import chess.svg

def save_board_svg(board, file_path):
    svg_content = chess.svg.board(board=board)
    
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)


starting_fen= '8/8/8/3k4/4K3/8/8/8 w - - 0 1'




# Create the initial board
board = Board(starting_fen)


save_board_svg(board, "chess_board_1.svg")