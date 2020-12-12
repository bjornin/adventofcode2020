from math import sin, cos, radians

def move(pos, heading, value):
    if heading == 0: # north
        pos['lat'] += value
    elif heading == 90: # east
        pos['long'] += value
    elif heading == 180: # east
        pos['lat'] -= value
    elif heading == 270: # east
        pos['long'] -= value

def part1(arg):
    pos = {'lat': 0, 'long': 0}
    heading = 90
    for i in arg:
        instruction = i[0]
        value = int(i[1:])
        if instruction == 'R':
            heading = (heading + value) % 360
        elif instruction == 'L':
            heading = (heading - value) % 360
        elif instruction == 'F':
            move(pos, heading, value)
        elif instruction == 'N':
            move(pos, 0, value)
        elif instruction == 'E':
            move(pos, 90, value)
        elif instruction == 'S':
            move(pos, 180, value)
        elif instruction == 'W':
            move(pos, 270, value)
    return abs(pos['lat']) + abs(pos['long'])
        
def move_to_wp(pos, wp, value):
    pos['lat'] += wp['lat'] * value
    pos['long'] += wp['long'] * value

def part2(arg):
    pos = {'lat': 0, 'long': 0}
    wp = {'lat': 1, 'long': 10}
    for i in arg:
        instruction = i[0]
        value = int(i[1:])
        if instruction == 'R':
            rad = radians(-value)
            longitude = wp['long']
            latitude = wp['lat']
            wp['long'] = round(cos(rad) * longitude - sin(rad) * latitude)
            wp['lat'] = round(sin(rad) * longitude + cos(rad) * latitude)
        elif instruction == 'L':
            rad = radians(value)
            longitude = wp['long']
            latitude = wp['lat']
            wp['long'] = round(cos(rad) * longitude - sin(rad) * latitude)
            wp['lat'] = round(sin(rad) * longitude + cos(rad) * latitude)
        elif instruction == 'F':
            move_to_wp(pos, wp, value)
        elif instruction == 'N':
            wp['lat'] += value
        elif instruction == 'E':
            wp['long'] += value
        elif instruction == 'S':
            wp['lat'] -= value
        elif instruction == 'W':
            wp['long'] -= value
    return abs(pos['lat']) + abs(pos['long'])

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

test = """
F10
N3
F7
R90
F11
"""
test2 = """
L90
L180
L270
"""

print('input rows:', len(input))
print('part1', part1(input))
# print('part1', part1(test.strip().split('\n')))
print('part2', part2(input))
# print('part2', part2(test2.strip().split('\n')))
