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
    for line in range(len(arg)):
        if arg[line].startswith('acc'):
            continue
        swapped = arg.copy()
        if arg[line].startswith('nop'):
            swapped[line] = swapped[line].replace('nop', 'jmp')
        elif arg[line].startswith('jmp'):
            swapped[line] = swapped[line].replace('jmp', 'nop')
        i = 0
        acc = 0
        visited = [False] * len(swapped)
        while not visited[i]:
            visited[i] = True
            inst, number = swapped[i].split(' ')
            if inst == 'acc':
                acc += int(number)
                i += 1
            elif inst == 'jmp':
                i += int(number)
            elif inst == 'nop':
                i += 1
            if (i == len(swapped)):
                return acc

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

print('input rows:', len(input))
print('part1', part1(input))
print('part2', part2(input))
