import Figure
import Point


class Points:
    def __init__(self, points: list[list[Point.Point]], order: str):
        self.points = points
        self.order = order

    def get_white(self) -> list[Figure.Figure]:
        figures = []
        for i in range(1, 9):
            for j in range(1, 9):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'w':
                        figures.append(cand.figure)
        return figures

    def get_black(self) -> list[Figure.Figure]:
        figures = []
        for i in range(1, 9):
            for j in range(1, 9):
                cand = self.points[i][j]
                if cand.figure:
                    if cand.figure.color == 'b':
                        figures.append(cand.figure)
        return figures

    def get_figures(self) -> dict[str, list[Figure.Figure]]:
        return {'w': Points.get_white(self)} | {'b': Points.get_black(self)}

    def possible_move_pawn(self, pawn: Figure.Pawn) -> set[tuple[str, int, int, int, int]]:
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
