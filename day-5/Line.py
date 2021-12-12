import re
from typing import List

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, line):
        coordinates = re.findall(r'(\d+)', line)
        self.one = Coordinate(int(coordinates[0]), int(coordinates[1]))
        self.two = Coordinate(int(coordinates[2]), int(coordinates[3]))

    def is_orthogonal(self) -> bool:
        return self.one.x == self.two.x or self.one.y == self.two.y

    def get_all_points(self) -> List[Coordinate]:
        points = []
        x_dir = 1 if self.two.x - self.one.x >= 0 else -1
        y_dir = 1 if self.two.y - self.one.y >= 0 else -1
        x_points = list(range(self.one.x, self.two.x + x_dir, x_dir))
        y_points = list(range(self.one.y, self.two.y + y_dir, y_dir))

        if (len(x_points) == 1):
            for y in y_points:
                points.append(Coordinate(x_points[0],y))
        elif (len(y_points) == 1):
            for x in x_points:
                points.append(Coordinate(x,y_points[0]))
        else:
            for i in range(len(x_points)):
                points.append(Coordinate(x_points[i], y_points[i]))
        
        return points


