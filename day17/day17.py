from collections import defaultdict, namedtuple
import math
from copy import deepcopy

Cell = namedtuple('Cell', "state neighbors")

def active_neighbors(m, x, y, z):
    active = 0
    for xn in range(x-1,x+2):
        for yn in range(y-1,y+2):
            for zn in range(z-1,z+2):
                m[xn][yn].setdefault(zn, Cell(0,0))
                active += m[xn][yn][zn].state
    return active - m[x][y][z].state

def active_neighbors2(m, x, y, z, w):
    active = 0
    for xn in range(x-1,x+2):
        for yn in range(y-1,y+2):
            for zn in range(z-1,z+2):
                for wn in range(w-1,w+2):
                    m[xn][yn][zn].setdefault(wn, Cell(0,0))
                    active += m[xn][yn][zn][wn].state
    return active - m[x][y][z][w].state

def update_cells(old):
    new = deepcopy(old)
    sum_active = 0
    for x in old.keys():
        for y in old[x].keys():
            for z in old[x][y].keys():
                state, _ = new[x][y][z]
                num = active_neighbors(new, x, y, z)
                new[x][y][z] = Cell(state, num)
    for x in new.keys():
        for y in new[x].keys():
            for z in new[x][y].keys():
                current_state, num_active_neighbors = new[x][y][z]
                if current_state:
                    sum_active += 1
                    new[x][y][z] = Cell(int(num_active_neighbors == 2 or num_active_neighbors == 3), num_active_neighbors)
                else:
                    new[x][y][z] = Cell(int(num_active_neighbors == 3), num_active_neighbors)
    return new, sum_active

def update_cells2(old):
    new = deepcopy(old)
    sum_active = 0
    for x in old.keys():
        for y in old[x].keys():
            for z in old[x][y].keys():
                for w in old[x][y][z].keys():
                    state, _ = new[x][y][z][w]
                    num = active_neighbors2(new, x, y, z, w)
                    new[x][y][z][w] = Cell(state, num)
    for x in new.keys():
        for y in new[x].keys():
            for z in new[x][y].keys():
                for w in new[x][y][z].keys():
                    current_state, num_active_neighbors = new[x][y][z][w]
                    if current_state:
                        sum_active += 1
                        new[x][y][z][w] = Cell(int(num_active_neighbors == 2 or num_active_neighbors == 3), num_active_neighbors)
                    else:
                        new[x][y][z][w] = Cell(int(num_active_neighbors == 3), num_active_neighbors)
    return new, sum_active

def part1(arg):
    for _ in range(7):
        arg, active = update_cells(arg)
        print(active)

def part2(arg):
    for _ in range(7):
        arg, active = update_cells2(arg)
        print(active)

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

test = """
.#.
..#
###
"""

def make_matrix(input):
    z = 0
    length = len(input)
    m = d_dict()
    for x in range(length):
        for y in range(length):
            m[x][y][z] = Cell(int((input[x][y] == '#')), 0)
    for x in range(length):
        for y in range(length):
            state, _ = m[x][y][z]
            num = active_neighbors(m, x, y, z)
            m[x][y][z] = Cell(state, num)
    return m

def make_matrix2(input):
    z = w = 0
    length = len(input)
    m = d_dict()
    for x in range(length):
        for y in range(length):
            m[x][y][z][w] = Cell(int((input[x][y][z] == '#')), 0)
    for x in range(length):
        for y in range(length):
            state, _ = m[x][y][z][w]
            num = active_neighbors2(m, x, y, z, w)
            m[x][y][z][w] = Cell(state, num)
    return m

def d_dict():
    return defaultdict(d_dict)

print('input rows:', len(input))
# print('part1', part1(make_matrix(input)))
# print('part1', part1(make_matrix(test.strip().split('\n'))))
print('part2', part2(make_matrix2(input)))
# print('part2', part2(make_matrix2(test.strip().split('\n'))))
