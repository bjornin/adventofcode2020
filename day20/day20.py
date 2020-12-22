import math
from collections import namedtuple

def part1(arg):
    tiles = parse_input(arg)
    corners, _, _ = categorize_tiles(tiles)
    return math.prod(corners)

def part2(arg):
    tiles = parse_input(arg)
    image = Image(tiles)
    num_hash = image.count_hash()
    num_monster = image.count_monster()
    print(num_monster)
    return num_hash - num_monster * 15

Tile = namedtuple('Tile', 'number data', defaults=(None,None))

class Image():
    def __init__(self, tiles):
        size = int(math.sqrt(len(tiles)))
        self.tiles = tiles
        self.image = [[Tile() for _ in range(size)] for _ in range(size)]
        print('solve')
        self.solve()
        for row in range(len(self.image)):
            for col in range(len(self.image)):
                print(row, col, self.image[row][col].number)
        print('trim')
        self.trim_image()
        
    def solve(self): # backtracking
        row, col = self.get_empty_cell()
        if row < 0 or col < 0:
            print('Done')
            return True
        used_tiles = []
        for r in range(len(self.image)):
            for c in range(len(self.image)):
                if (nr := self.image[r][c].number) != None:
                    used_tiles.append(nr)
        tiles = [(nr, t) for nr, t in self.tiles.items() if nr not in used_tiles]
        for nr, t in tiles:
            for _ in range(2): # flip
                t = flip_h(t)
                for _ in range(4): # rotate
                    t = rotate_cw(t)
                    if self.tile_fits(t, row, col):
                        self.image[row][col] = Tile(nr, t)
                        if self.solve():
                            return True
                        self.image[row][col] = Tile()
        return False

    def get_empty_cell(self):
        for row in range(len(self.image)):
            for col in range(len(self.image)):
                if self.image[row][col].data is None:
                    return row, col
        return -1, -1
    
    def tile_fits(self, tile, row, col):
        fits = False
        if row == 0 and col == 0:
            fits = True
        elif row == 0: # check only left
            fits = self.match_left(self.image[row][col - 1].data, tile)
        elif col == 0: # check only top 
            fits = self.match_top(self.image[row - 1][col].data, tile)
        else: # check top and left
            fits = self.match_left(self.image[row][col - 1].data, tile) and self.match_top(self.image[row - 1][col].data, tile)
        return fits

    def match_left(self, left, right):
        return rotate_cw(right)[0] == rotate_cw(left)[-1]

    def match_top(self, top, bottom):
        return bottom[0] == top[-1]
    
    def trim_image(self):
        self.trimmed_image = {}
        for tile_row in range(len(self.image)):
            for tile_col in range(len(self.image)):
                tile = self.image[tile_row][tile_col].data
                for image_row, data in enumerate([t[1:-1] for t in tile[1:-1]]):
                    trimmed_row = tile_row * len(data) + image_row
                    self.trimmed_image[trimmed_row] = self.trimmed_image.get(trimmed_row, [])
                    self.trimmed_image[trimmed_row].extend(data)

    def count_hash(self):
        flat = [h for sub in self.trimmed_image.values() for h in sub]
        return sum([1 for ele in flat if ele == '#'])

    def count_monster(self):
        num_monster = 0
        image = list(self.trimmed_image.values())
        l = len(image)
        # monster form
        #                   # 
        # #    ##    ##    ###
        #  #  #  #  #  #  #    
        # flat monster
        monster = [0,l-18,l-13,l-12,l-6,l-5,l-1,l,l+1,2*l-17,2*l-14,2*l-11,2*l-8,2*l-5,2*l-2]
        for _ in range(2): # flip
            image = flip_h(image)
            for _ in range(4): # rotate
                image = rotate_cw(image)
                for start in range(len(flat)):
                    found = True
                    for m in monster:
                        if flat[start + m] != '#':
                            found = False
                            break
                    num_monster += found
        return num_monster

    # def count_monster(self):
    #     num_monster = 0
    #     image = list(self.trimmed_image.values())
    #     l = len(image)
    #     # monster form
    #     #                   # 
    #     # #    ##    ##    ###
    #     #  #  #  #  #  #  #    
    #     # flat monster
    #     monster = [0,l-18,l-13,l-12,l-6,l-5,l-1,l,l+1,2*l-17,2*l-14,2*l-11,2*l-8,2*l-5,2*l-2]
    #     for _ in range(2): # flip
    #         image = flip_h(image)
    #         for _ in range(4): # rotate
    #             image = rotate_cw(image)
    #             flat = [h for sub in image for h in sub]
    #             for start in range(len(flat)):
    #                 found = True
    #                 for m in monster:
    #                     if flat[start + m] != '#':
    #                         found = False
    #                         break
    #                 num_monster += found
    #     return num_monster

def categorize_tiles(tiles):
    corners = []
    borders = []
    fill = []
    for t in tiles:
        matching_borders = match(t, tiles)
        print(t, matching_borders)
        if matching_borders == 2:
            corners.append(t)
        elif matching_borders == 3:
            borders.append(t)
        elif matching_borders == 4:
            fill.append(t)
    return corners, borders, fill

def match(tile_nr, tiles):
    matching_edges = 0
    tile = tiles[tile_nr]
    for t in [t for t in tiles if t != tile_nr]:
        compare_tile = tiles[t]
        for _ in range(4): # all sides on tile
            tile = rotate_cw(tile)
            for _ in range(2): # flip compare tile twice
                compare_tile = flip_h(compare_tile)
                for _ in range(4): # all sides on compare tile
                    compare_tile = rotate_cw(compare_tile)
                    if tile[0] == compare_tile[-1]:
                        matching_edges += 1
    return matching_edges
            
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

# print('part1', part1(get_input('./input.txt')))
# print('part1', part1(get_input('./test_input.txt')))
print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
