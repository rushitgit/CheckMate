
import board_toSVG as bsvg
from chess import Board
import sys
import chess
import os
import time 

for i in range(1,5):
    file_path = f'chess_board_{i}.svg'
    try:
        os.remove(file_path)
        print(f'Removed: {file_path}')
    except FileNotFoundError:
        pass
        # print(f'File not found: {file_path}')

def move_generator(move):
    the_best_move= chess.Move.from_uci(move)
    return the_best_move
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        value = -float('inf')
        for move in legal_moves:
            board.push(move)
            value = max(value, minimax_alpha_beta(board, depth - 1, alpha, beta, False))
            board.pop()
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Alpha cutoff (pruning)
        return value
    else:
        value = float('inf')
        for move in legal_moves:
            board.push(move)
            value = min(value, minimax_alpha_beta(board, depth - 1, alpha, beta, True))
            board.pop()
            beta = min(beta, value)
            if beta <= alpha:
                break  # Beta cutoff
        return value
    
def evaluate_board(board):
   
    if board.is_checkmate():
       
        return -9999 if board.turn else 9999
    elif board.is_stalemate() or board.is_insufficient_material():
        # Drawn game situations
        return 0
    else:
        return 0
    

def find_best_move(board, depth):
    legal_moves = list(board.legal_moves)
    best_move = None
    best_value = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    for move in legal_moves:
        board.push(move)
        value = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
        board.pop()

        if value > best_value:
            best_value = value
            best_move = move

    return best_move

#  sample FENs
# 'k7/7R/2K5/8/8/8/8/8 w - - 0 1'
# 'k7/7R/8/1K6/8/8/8/8 w - - 0 1'
# 'k7/7R/8/K7/8/8/8/8 w - - 0 1'
# '1k1K4/7R/8/8/3N4/8/8/8 w - - 0 1'
# 'k7/5b2/7R/1K6/1P6/6BP/2P5/8 w - - 0 1' null 


starting_fen='1k1K4/p6R/1p4p1/5b2/3N4/1P6/P7/8 w - - 0 1'


board = Board(starting_fen)
print('initial position, AI to move')

bsvg.save_board_svg(board, 'chess_board_1.svg')
print(board)

time.sleep(5) 

ctr=2 # counter for svg files
max_moves = 6
move_count = 0
depth=3     # depth of the minimax algorithm
while not board.is_checkmate() and move_count < max_moves:
    print("AI is thinking...")
    ai_move = find_best_move(board, depth)  # Adjust the depth as needed
    print("AI's move:", ai_move.uci())
    board.push(ai_move)   
    print(board)
    time.sleep(1)
    bsvg.save_board_svg(board, f'chess_board_{ctr}.svg')
    
    ctr+=1
    if(board.is_checkmate()):
        break
    
    legal_moves = list(board.legal_moves)
    print(legal_moves)
    user_move = input("User, please enter your SAN move from interpreting the legal options:\n")
    # if user_move not in [move.uci() for move in legal_moves]:
    #     print("Invalid move. Please choose a legal move.")
    #     continue

    board.push_san(user_move)
    print(board)
    bsvg.save_board_svg(board, f'chess_board_{ctr}.svg')
    ctr+=1

    move_count += 2  # Assuming both AI and user make one move each in each iteration
    depth=depth-1
    
print("Game Over.")
if board.is_checkmate():
    print("Checkmate!")
elif move_count >= max_moves:
    print("Maximum moves reached.")
else:
    print("Unknown condition.")