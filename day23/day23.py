from collections import deque

def part1(arg):
    circle = deque([int(i) for i in arg], maxlen=len(arg))
    current_cup = circle[0]
    for _ in range(100):
        yanked = yank_after(current_cup, 3, circle)
        dest_cup = get_destination_cup(current_cup, circle)
        put_after(dest_cup, yanked, circle)
        next_current_cup_index = (circle.index(current_cup) + 1) % len(circle)
        current_cup = circle[next_current_cup_index]
    return get_answer(circle)

def get_answer(circle):
    start = circle.index(1)
    circle.rotate(-start)
    ans = ''
    for i in range(1,len(circle)):
        ans += str(circle[i])
    return ans

def put_after(cup, values, circle):
    rot = circle.index(cup) + 1
    circle.rotate(-rot)
    for i in values[::-1]:
        circle.appendleft(i)
    circle.rotate(rot)

def yank_after(cup, count, circle):
    rot = circle.index(cup) + 1
    ret = []
    circle.rotate(-rot)
    for _ in range(count):
        ret.append(circle.popleft())
    circle.rotate(rot)
    return ret

def get_destination_cup(current_cup, circle):
    target = current_cup - 1
    while True:
        if target < min(circle):
            target = max(circle)
        try:
            ind = circle.index(target)
            return circle[ind]
        except ValueError:
            target -= 1

def part2(arg):
    pass

input = '712643589'
test_input = '389125467'

print('part1', part1(input))
# print('part1', part1(test_input))
# print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
