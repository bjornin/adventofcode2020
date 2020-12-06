from  functools import reduce

def part1(arg):
    ans = 0
    for i in arg:
        merged_unique = set(reduce(lambda a,b: a+b,i.values()))
        ans += len(merged_unique)
    return ans

def part2(arg):
    ans = 0
    for i in arg:
        all_ans = i[0]
        for j in range(1, len(i)):
            all_ans = set(all_ans).intersection(i[j])
        ans += len(all_ans)
    return ans

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

def clean_input(input):
    cleaned = []
    user_dict = {}
    group = 0
    for i in input:
        if i == '':
            cleaned.append(user_dict.copy())
            user_dict.clear()
            group = 0 
        else:
            user_dict.update({group: i})
            group += 1
    cleaned.append(user_dict.copy())
    return cleaned

print('input rows:', len(input))
print('part1', part1(clean_input(input)))
print('part2', part2(clean_input(input)))
