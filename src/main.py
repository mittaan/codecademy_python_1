#!/usr/bin/env python3

from libs import Board, Path

def choose_difficulty(difficulty_index: str) -> str:
    match difficulty_index:
        case '1':
            return 'EASY'
        case '2':
            return 'MEDIUM'
        case '3':
            return 'HARD'
        case '-1':
            return 'IRON'
        case '42':
            return 'YOU WIN'
        case _:
            return 'Invalid input.'

def set_parameters(difficulty: str) -> tuple:
    match difficulty:
        case 'EASY':
            return (4, 4, 8)
        case 'MEDIUM':
            return (6, 4, 5)
        case 'HARD':
            return (8, 5, 3)
        case 'IRON':
            return (4, 4, 1)

def start_game(difficulty: str) -> None:
    # Parameters used to set the layout for the game
    width, height, tries = set_parameters(difficulty)
    path_level = 0

    # Initialising the classes imported from libs.py
    path = Path(width, height)
    board = Board(width, height, path)

    board.print_board()
    
    print(f'\nFind the hidden path! Insert a number between 0 and {width - 1}:')

    while tries > 0:

        user_input = input()

        if not(user_input in [str(i) for i in range(width)]):
            print('Not a valid input, try again!')
            continue

        user_number = int(user_input)

        coords = f'{user_number},{path_level}'

        board.update_visual(user_number, path_level)

        if board.has_matched(coords):
            path_level += 1
            if path_level == height:
                break
            print('\nCorrect! Keep going...')
        else:
            tries -= 1
            print(f'\nNope, try again. You have {tries} tries left.')
        
    if path_level == height:
        print('\nCongratulations! You won the game :)')
    else:
        print('\nGame over. Better luck next time.')


if __name__ == '__main__':

    print('Choose the difficulty:')
    print('EASY        [type "1"]')
    print('MEDIUM      [type "2"]')
    print('HARD        [type "3"]\n')

    difficulty_index = input()

    difficulty = choose_difficulty(difficulty_index)
    valid_modes = ['-1', '1', '2', '3']

    if not(difficulty_index in valid_modes):
        print(difficulty)
    else:
        print(f'You chose to play the {difficulty} MODE\n')
        start_game(difficulty)
