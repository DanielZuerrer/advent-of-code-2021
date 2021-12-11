from Board import Board

with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

drawn_numbers = [int(number) for number in lines[0].split(',')]

board_lines =  [lines[2:][x:x+6][:-1] for x in range(0, len(lines[2:]),6)]

boards = []
for board_line in board_lines:
    boards.append(Board(board_line))

def get_winning_board():
    for drawn_number in drawn_numbers:
        for board in boards:
            board.mark_number(drawn_number)
            if (board.won()):
                return board, drawn_number

winning_board, winning_number = get_winning_board()

print('Solution:', winning_board.leftover_sum() * winning_number)
