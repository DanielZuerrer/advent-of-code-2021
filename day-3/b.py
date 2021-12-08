with open('./input.txt', 'r', encoding='utf-8') as puzzle_input:
    lines = [line.strip() for line in puzzle_input.readlines()]

number_lengths = len(lines[0])

def get_oxygen_generator_rating(bit, numbers):
    if len(numbers) == 1:
        return numbers[0]

    bits = [int(number[bit]) for number in numbers]
    most_common = '1' if sum(bits) >= len(numbers) / 2 else '0'
    numbers = list(filter(lambda n: n[bit] == most_common, numbers))

    return get_oxygen_generator_rating(bit + 1, numbers)

def get_CO2_scrubber_rating(bit, numbers):
    if len(numbers) == 1:
        return numbers[0]

    bits = [int(number[bit]) for number in numbers]
    least_common = '1' if sum(bits) < len(numbers) / 2 else '0'
    numbers = list(filter(lambda n: n[bit] == least_common, numbers))

    return get_CO2_scrubber_rating(bit + 1, numbers)

oxygen_generator_rating = get_oxygen_generator_rating(0, lines)
CO2_scrubber_rating = get_CO2_scrubber_rating(0, lines)

oxygen_generator_rating = int(oxygen_generator_rating, base=2)
CO2_scrubber_rating = int(CO2_scrubber_rating, base=2)

print('Solution:', oxygen_generator_rating * CO2_scrubber_rating)
