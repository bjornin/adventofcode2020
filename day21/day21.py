from collections import namedtuple

Food = namedtuple('food', 'ingredients allergens')

def part1(arg):
    foods = parse_input(arg)
    allergens, ingr_occurance = parse_food(foods)
    found_allergens = set()
    for ingr in allergens.values():
        for i in ingr:
            found_allergens.add(i)
    ans = sum([ingr_occurance[a] for a in set(ingr_occurance.keys()).difference(found_allergens)])
    return ans

def part2(arg):
    foods = parse_input(arg)
    allergens, _ = parse_food(foods)
    ans = ','.join([''.join(v) for k, v in sorted(allergens.items())])
    return ans

def parse_food(foods):
    ingr_occurance = {}
    allr_filter = {}
    for ingr, allr in foods:
        for a in allr:
            allr_filter[a] = allr_filter.get(a,set())
            if len(allr_filter[a]) == 0:
                allr_filter[a] = set(ingr)
            else:
                allr_filter[a].intersection_update(set(ingr))
        for i in ingr:
            ingr_occurance[i] = ingr_occurance.get(i, 0)
            ingr_occurance[i] += 1
    allergens = {}
    while len(allr_filter) > 0:
        done = [key for key, val in allr_filter.items() if len(val) == 1]
        for d in done:
            allergens.setdefault(d, allr_filter.pop(d))
        for a_rem in allergens.values():
            for a in allr_filter:
                allr_filter[a].difference_update(a_rem)
    return allergens, ingr_occurance

def parse_input(input):
    foods = []
    for i in input:
        ingr, allr = i.split('(')
        ingredients = set(ingr.strip().split(' '))
        allergens = set()
        for a in allr.split(','):
            m = a.replace('contains', '').replace(')','').strip()
            allergens.add(m)
        foods.append(Food(ingredients, allergens))
    return foods
        
def get_input(filename):
    input = []
    with open(filename, 'r') as f:
        input = [x.strip() for x in f]
    return input

print('part1', part1(get_input('./input.txt')))
# print('part1', part1(get_input('./test_input.txt')))
print('part2', part2(get_input('./input.txt')))
# print('part2', part2(get_input('./test_input.txt')))
