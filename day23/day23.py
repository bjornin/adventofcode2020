from collections import deque
from array import array

def part1(arg):
    circle = create_circle(arg, len(input))
    current_cup = circle[0]
    for _ in range(100):
        yanked = yank_after(current_cup, 3, circle)
        dest_cup = get_destination_cup(current_cup, circle)
        put_after(dest_cup, yanked, circle)
        next_current_cup_index = (circle.index(current_cup) + 1) % len(circle)
        current_cup = circle[next_current_cup_index]
    return get_answer_1(circle)

def part2(arg):
    circle = create_circle(arg, 1000000)
    current_cup = circle[0]
    for turn in range(10000000):
        if turn % 100000 == 0:
            print(turn)
        yanked = yank_after(current_cup, 3, circle)
        dest_cup = get_destination_cup(current_cup, circle)
        put_after(dest_cup, yanked, circle)
        next_current_cup_index = (circle.index(current_cup) + 1) % len(circle)
        current_cup = circle[next_current_cup_index]
    return get_answer_2(circle)

def create_circle(input, maxlen):
    cup_list = [int(i) for i in input] + list(range(len(input))
    # cup_list = [int(i) for i in input] + list(range(len(input) + 1,maxlen + 1))
    return cup_list

def get_answer_2(circle):
    ind = circle.index(1)
    if ind == len(circle) - 1:
        ind = -1
    return circle[ind + 1] * circle[ind + 2]

def get_answer_1(circle):
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

input = '712643589'
test_input = '389125467'

# print('part1', part1(input))
# print('part1', part1(test_input))
# print('part2', part2(input))
print('part2', part2(test_input))
