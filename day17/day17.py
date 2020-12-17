from collections import defaultdict, namedtuple
import math
from copy import deepcopy

# class Matrix():
#     def __init__(self):
#         pass

Cell = namedtuple('Cell', "state neighbors")

def active_neighbors(m, x, y, z):
    active = 0
    for xn in range(x-1,x+2):
        for yn in range(y-1,y+2):
            for zn in range(z-1,z+2):
                m[xn][yn].setdefault(zn, Cell(0,0))
                active += m[xn][yn][zn].state
    return active - m[x][y][z].state

# def count_neighbors(old) -> defaultdict(int):
#     new = deepcopy(old)
#     for x in old.keys():
#         for y in old[x].keys():
#             for z in old[x][y].keys():
#                 new[get_index(x, y, z)] = active_neighbors(new, x, y, z)
#     print(new)
#     return new

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


def part1(arg):
    for _ in range(7):
        arg, active = update_cells(arg)
        print(active)

def part2(arg):
    pass

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
    m = defaultdict(lambda: defaultdict(dict))
    for x in range(length):
        for y in range(length):
            m[x][y][z] = Cell(int((input[x][y] == '#')), 0)
    for x in range(length):
        for y in range(length):
            state, _ = m[x][y][z]
            num = active_neighbors(m, x, y, z)
            m[x][y][z] = Cell(state, num)
    return m

print('input rows:', len(input))
# print('part1', part1(make_matrix(input)))
# print('part1', part1(make_matrix(test.strip().split('\n'))))
# print('part2', part2(input))
print('part2', part2(make_matrix(test.strip().split('\n'))))
