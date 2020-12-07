import re

def part1(arg):
    parent = set()
    queue = ['shiny gold']
    while len(queue) > 0:
        color = queue.pop()
        for k, v in arg.items():
            if color in [c[1] for c in v]:
                parent.add(k)
                queue.insert(0,k)
    return len(parent)

def part2(arg):
    queue = ['shiny gold']
    ans = 0
    while len(queue) > 0:
        color = queue.pop()
        for child in arg[color]:
            ans += int(child[0])
            for _ in range(int(child[0])):
                queue.insert(0,child[1])
    return ans

def get_src(s):
    src_pattern = r'^(?P<src_color>\w+\s\w+)'
    m = re.search(src_pattern, s)
    return m['src_color']

def get_dst(s):
    dst_pattern = r'(?P<number>\d+)\s(?P<dst_color>\w+\s\w+)'
    m = re.findall(dst_pattern, s)
    return m

def clean_input(input):
    a = {}
    for i in input:
        src = get_src(i)
        groups = get_dst(i)
        a[src] = a.get(src, [])
        a[src].extend(groups)
    return a

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

print('input rows:', len(input))
print('part1', part1(clean_input(input)))
print('part2', part2(clean_input(input)))
