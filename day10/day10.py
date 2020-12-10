def part1(arg):
    arg.sort()
    print(arg)
    diff = dict({1: 0 ,2: 0, 3: 0})
    jolt = 0
    for i in arg:
        d = i - jolt
        if d <= 3:
            diff[d] += 1
            jolt += d
    return diff[1] * (diff[3] + 1) # add device

def part2(arg):
    arg.sort()
    # arg = [1, 2, 5, 8, 9, 10, 11]
    arg.append(max(arg) + 3) # device
    paths = [1, 1, 2] # (outlet) -> 1 -> 2
    use_path = [False] * (arg[-1] + 1)
    for i in arg:
        use_path[i] = True
    for i in range(3, len(use_path)):
        p = paths[2] + paths[1] + paths[0]
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = p * use_path[i]
    return paths[2]

input = []
with open('./input.txt', 'r') as f:
    input = [int(x.rstrip()) for x in f]

print('input rows:', len(input))
print('part1', part1(input))
print('part2', part2(input))
