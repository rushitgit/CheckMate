import os

for i in range(1,5):
    file_path = f'chess_board_{i}.svg'
    try:
        os.remove(file_path)
        print(f'Removed: {file_path}')
    except FileNotFoundError:
        pass
        # print(f'File not found: {file_path}')
