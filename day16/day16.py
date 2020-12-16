import re

def part1(arg):
    fields, tickets = arg
    invalid = 0
    for t in tickets[1:]:
        for n in t:
            if int(n) not in [int(k) for k in fields]:
                invalid += int(n)
    return invalid

def part2(arg):
    fields, tickets = arg
    order = [set(sum(fields.values(), []))] * len(tickets[0])
    for t in tickets[1:]:
        for n in t:
            if int(n) not in [int(k) for k in fields]:
                tickets.remove(t)
    for i, tr in enumerate(zip(*tickets[1:])):
        for t in tr:
            order[i] = order[i].intersection(set(fields[int(t)]))
    used_fields = set()
    ans = 1
    print(tickets[0])
    for i, o in sorted(enumerate(order), key=lambda x: len(x[1])):
        field = used_fields.symmetric_difference(o).pop()
        used_fields.add(field)
        if field.startswith('departure'):
            ans *= int(tickets[0][i])
    return ans
        

def clean_input(input):
    field_pattern = r'^(?P<field>.+):\s(?P<range1>\d+-\d+)\sor\s(?P<range2>\d+-\d+)$'
    fields = {}
    tickets = []
    for i in input:
        if i == '':
            continue
        if i[0].isdigit():
            tickets.append(i.split(','))
            continue
        m = re.match(field_pattern, i)
        if m:
            field = m['field']
            field1 = m['range1'].split('-')
            field2 = m['range2'].split('-')
            for j in range(int(field1[0]), int(field1[1]) + 1):
                fields.setdefault(j, [])
                fields[j].append(field)
            for k in range(int(field2[0]), int(field2[1]) + 1):
                fields.setdefault(k, [])
                fields[k].append(field)
    return fields, tickets

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

test = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

test2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""

print('input rows:', len(input))
print('part1', part1(clean_input(input)))
# print('part1', part1(clean_input(test.strip().split('\n'))))
print('part2', part2(clean_input(input)))
# print('part2', part2(clean_input(test2.strip().split('\n'))))
