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

def get_horizontal(layout, seat, length):
    start = seat // length * length
    end = start + length
    return range(start,end)

def get_vertical(layout, seat, length):
    start = get_col(seat, length)
    return [i * length + start for i in range(len(layout)//length)]

def get_rdiag(layout, seat, length):
    col = get_col(seat, length)
    row = get_row(seat, length)
    start = (col - row) if 0 <= col - row < length else row * length + col
    diag = [i * (length + 1) + start for i in range(length - col - row)]
    return diag

def get_ldiag(layout, seat, length):
    col = get_col(seat, length)
    row = get_row(seat, length)
    start = (col + row) if col + row < length - 1 else row * col + row + col
    diag = [i * (length - 1) + start for i in range(get_col(start, length) - get_row(start, length) + 1)]
    return diag

def get_col(seat, length):
    return seat % length

def get_row(seat, length):
    return seat // length

def get_neighbors_2(layout, seat, length):
    mask = []
    mask.extend(get_horizontal(layout, seat, length))
    mask.extend(get_vertical(layout, seat, length))
    mask.extend(get_rdiag(layout, seat, length))
    mask.extend(get_ldiag(layout, seat, length))
    ret = [layout[x] for x in set(mask)]
    return ret

def update_seat_2(layout, seat, length):
    neighbors = get_neighbors_2(layout, seat, length)
    if layout[seat] == 'L' and neighbors.count('#') == 0:
        return '#'
    elif layout[seat] == '#' and neighbors.count('#') > 5:
        return 'L'
    return layout[seat]

def part2(arg):
    layout, length = arg
    print(layout, length)
    org_layout = []
    round = 0
    while org_layout != layout:
        org_layout = layout.copy()
        for seat in range(len(org_layout)):
            if org_layout[seat] != '.':
                layout[seat] = update_seat_2(org_layout, seat, length)
        round += 1
        print(round)
    return layout.count('#')

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
# print('part1', part1(clean_input(input)))
# print('part1', part1(clean_input(test)))
print('part2', part2(clean_input(test)))
