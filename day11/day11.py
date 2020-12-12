import math

# def get_row_neighbors(layout, pos, length):
#     if pos < 0 or pos >= len(layout):
#         return []
#     start = max(pos // length * length, pos - 1)
#     end = min(math.ceil((pos + 1)/length) * length, pos + 2)
#     return layout[start:end]

# def get_neighbors(layout, seat, length):
#     ret = []
#     ret.extend(get_row_neighbors(layout, seat - length, length))
#     ret.extend(get_row_neighbors(layout, seat, length))
#     ret.extend(get_row_neighbors(layout, seat + length, length))
#     return ret

# def update_seat(layout, seat, length):
#     neighbors = get_neighbors(layout, seat, length)
#     if layout[seat] == 'L' and neighbors.count('#') == 0:
#         return '#'
#     elif layout[seat] == '#' and neighbors.count('#') > 4:
#         return 'L'
#     return layout[seat]

def get_col(seat, length):
    return seat % length

def get_row(seat, length):
    return seat // length

def find_seat_in_direction(layout, seat, length, d, adjacent_steps):
    r, c = d
    row = get_row(seat, length)
    col = get_col(seat, length)
    max_row = len(layout)//length - 1
    step = 0
    while step < adjacent_steps:
        row += r
        col += c
        if row < 0 or row > max_row or col < 0 or col > (length - 1):
            return
        if layout[length * row + col] != '.':
            return length * row + col
        step += 1
        
def get_neighbors(layout, seat, length, adjacent_steps):
    mask = []
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for d in directions:
        pos = find_seat_in_direction(layout, seat, length, d, adjacent_steps)
        if pos != None:
            mask.append(pos)
    ret = [layout[x] for x in set(mask)]
    return ret

def update_seat(layout, seat, length, adjacent_ok, adjacent_steps):
    neighbors = get_neighbors(layout, seat, length, adjacent_steps)
    if layout[seat] == 'L' and neighbors.count('#') == 0:
        return '#'
    elif layout[seat] == '#' and neighbors.count('#') >= adjacent_ok:
        return 'L'
    return layout[seat]

def get_occupied(layout, length, adjacent_ok, adjacent_steps):
    org_layout = []
    round = 0
    while org_layout != layout:
        org_layout = layout.copy()
        for seat in range(len(org_layout)):
            if org_layout[seat] != '.':
                layout[seat] = update_seat(org_layout, seat, length, adjacent_ok, adjacent_steps)
        round += 1
        print(round)
    return layout.count('#')

def part1(arg):
    layout, length = arg
    return get_occupied(layout, length, 4, 1)

def part2(arg):
    layout, length = arg
    return get_occupied(layout, length, 5, length)

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
print('part2', part2(clean_input(input)))
# print('part2', part2(clean_input(test)))
