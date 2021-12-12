from Line import Line
import itertools
from collections import defaultdict

with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

lines = [Line(line) for line in lines]

points = [line.get_all_points() for line in lines]

points = list(itertools.chain(*points))

points_dict = defaultdict(int)

for point in points:
    points_dict[(point.x, point.y)] = points_dict[(point.x, point.y)] + 1

print('Solution:', sum(value > 1 for value in points_dict.values()))
