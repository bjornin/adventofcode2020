def binarify(code):
    return code.replace('F','0').replace('B','1').replace('R','1').replace('L','0')

def get_id(code):
    row = int(code[:7],2)
    col = int(code[7:],2)
    return row * 8 + col

def part1(arg):
    max_id = 0
    for i in arg:
        i = binarify(i)
        max_id = max(max_id, get_id(i))
    return max_id

def part2(arg):
    codes = []
    for i in arg:
        codes.append(binarify(i))
    codes.sort()

    for c in range(1, len(codes)-1):
        this_id = get_id(codes[c])
        next_id = get_id(codes[c+1])
        if this_id != next_id - 1:
            return this_id + 1

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

print('input rows:', len(input))
print('part1', part1(input))
print('part2', part2(input))
