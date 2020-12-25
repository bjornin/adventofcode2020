def part1(arg):
    tiles = get_tiles(arg)
    return sum([v for v in tiles.values() if v == 1])

def part2(arg):
    tiles = get_tiles(arg)
    for d in range(1, 101):
        make_art(tiles)
    return sum([v for v in tiles.values() if v == 1])

def get_tiles(input):
    tiles = {}
    for instr in input:
        tile = parse_instruction(instr)
        tiles[tile] = tiles.get(tile, 0) # 0 = White, 1 = Black
        tiles[tile] = toggle_color(tiles[tile])
    return tiles
    
def make_art(tiles):
    black = get_adjacent_black(tiles)
    for k in black:
        tiles[k] = tiles.get(k, 0)
        if tiles[k] == 0 and black[k] == 2:
            tiles[k] = 1
        elif tiles[k] == 1 and (black[k] == 0 or black[k] > 2):
            tiles[k] = 0

def get_adjacent_black(tiles):
    black = {}
    neighbors = [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]
    for k in tiles:
        mid_x, mid_y, mid_z = k
        b = tiles[k]
        black[k] = black.get(k, 0)
        for x, y, z in neighbors:
            coord = (mid_x + x, mid_y + y, mid_z + z)
            black[coord] = black.get(coord, 0) + b
    return black

def toggle_color(color):
    return (color + 1) % 2

def parse_instruction(instr):
    x, y, z = (0, 0, 0)
    while len(instr) > 0:
        if instr.startswith('e'):
            x += 1
            y -= 1
            instr = instr[1:]
        elif instr.startswith('w'):
            x -= 1
            y += 1
            instr = instr[1:]
        elif instr.startswith('se'):
            y -= 1
            z += 1
            instr = instr[2:]
        elif instr.startswith('sw'):
            x -= 1
            z += 1
            instr = instr[2:]
        elif instr.startswith('ne'):
            x += 1
            z -= 1
            instr = instr[2:]
        elif instr.startswith('nw'):
            y += 1
            z -= 1
            instr = instr[2:]
    return (x,y,z)

def get_input(filename):
    input = []
    with open(filename, 'r') as f:
        input = [x.strip() for x in f]
    return input

print('part1', part1(get_input('./input.txt')))
# print('part1', part1(get_input('./test_input.txt')))
print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
