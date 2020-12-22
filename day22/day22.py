from collections import deque
from itertools import islice

def part1(arg):
    player1, player2 = parse_input(arg)
    return regular_play(player1, player2)

def part2(arg):
    player1, player2 = parse_input(arg)
    return recursive_play(player1, player2)[1]

def regular_play(p1, p2):
    while (len(p1) > 0 and len(p2) > 0):
        card1 = p1.popleft()
        card2 = p2.popleft()
        if card1 > card2:
            put_deck(p1, card1, card2)
        else:
            put_deck(p2, card2, card1)
    score = calc_score(p1 if len(p1) else p2)
    return score

def recursive_play(p1,p2):
    # print('new game')
    mem = {}
    force_p1 = False
    while (len(p1) > 0 and len(p2) > 0):
        if is_recursion(mem, p1, p2):
            force_p1 = True
            break
        card1 = p1.popleft()
        card2 = p2.popleft()
        # print('new round', card1, card2)
        if card1 <= len(p1) and card2 <= len(p2):
            pp1 = deque(islice(p1, 0, card1))
            pp2 = deque(islice(p2, 0, card2))
            if recursive_play(pp1, pp2)[0]:
                put_deck(p1, card1, card2)
            else:
                put_deck(p2, card2, card1)
        elif card1 > card2:
            put_deck(p1, card1, card2)
        else:
            put_deck(p2, card2, card1)
    winner = force_p1 or len(p1) > len(p2)
    score = calc_score(p1 if winner else p2)
    return winner, score

def is_recursion(mem, p1, p2):
    key1 = 'p1'+str(list(p1))
    key2 = 'p2'+str(list(p2))
    seen = mem.get(key1, False) or mem.get(key2, False)
    mem[key1] = True
    mem[key2] = True
    return seen

def calc_score(deck):
    return sum(map(lambda v, m: v * m, deck, range(len(deck), 0, -1)))

def put_deck(deck, c1, c2):
    deck.extend([c1, c2])

def parse_input(input):
    player = 0
    decks = {}
    deck = deque()
    for i in input:
        if i.startswith('Player'):
            player += 1
        elif i == '':
            decks.setdefault(player, deck)
            deck = deque()
        else:
            deck.append(int(i))
    decks.setdefault(player, deck)
    return decks[1], decks[2]

def get_input(filename):
    input = []
    with open(filename, 'r') as f:
        input = [x.strip() for x in f]
    return input

# print('part1', part1(get_input('./input.txt')))
# print('part1', part1(get_input('./test_input.txt')))
print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
