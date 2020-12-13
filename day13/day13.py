def part1(arg):
    time, schedule = arg
    schedule.sort()
    min_wait = 100
    min_index = -1
    for i, s in enumerate(schedule):
        if s != 'x':
            rest = time % int(s)
            wait_time = int(s) - rest
            if wait_time < min_wait:
                min_wait = wait_time
                min_index = i
    print(schedule[min_index], min_wait)
    return int(schedule[min_index]) * min_wait

def part2(arg):
    _, schedule = arg
    indexed_list = [(i, s) for i, s in enumerate(schedule) if s != 'x']
    t = 1
    while True:
        rest = 0
        for i, s in indexed_list:
            rest += (t + i) % int(s)
        if rest == 0:
            return t
        if t % 1000 == 0:
            print(t)
        t += 1


input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

test = """
939
7,13,x,x,59,x,31,19
"""

def clean_input(input):
    time = int(input[0])
    schedule = input[1].split(',')
    return (time, schedule)

print('input rows:', len(input))
print('part1', part1(clean_input(input)))
# print('part1test', part1(clean_input(test.strip().split('\n'))))
print('part2', part2(clean_input(input)))
# print('part2', part2(clean_input(test.strip().split('\n'))))
