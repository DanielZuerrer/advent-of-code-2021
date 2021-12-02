with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

commands = [line.split(' ') for line in lines]
commands = [(command[0], int(command[1])) for command in commands]

COMMAND_OPERATIONS = {
    'forward': (lambda horizontal_pos, depth, amount: (horizontal_pos + amount, depth)),
    'down': (lambda horizontal_pos, depth, amount: (horizontal_pos, depth + amount)),
    'up': (lambda horizontal_pos, depth, amount: (horizontal_pos, depth - amount)),
}

horizontal_pos, depth = 0, 0

for command in commands:
    horizontal_pos, depth = COMMAND_OPERATIONS[command[0]](horizontal_pos, depth, command[1])

print('Solution:', horizontal_pos * depth)
