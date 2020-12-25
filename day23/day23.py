
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class CircularLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.cup = {}
        if nodes is not None:
            self.max = len(nodes)
            n = nodes.pop(0)
            node = Node(n)
            self.cup[n] = node
            self.head = node
            for n in nodes:
                node.next = Node(n)
                node = node.next
                self.cup[n] = node
            node.next = self.head
    
    def __repr__(self):
        n = self.head
        ns = []
        while n is not None:
            ns.append(str(n))
            n = n.next
            if n is self.head:
                break
        return ','.join(ns)

    def move(self, src):
        chunk = src.next
        dst = self.get_dst(src, chunk)
        src.next = chunk.next.next.next
        chunk.next.next.next = dst.next
        dst.next = chunk

    def get_dst(self, src, exclude):
        exclude_values = [exclude.value, exclude.next.value, exclude.next.next.value]
        n = src
        v = n.value - 1
        if v == 0:
            v = self.max
        while v in exclude_values:
            v -= 1
            if v == 0:
                v = self.max
        n = self.get(v)
        return n

    def get(self, value):
        return self.cup[value]

def part1(arg, pad_to, turns):
    c = solve(arg, pad_to, turns)
    n = c.get(1).next
    ret = ''
    while n.value != 1:
        ret += str(n.value)
        n = n.next
    return ret

def part2(arg, pad_to, turns):
    c = solve(arg, pad_to, turns)
    n = c.get(1)
    return n.next.value * n.next.next.value

def solve(arg, pad_to, turns):
    circle = create_circle(arg, pad_to)
    current_cup = circle.head
    for _ in range(turns):
        circle.move(current_cup)
        current_cup = current_cup.next
    return circle

def create_circle(input, maxlen):
    cups = [int(i) for i in input] + list(range(len(input) + 1,maxlen + 1))
    cup_list = CircularLinkedList(cups)
    return cup_list

input = '712643589'
test_input = '389125467'

print('part1', part1(input, 0, 100))
# print('part1', part1(test_input, 0, 10))
print('part2', part2(input, 1000000, 10000000))
# print('part2', part2(test_input, 0, 10))
