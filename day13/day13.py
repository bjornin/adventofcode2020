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
    return int(schedule[min_index]) * min_wait

def part2(arg):
    _, schedule = arg
    indexed_list = [(i, int(s)) for i, s in enumerate(schedule) if s != 'x']
    a_phase, a_period = indexed_list[0]
    for b_phase, b_period in indexed_list[1:]:
        a_period, a_phase = combine(a_period, a_phase, b_period, -b_phase)
    return a_phase

def combine(a_period, a_phase, b_period, b_phase):
    gcd, s, _ = extended_gcd(a_period, b_period)
    phase_diff = a_phase - b_phase
    phase_diff_mult = phase_diff // gcd
    c_period = a_period // gcd * b_period
    c_phase = (a_phase - s * phase_diff_mult * a_period) % c_period
    return c_period, c_phase

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

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
# print('part1', part1(clean_input(test.strip().split('\n'))))
print('part2', part2(clean_input(input)))
# print('part2', part2(clean_input(test.strip().split('\n'))))
