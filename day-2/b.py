with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

commands = [line.split(' ') for line in lines]
commands = [(command[0], int(command[1])) for command in commands]

COMMAND_OPERATIONS = {
    'forward': (lambda horizontal_pos, depth, aim, amount: (horizontal_pos + amount, depth + amount * aim, aim)),
    'down': (lambda horizontal_pos, depth, aim, amount: (horizontal_pos, depth, aim + amount)),
    'up': (lambda horizontal_pos, depth, aim, amount: (horizontal_pos, depth, aim - amount)),
}

horizontal_pos, depth, aim = 0, 0, 0

for command in commands:
    horizontal_pos, depth, aim = COMMAND_OPERATIONS[command[0]](horizontal_pos, depth, aim, command[1])

print('Solution:', horizontal_pos * depth)
