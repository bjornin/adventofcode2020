def part1(arg):
    rules, messages = parse_input(arg)
    count = 0
    for m in messages:
        if m in rules:
            count += 1
    return count

def part2(arg):
    pass

def parse_input(input):
    rules = {}
    messages = []
    for i in input:
        if len(i) == 0:
            continue
        elif i[0].isdigit():
            rule_nr, rule_pattern = i.split(': ')
            rules.setdefault(int(rule_nr), rule_pattern.replace('"',''))
        else:
            messages.append(i)
    patterns = parse_rules(0, rules)
    return patterns, messages

def parse_rules(index: int, rules):
    patterns = []
    for rule in rules[index].split('|'):
        part = []
        for r in rule.strip().split(' '):
            if r.isalpha():
                part.append(r)
            else:
                p = parse_rules(int(r), rules)
                if len(part):
                    part = ([x + y for x in part for y in p])
                else:
                    part = p
        if len(patterns):
            patterns.extend(part)
        else:
            patterns = part
    return patterns

input = []
with open('./input.txt', 'r') as f:
    input = [x.strip() for x in f]

test = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

test2 = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""


print('input rows:', len(input))
# print('part1', part1(input))
# print('part1', part1(test.strip().split('\n')))
# print('part2', part2(input))
print('part2', part2(test2.strip().split('\n')))
