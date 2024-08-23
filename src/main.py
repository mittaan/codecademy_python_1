#!/usr/bin/env python3

from libs import Board, Path, pretty_header, choose_difficulty, set_parameters


def start_game(difficulty: str) -> None:

    # Parameters used to set the layout for the game
    width, height, tries = set_parameters(difficulty)
    path_level = 0

    # Initialising the classes imported from libs.py
    path = Path(width, height)
    board = Board(width, height, path)

    board.print_board()
    
    print(f'\nFind the hidden path! Insert a number between 0 and {width - 1}:')

    while tries >= 0:

        user_input = input()

        if not(user_input in [str(i) for i in range(width)]):
            print('Not a valid input, try again!')
            continue

        user_number = int(user_input)
        board.update_visual(user_number, path_level)

        # It's useful to represent the player's try as a (x,y)-pair of coordinates
        coords = f'{user_number},{path_level}'
        matched = board.has_matched(coords)

        if matched and path_level != (height - 1):
            path_level += 1
            print('\nCorrect! Keep going...')
        elif path_level == (height - 1):
            break
        elif tries > 0:
            print(f'\nNope, try again. You have {tries} tries left.')
            tries -= 1
        else:
            break
    
    # Added a final snapshot of the board to correctly update the display
    # of both the board and the points
    if tries != 0:
        board.update_visual(user_number, path_level, isEnd=True)
        print('\nCongratulations! You won the game :)')
    else:
        board.print_board()
        print('\nGame over. Better luck next time.')

    print(f'Total points scored: {path.get_points()} out of {height * 5}')


if __name__ == '__main__':
    while True:
        pretty_header()
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

        quitting = input('Do you want to keep playing? Quit [Q/q] or continue [C/c] >> ').upper()

        keep_playing = False

        while not(keep_playing):
            if quitting == 'Q':
                exit()
            elif quitting == 'C':
                keep_playing = True
            else:
                quitting = input('Not a valid input. Quit [Q/q] or continue [C/c] >> ').upper()
