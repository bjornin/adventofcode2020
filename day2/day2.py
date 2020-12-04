import re

def getmatch(s):
    pattern = r'^(?P<min>\d*)-(?P<max>\d*)\s(?P<char>\w):\s(?P<password>\w*)$'
    m = re.match(pattern, s)
    minc = int(m.group('min'))
    maxc = int(m.group('max'))
    c = m.group('char')
    password = m.group('password')
    return minc, maxc, c, password

def part1(arg):
    valid = 0
    for line in arg:
        minc, maxc, c, password = getmatch(line)
        count = password.count(c)
        if count >= minc and count <= maxc:
            valid += 1
    return valid

def part2(arg):
    valid = 0
    for line in arg:
        pos1, pos2, c, password = getmatch(line)
        valid += ((password[pos1 - 1] == c) ^ (password[pos2 - 1] == c))
    return valid

passwords = []
with open('./input.txt', 'r') as f:
    passwords = [x.rstrip() for x in f]

print('input rows:', len(passwords))
print('part1', part1(passwords))
print('part2', part2(passwords))
