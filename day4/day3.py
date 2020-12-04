def part1(arg):
    needed = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
    valid = 0
    for i in arg:
        valid += all(x in sorted(i.keys()) for x in needed)
    return valid

def part2(arg):
    pass

input = []
with open('./input.txt', 'r') as f:
    input = [x.rstrip() for x in f]

def clean_input(input):
    cleaned = []
    user_dict = {}
    for i in input:
        if i == '':
            cleaned.append(user_dict.copy())
            user_dict.clear()
        else:
            for prop in i.split(' '):
                key, value = prop.split(':')
                user_dict.update({key: value})
    cleaned.append(user_dict.copy())
    return cleaned

print('input rows:', len(input))
cleaned_input = clean_input(input)
print('passports:', len(cleaned_input))
print('part1', part1(cleaned_input))
print('part2', part2(cleaned_input))
