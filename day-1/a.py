with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

depths = [int(line) for line in lines]

increases = 0
for idx, depth in enumerate(depths):
    if idx > 0 and depths[idx-1] < depth:
        increases += 1

print('Solution:', increases)
