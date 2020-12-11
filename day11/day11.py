import math

def get_row_neighbors(layout, pos, length):
    if pos < 0 or pos >= len(layout):
        return []
    start = max(pos // length * length, pos - 1)
    end = min(math.ceil((pos + 1)/length) * length, pos + 2)
    return layout[start:end]

def get_neighbors(layout, seat, length):
    ret = []
    ret.extend(get_row_neighbors(layout, seat - length, length))
    ret.extend(get_row_neighbors(layout, seat, length))
    ret.extend(get_row_neighbors(layout, seat + length, length))
    return ret

def update_seat(layout, seat, length):
    neighbors = get_neighbors(layout, seat, length)
    if layout[seat] == 'L' and neighbors.count('#') == 0:
        return '#'
    elif layout[seat] == '#' and neighbors.count('#') > 4:
        return 'L'
    return layout[seat]

def part1(arg):
    layout, length = arg
    print(layout, length)
    org_layout = []
    while org_layout != layout:
        org_layout = layout.copy()
        for seat in range(len(org_layout)):
            if org_layout[seat] != '.':
                layout[seat] = update_seat(org_layout, seat, length)
    return layout.count('#')

def part2(arg):
    pass

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

test = [
'L.LL.LL.LL',
'LLLLLLL.LL',
'L.L.L..L..',
'LLLL.LL.LL',
'L.LL.LL.LL',
'L.LLLLL.LL',
'..L.L.....',
'LLLLLLLLLL',
'L.LLLLLL.L',
'L.LLLLL.LL',
]

def clean_input(input):
    length = len(input[0])
    return (list(''.join(input)), length)

print('input rows:', len(input))
print('part1', part1(clean_input(input)))
# print('part1', part1(clean_input(test)))
print('part2', part2(input))
