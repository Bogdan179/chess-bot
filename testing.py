import Points
import Point
import Figure


def start_game(list_of_points: list[list[Point.Point]]):
    with open('input.txt') as input_file:
        inp = input_file.readline().rstrip()
        while inp:
            name, color, pos = map(str, inp.split())
            pos_x, pos_y = int(pos[0]), int(pos[1])
            assert 0 <= pos_x <= 7
            assert 0 <= pos_y <= 7
            if name == "Pawn":
                list_of_points[pos_x][pos_y].figure = Figure.Pawn(color, pos_x, pos_y)
            elif name == "King":
                list_of_points[pos_x][pos_y].figure = Figure.King(color, pos_x, pos_y)
            elif name == "Knight":
                list_of_points[pos_x][pos_y].figure = Figure.Knight(color, pos_x, pos_y)
            elif name == "Bishop":
                list_of_points[pos_x][pos_y].figure = Figure.Bishop(color, pos_x, pos_y)
            elif name == "Rook":
                list_of_points[pos_x][pos_y].figure = Figure.Rook(color, pos_x, pos_y)
            elif name == "Queen":
                list_of_points[pos_x][pos_y].figure = Figure.Queen(color, pos_x, pos_y)
            else:
                raise NotImplemented
            inp = input_file.readline().rstrip()


points = [[Point.Point(x, y, None) for x in range(0, 8)] for y in range(0, 8)]
start_game(points)
position = Points.Points(points, 'w')

moves = position.move_white()
print(moves)
