import chess
import chess.svg

def save_board_svg(board, file_path):
    svg_content = chess.svg.board(board=board)
    
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)

# Example usage:
# fen_notation = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# board = chess.Board(fen=fen_notation)

# Save the SVG content to a file
    # save_board_svg(board, "chess_board.svg")