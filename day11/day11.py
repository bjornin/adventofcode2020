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
        
def get_neighbors(layout, seat, length, adjacent_steps, memo):
    mask = memo.get(seat, [])
    if len(mask) == 0:
        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for d in directions:
            pos = find_seat_in_direction(layout, seat, length, d, adjacent_steps)
            if pos != None:
                mask.append(pos)
        memo[seat] = mask
    ret = [layout[x] for x in set(mask)]
    return ret

def update_seat(layout, seat, length, adjacent_ok, adjacent_steps, memo):
    neighbors = get_neighbors(layout, seat, length, adjacent_steps, memo)
    if layout[seat] == 'L' and neighbors.count('#') == 0:
        return '#'
    elif layout[seat] == '#' and neighbors.count('#') >= adjacent_ok:
        return 'L'
    return layout[seat]

def get_occupied(layout, length, adjacent_ok, adjacent_steps, memo):
    org_layout = []
    while org_layout != layout:
        org_layout = layout.copy()
        for seat in range(len(org_layout)):
            if org_layout[seat] != '.':
                layout[seat] = update_seat(org_layout, seat, length, adjacent_ok, adjacent_steps, memo)
    return layout.count('#')

def part1(arg):
    layout, length = arg
    memo = {}
    return get_occupied(layout, length, 4, 1, memo)

def part2(arg):
    layout, length = arg
    memo = {}
    return get_occupied(layout, length, 5, length, memo)

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
