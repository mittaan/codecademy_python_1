#!/usr/bin/env python3

from libs import Board, Path
import random as rn

if __name__ == '__main__':
    width = 10
    height = 10
    path = Path(width, height)
    board = Board(width, height, path)
    board.print_board()
    tries = 3
    
    path_level = 0
    
    print(f'Find the path! Insert a number between 0 and {width}:')

    while tries > 0:
        user_input = input()
        if not(user_input in [str(i) for i in range(width)]):
            print('Not a valid input, try again!')
            continue
        user_number = int(user_input)
        coords = f'{user_number},{path_level}'
        board.update_visual(user_number, path_level)
        if board.has_matched(coords):
            if path_level == height:
                break
            print('Correct! Keep going...')
            path_level += 1
        else:
            print('Nope, try again.')
            tries -= 1
        
    if path_level == height:
        print('Congratulations! You won the game :)')
    else:
        print('Game over. Better luck next time.')
