with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

number_count = len(lines)
number_lengths = len(lines[0])

def get_bit_sum(bit, numbers):
    bits = [int(number[bit]) for number in numbers]
    return sum(bits)

gamma_rate = ''
for bit in range(number_lengths):
    bit_sum = get_bit_sum(bit, lines)
    gamma_rate += ('1' if bit_sum > number_count / 2 else '0')

epsilon_rate = ''.join(['1' if b == '0' else '0' for b in gamma_rate])
gamma_rate = int(gamma_rate, base=2)
epsilon_rate = int(epsilon_rate, base=2)

print('Solution:', gamma_rate * epsilon_rate)
