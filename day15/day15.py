from collections import namedtuple

Number = namedtuple('Number', ['last', 'prev'])

def part1(arg):
    return get_number(arg, 2020)

def part2(arg):
    return get_number(arg, 30000000)

def get_number(seq, stop):
    count = {}
    number = -1
    i = 1
    for n in seq: # starting numbers
        number = n
        last, _ = count.get(number, Number(0,0))
        count[number] = Number(i, last)
        i += 1
    for m in range(i, stop + 1): # rest
        last, prev = count.get(number, Number(0,0))
        if prev:
            number = last - prev
            last, prev = count.get(number, Number(0,0))
            count[number] = Number(m, last)
        else:
            number = 0
            last, _ = count.get(number, Number(0,0))
            count[number] = Number(m, last)
    return number

input = """
12,1,16,3,11,0
"""

test = """
2,1,3
"""

def clean_input(input):
    return [int(x) for x in input.strip().split(',')]

print('input rows:', len(input))
print('part1', part1(clean_input(input)))
# print('part1', part1(clean_input(test)))
print('part2', part2(clean_input(input)))
# print('part2', part2(test2.strip().split('\n')))
