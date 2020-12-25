def part1(arg):
    loops = [find_loops(int(i)) for i in arg]
    return get_encryption_key(loops[0], int(arg[1]))

def part2(arg):
    pass
def get_input(filename):
    input = []
    with open(filename, 'r') as f:
        input = [x.strip() for x in f]
    return input

def get_encryption_key(loops, public_key):
    v = 1
    for _ in range(loops):
        v = transform(v, public_key)
    return v

def find_loops(public_key):
    value = 1
    loop = 0
    while True:
        # if loop % 100 == 0:
        #     print(loop, value)
        loop += 1
        value = transform(value, 7)
        if value == public_key:
            return loop
    return -1

def transform(value, subj_nr):
    return (value * subj_nr) % 20201227

input = """
17115212
3667832
"""

test_input = """
5764801
17807724
"""

print('part1', part1(input.strip().split()))
# print('part1', part1(test_input.strip().split()))
# print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
