def part1(arg):
    visited = [False] * len(arg)
    i = 0
    acc = 0
    while not visited[i]:
        visited[i] = True
        inst, number = arg[i].split(' ')
        if inst == 'acc':
            acc += int(number)
            i += 1
        elif inst == 'jmp':
            i += int(number)
        elif inst == 'nop':
            i += 1
    return acc

def part2(arg):
    pass

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

print('input rows:', len(input))
print('part1', part1(input))
print('part2', part2(input))
