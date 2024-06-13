from chess import Board



starting_fen = '2r3k1/p4p2/3Rp2p/1p2P1pK/8/1P4P1/P3Q2P/1q6 b - - 0 1'
board=Board(starting_fen)
print(board)

while(board.is_checkmate):
    print(board.legal_moves)
    opponent_move_uci = input("play your move at this position \n")
    board.push_san(opponent_move_uci)

    
    print(board)


