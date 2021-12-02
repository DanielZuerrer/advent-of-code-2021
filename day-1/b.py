with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

depths = [int(line) for line in lines]

def calculate_windows():
    windows = []
    for idx, depth in enumerate(depths):
        if idx < (len(depths) - 2):
            depth_sum = depth + depths[idx + 1] + depths[idx + 2]
            windows.append(depth_sum)

    return windows

def count_increases(windows):
    increases = 0
    for idx, window in enumerate(windows):
        if idx > 0 and windows[idx-1] < window:
            increases += 1

    return increases

windows = calculate_windows()

print('Solution:', count_increases(windows))
