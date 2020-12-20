import math

def part1(arg):
    tiles = parse_input(arg)
    corners = []
    for t in tiles: # brute force
        matching_borders = match(t, tiles)
        if matching_borders == 2:
            corners.append(t)
    return math.prod(corners)

def match(tile_nr, tiles):
    matching_borders = 0
    tile = tiles[tile_nr]

    for t in [t for t in tiles if t != tile_nr]:
        compare_tile = tiles[t]
        for _ in range(4):
            tile = rotate_cw(tile)
            for _ in range(2):
                compare_tile = flip_h(compare_tile)
                for _ in range(4):
                    compare_tile = rotate_cw(compare_tile)
                    if tile[0] == compare_tile[-1]:
                        matching_borders += 1
    return matching_borders
            

def part2(arg):
    pass

def flip_h(tile):
    ret = []
    for t in tile:
        ret.append(t[::-1])
    return ret

def rotate_cw(tile):
    transpose = list(zip(*tile))
    return flip_h(transpose)

def parse_input(input: list()):
    tiles = {}
    tile = []
    for i in input:
        if i.startswith('Tile'):
            tile_nr = i[5:-1]
        elif i == '':
            tiles.setdefault(int(tile_nr), tile.copy())
            tile.clear()
        else:
            tile.append(list(i))
    tiles.setdefault(int(tile_nr), tile.copy())
    return tiles

def get_input(filename):
    input = []
    with open(filename, 'r') as f:
        input = [x.strip() for x in f]
    return input

print('part1', part1(get_input('./input.txt')))
# print('part1', part1(get_input('./test_input.txt')))
#print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
