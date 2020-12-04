def get_trees(forrest, right, down):
    trees = 0
    for row in range(0, len(forrest), down):
        col = (row * right // down) % len(forrest[row])
        trees += forrest[row][col] == '#'
    return trees

def part1(arg):
    return get_trees(arg, 3, 1)

def part2(arg):
    return \
        get_trees(arg, 1, 1)* \
        get_trees(arg, 3, 1)* \
        get_trees(arg, 5, 1)* \
        get_trees(arg, 7, 1)* \
        get_trees(arg, 1, 2)

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

print('input rows:', len(input))
print('part1', part1(input))
print('part2', part2(input))
