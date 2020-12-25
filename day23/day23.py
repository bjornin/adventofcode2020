from collections import deque
from array import array

def solve(arg, pad_to, turns):
    circle = create_circle(arg, pad_to)
    current_cup_index = 0
    # print(circle)
    for i in range(turns):
        if i % 1000 == 0:
            print(i)
        current_cup_value = circle[current_cup_index]
        yanked_index = [(current_cup_index + i) % len(circle) for i in range(1,4)]
        dest_cup_index = get_dest_cup(current_cup_value, yanked_index, circle)
        # print(circle, current_cup_value, circle[dest_cup_index], [circle[i] for i in yanked_index])
        move(current_cup_index, dest_cup_index, yanked_index, circle)
        # print(circle)
        current_cup_index = (circle.index(current_cup_value) + 1) % len(circle)
    return get_answer_2(circle)

def get_dest_cup(current_cup_value, yanked_index, circle):
    target = current_cup_value - 1
    yanked = [circle[i] for i in yanked_index]
    while True:
        if target < min(circle): # save for optimization
            target = max(circle) # save for optimization
        if target in yanked:
            target -= 1
        else:
            break
    return circle.index(target)

def move(current_cup_index, dest_cup_index, yanked_index, circle):
    upper = [x for x in yanked_index if x > dest_cup_index]
    lower = sorted(list(set(yanked_index).difference(upper)))
    # print(lower, upper)
    if lower:
        yank_slice = slice(lower[0], lower[-1] + 1)
        put_slice = slice(dest_cup_index - len(lower) + 1, dest_cup_index + 1)
        l_fill_slice = slice(lower[0], dest_cup_index - len(lower) + 1)
        r_fill_slice = slice(lower[-1] + 1, dest_cup_index + 1)
        circle[put_slice], circle[l_fill_slice] = circle[yank_slice], circle[r_fill_slice]
    if upper:
        dest_cup_index -= len(lower)
        yank_slice = slice(upper[0], upper[-1] + 1)
        put_slice = slice(dest_cup_index + 1, dest_cup_index + len(upper) + 1)
        l_fill_slice = slice(dest_cup_index + 1, upper[0])
        r_fill_slice = slice(dest_cup_index + len(upper) + 1, upper[-1] + 1)
        circle[r_fill_slice], circle[put_slice] = circle[l_fill_slice], circle[yank_slice]


def get_answer_1(circle):
    start = circle.index(1) + 1
    ans = ''.join(str(circle[(i + start) % len(circle)]) for i in range(len(circle) - 1))
    return ans

def create_circle(input, maxlen):
    cup_list = array('I', [int(i) for i in input] + list(range(len(input) + 1,maxlen + 1)))
    return cup_list

def get_answer_2(circle):
    ind = circle.index(1)
    if ind == len(circle) - 1:
        ind = -1
    return circle[ind + 1] * circle[ind + 2]


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


input = '712643589'
test_input = '389125467'

# print('part1', solve(input, 0, 100))
# print('part1', solve(test_input, 0, 100))
print('part2', solve(input, 1000000, 400))
