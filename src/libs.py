import random as rn

def pretty_header() -> None:
    ascii_art = '''
 ======================================================================
||  ______ _           _   _   _                        _   _         ||
||  |  ___(_)         | | | | | |                      | | | |        ||
||  | |_   _ _ __   __| | | |_| |__   ___   _ __   __ _| |_| |__      ||
||  |  _| | | '_ \ / _` | | __| '_ \ / _ \ | '_ \ / _` | __| '_ \     ||
||  | |   | | | | | (_| | | |_| | | |  __/ | |_) | (_| | |_| | | |    ||
||  \_|   |_|_| |_|\__,_|  \__|_| |_|\___| | .__/ \__,_|\__|_| |_|    ||
||                                         | |                        ||
||                                         |_|                        ||
||                                                                    ||
 ======================================================================

 Welcome to Find-the-Path!

 ----------------------------------------------------------------------

 Test your luck! Choose a square and progress down the path.

'''

    print(ascii_art)


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
            return (4, 4, 10)
        case 'MEDIUM':
            return (6, 4, 5)
        case 'HARD':
            return (8, 5, 3)
        case 'IRON':
            return (4, 4, 1)

class Path:
    def __init__(self, width: int, height: int):
        self.WIDTH = width
        self.HEIGHT = height
        self.path = self.__create_path()
        self.points = 0

    def __create_path(self) -> list:
        basic_path = [["□" if _ != 0 else "■" for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        shuffled_path = []
        for row in basic_path:
            rn.shuffle(row)
            shuffled_path.append(row)
        return shuffled_path
    
    def get_level(self, level: int) -> list:
        counter = 0
        for row in self.path:
            if level == counter:
                return row
            counter += 1

    def add_points(self, tries: int) -> None:
        if tries == 1:
            points = 5
        elif tries == 2:
            points = 3
        elif tries == 3:
            points = 2
        else:
            points = 1
        self.points += points

    def get_points(self) -> int:
        return self.points


class Board:
    def __init__(self, width: int, height: int, path: Path):
        self.WIDTH = width
        self.HEIGHT = height
        self.board = self.__create_board()
        self.path = path
        self.isMatched = {}
    
    def __create_board(self) -> list:
        return [["□" for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
    
    def print_board(self, difficulty: str) -> None:
        print('\n')
        column_numbers = '0:'

        params = set_parameters(difficulty)
        remaining_columns = 1
        while remaining_columns != params[0]:
            column_numbers += f'   {remaining_columns}:'
            remaining_columns += 1

        print(f'          {column_numbers}\n')
        count = 1
        for row in self.board:
            print(f'{count}:\t{row}')
            count += 1

    def has_matched(self, coords: str) -> bool:
        return self.isMatched.get(coords)

    def __update_board(self, update_index: int) -> list:
        board_updated = []
        for i in range(self.HEIGHT):
            if i <= update_index:
                board_updated.append(self.path.get_level(i))
            else:
                board_updated.append(["□" for _ in range(self.WIDTH)])
        return board_updated
    
    def __check_path(self, user_input: int, path_level: int) -> bool:
        if path_level >= self.HEIGHT:
            return
        coords = f'{user_input},{path_level}'
        hidden_value = list(self.path.get_level(path_level))

        if hidden_value[user_input] == "■":
            self.isMatched.update({coords: True})
        else:
            self.isMatched.update({coords: False})
        return self.isMatched.get(coords)
    
    def __count_tries(self, user_try: int) -> int:
        level = f',{user_try}'
        tries = 0
        for element in self.isMatched.keys():
            if level in element:
                tries += 1
        return tries

    def update_visual(self, user_input: int, path_level: int, difficulty: str) -> None:
        if self.__check_path(user_input, path_level):
            self.board = self.__update_board(path_level)
            tries = self.__count_tries(path_level)
            self.path.add_points(tries)
            self.print_board(difficulty)