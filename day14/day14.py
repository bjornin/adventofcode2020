import re
from itertools import product

def part1(arg):
    mem = {}
    mask = ''
    for i in arg:
        if i.startswith('mask'):
            mask = i.split(' = ')[1]
        else:
            pattern = r'^mem\[(?P<address>\d*)\] = (?P<value>.*)'
            m = re.match(pattern, i)
            address = int(m['address'])
            value = int(m['value'])
            for i, bit in [(i, int(x)) for i, x in enumerate(mask[::-1]) if x != 'X']:
                if bit:
                    value = value|(1<<i)
                else:
                    value = value&~(1<<i)
            mem[address] = mem.get(address, 0)
            mem[address] = value
    return(sum(mem.values()))

def part2(arg):
    mem = {}
    mask = ''
    for i in arg:
        if i.startswith('mask'):
            mask = i.split(' = ')[1]
        else:
            pattern = r'^mem\[(?P<address>\d*)\] = (?P<value>.*)'
            match = re.match(pattern, i)
            address = int(match['address'])
            value = int(match['value'])
            for a in get_addresses(address, mask):
                mem[a] = mem.get(a, 0)
                mem[a] = value
    return(sum(mem.values()))

def get_addresses(address, mask):
    address_bin = format(address, '036b')
    res = ''.join(['X' if x == 'X' or y == 'X' else str(int(x)|int(y)) for x, y in zip(address_bin, mask)])
    count_x = mask.count('X')
    ret = []
    for c in product(range(2), repeat=count_x):
        perm = res.replace('X','{}').format(*c)
        ret.append(perm)
    return ret

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

test = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

test2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

print('input rows:', len(input))
print('part1', part1(input))
# print('part1', part1(test.strip().split('\n')))
print('part2', part2(input))
# print('part2', part2(test2.strip().split('\n')))
