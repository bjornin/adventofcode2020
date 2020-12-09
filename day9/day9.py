def get_values(l, sum):
    for x in range(len(l) - 1):
        for y in range(x + 1, len(l)):
            if (l[x] != l[y] and l[x] + l[y] == sum):
                return True
    return False

def part1(arg):
    for i in range(25, len(arg)):
        v = get_values(arg[i-25:i], arg[i])
        if not v:
            return arg[i]

def part2(arg):
    weakness = part1(arg)
    for x in range(len(arg) - 1):
        for y in range(x + 1, len(arg)):
            s = sum(arg[x:y])
            if s == weakness:
                return min(arg[x:y]) + max(arg[x:y])
            elif s > weakness:
                break
    return 0

input = []
with open('./input.txt', 'r') as f:
    input = [int(x.rstrip()) for x in f]

print('input rows:', len(input))
print('part1', part1(input))
print('part2', part2(input))

# not 3607989