import random as rn

class Path:
    def __init__(self, width: int, height: int):
        self.WIDTH = width
        self.HEIGHT = height
        self.path = self.__create_path()

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


class Board:
    def __init__(self, width: int, height: int, path: Path):
        self.WIDTH = width
        self.HEIGHT = height
        self.board = self.__create_board()
        self.path = path
        self.isMatched = {}
    
    def __create_board(self) -> list:
        return [["□" for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
    
    def print_board(self) -> None:
        print('\n')
        for row in self.board:
            print(row)

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

    def update_visual(self, user_input: int, path_level: int) -> None:
        if self.__check_path(user_input, path_level):
            self.board = self.__update_board(path_level)
            self.print_board()



