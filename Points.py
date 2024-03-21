import Figure
import Point

# класс поля (клеток)


class Points:
    def __init__(self, points: list[list[Point.Point]], order: str):
        self.points = points
        self.order = order

    # получить все белые фигуры

    def get_white(self) -> list[Figure.Figure]:
        figures = []
        for i in range(1, 9):
            for j in range(1, 9):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'w':
                        figures.append(cand.figure)
        return figures

     # получить все черные фигуры

    def get_black(self) -> list[Figure.Figure]:
        figures = []
        for i in range(1, 9):
            for j in range(1, 9):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'b':
                        figures.append(cand.figure)
        return figures

    # получить все фигуры

    def get_figures(self) -> list[Figure.Figure]:
        return self.get_white() + self.get_black()
    
    # получить белого короля
    
    def get_white_king(self) -> list[Figure.Figure]:
        return [figure for figure in self.get_white()
                if figure is Figure.King]
    
    # получить черного короля
    
    def get_black_king(self) -> list[Figure.Figure]:
        return [figure for figure in self.get_black()
                if figure is Figure.King]

    # возможные ходы пешки

    def possible_move_pawn(self, pawn: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        if pawn.color == 'w':
            if self.points[pawn.pos_x][pawn.pos_y + 1].figure is None:
                moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y + 1))
                if pawn.pos_y == 2:
                    if self.points[pawn.pos_x][pawn.pos_y + 2].figure is None:
                        moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y + 2))
            if 1 <= pawn.pos_x <= 7:
                if self.points[pawn.pos_x + 1][pawn.pos_y + 1] is not None:
                    if self.points[pawn.pos_x + 1][pawn.pos_y + 1].figure.color != pawn.color:
                        moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x + 1, pawn.pos_y + 1))
            if 2 <= pawn.pos_y <= 8:
                if self.points[pawn.pos_x - 1][pawn.pos_y + 1] is not None:
                    if self.points[pawn.pos_x - 1][pawn.pos_y + 1].figure.color != pawn.color:
                        moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x - 1, pawn.pos_y + 1))
        elif pawn.color == 'b':
            if self.points[pawn.pos_x][pawn.pos_y - 1].figure is None:
                moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y - 1))
                if pawn.pos_y == 7:
                    if self.points[pawn.pos_x][pawn.pos_y - 2].figure is None:
                        moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x, pawn.pos_y - 2))
            if 1 <= pawn.pos_x <= 7:
                if self.points[pawn.pos_x + 1][pawn.pos_y - 1] is not None:
                    if self.points[pawn.pos_x + 1][pawn.pos_y - 1].figure.color != pawn.color:
                        moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x + 1, pawn.pos_y - 1))
            if 2 <= pawn.pos_y <= 8:
                if self.points[pawn.pos_x - 1][pawn.pos_y - 1] is not None:
                    if self.points[pawn.pos_x - 1][pawn.pos_y - 1].figure.color != pawn.color:
                        moves.append((pawn.identifier, pawn.pos_x, pawn.pos_y, pawn.pos_x - 1, pawn.pos_y - 1))
        else:
            raise NotImplemented
        return set(moves)

    # возможные ходы короля

    def possible_move_king(self, king: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (1 <= king.pos_x + i <= 8) or not (1 <= king.pos_y + j <= 8):
                    continue
                if i == 0 and j == 0:
                    continue
                if self.points[king.pos_x + i][king.pos_y + j] is not None:
                    if self.points[king.pos_x + i][king.pos_y + j].figure.color != king.color:
                        moves.append((king.identifier, king.pos_x, king.pos_y, king.pos_x + i, king.pos_y + j))
                else:
                    moves.append((king.identifier, king.pos_x, king.pos_y, king.pos_x + i, king.pos_y + j))
        return set(moves)

    # возможные ходы коня

    def possible_move_knight(self, knight: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        xy: list[tuple[int, int]] = [(2, 1), [1, 2], (2, -1), (1, -2), (-2, -1), (-1, -2), (-1, 2), (-2, 1)]
        for i, j in xy:
            if not (1 <= knight.pos_x + i <= 8) or not (1 <= knight.pos_y + j <= 8):
                continue
            if self.points[knight.pos_x + i][knight.pos_y + j] is not None:
                if self.points[knight.pos_x + i][knight.pos_y + j].figure.color != knight.color:
                    moves.append((knight.identifier, knight.pos_x, knight.pos_y, knight.pos_x + i, knight.pos_y + j))
            else:
                moves.append((knight.identifier, knight.pos_x, knight.pos_y, knight.pos_x + i, knight.pos_y + j))
        return set(moves)

    # возможные ходы слона

    def possible_move_bishop(self, bishop: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        # код Богдана
        return set(moves)

    # возможные ходы ладьи

    def possible_move_rook(self, rook: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        # код Богдана
        return set(moves)

    # возможные ходы ферзя

    def possible_move_queen(self, queen: Figure.Figure) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        # код Богдана
        return set(moves)

    # проверка на шах

    def is_check(self, order: str) -> bool:
        flag = False
        if order == 'w':
            king = self.get_white_king()[0]
            pos_x, pos_y = king.pos_x, king.pos_y
            for cand in self.move_black():
                x, y = cand[3], cand[4]
                if pos_x == x and pos_y == y:
                    flag = True
                    break
        elif order == 'b':
            king = self.get_black_king()[0]
            pos_x, pos_y = king.pos_x, king.pos_y
            for cand in self.move_white():
                x, y = cand[3], cand[4]
                if pos_x == x and pos_y == y:
                    flag = True
                    break
        else:
            raise NotImplemented
        return flag

    # возможные ходы белых без учета шахов
    def move_white(self) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        for figure in self.get_white():
            match figure:
                case Figure.Pawn:
                    moves += self.possible_move_pawn(figure)
                case Figure.King:
                    moves += self.possible_move_king(figure)
                case Figure.Knight:
                    moves += self.possible_move_knight(figure)
                case Figure.Bishop:
                    moves += self.possible_move_bishop(figure)
                case Figure.Rook:
                    moves += self.possible_move_rook(figure)
                case Figure.Queen:
                    moves += self.possible_move_queen(figure)
                case _:
                    raise NotImplemented
        return set(moves)

    # возможные ходы черных без учета шахов

    def move_black(self) -> set[tuple[str, int, int, int, int]]:
        moves = list()
        for figure in self.get_black():
            match figure:
                case Figure.Pawn:
                    moves += self.possible_move_pawn(figure)
                case Figure.King:
                    moves += self.possible_move_king(figure)
                case Figure.Knight:
                    moves += self.possible_move_knight(figure)
                case Figure.Bishop:
                    moves += self.possible_move_bishop(figure)
                case Figure.Rook:
                    moves += self.possible_move_rook(figure)
                case Figure.Queen:
                    moves += self.possible_move_queen(figure)
                case _:
                    raise NotImplemented
        return set(moves)
