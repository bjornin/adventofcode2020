def to_rpn(data, precedence):
    """
    Modified Shuntyard
    Inut: infix
    Output: postfix with given operator precedence
    """
    output = []
    ops = []
    for c in data:
        if c.isdigit():
            output.append(c)
        elif c == '(':
            ops.append(c)
        elif c == ')':
            o = ops.pop()
            while o != '(':
                output.append(o)
                o = ops.pop()
        else:
            while len(ops) and precedence.get(ops[-1], 0) >= precedence.get(c) and ops[-1] != '(':
                output.append(ops.pop())
            ops.append(c)
    while len(ops):
        o = ops.pop()
        output.append(o)
    return output

def calc_rpn(data) -> int:
    a = []
    b = {'+': lambda x,y: int(y)+int(x), '*': lambda x,y: int(y)*int(x)}
    for c in data:
        if c in b:
            a.append(b[c](a.pop(),a.pop()))
        else:
            a.append(c)
    return sum(a)

def part1(arg):
    precedence = {'+': 0, '*': 0}
    return sum([calc_rpn(to_rpn(a, precedence)) for a in arg])

def part2(arg):
    precedence = {'+': 1, '*': 0}
    return sum([calc_rpn(to_rpn(a, precedence)) for a in arg])

input = []
with open('./input.txt', 'r') as f:
    input = [x.strip().replace(' ','') for x in f]

test = """
1 + 2 + 3
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""

print('input rows:', len(input))
print('part1', part1(input))
# print('part1', part1(test.replace(' ','').split()))
print('part2', part2(input))
# print('part2', part2(test.replace(' ','').split()))
