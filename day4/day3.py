import re

def part1(arg):
    needed = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    valid = 0
    for i in arg:
        valid += all(x in i.keys() for x in needed)
    return valid

def check_byr(v):
    return v >= 1920 and v <=2002

def check_iyr(v):
    return v >= 2010 and v <=2020

def check_eyr(v):
    return v >= 2020 and v <=2030
    
def check_hgt(v):
    ok = False
    if v.endswith('cm'):
        h = int(v[:-2])
        ok = (h >= 150 and h <= 193)
    elif v.endswith('in'):
        h = int(v[:-2])
        ok = (h >= 59 and h <= 76)
    return ok

def check_hcl(v):
    pattern = r'^#[0-9a-f]{6}$'
    return re.match(pattern, v)

def check_ecl(v):
    return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
def check_pid(v):
    pattern = r'^\d{9}$'
    return re.match(pattern, v)

def part2(arg):
    needed = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    valid = 0
    for i in arg:
        if all(x in i.keys() for x in needed) and \
            check_byr(int(i['byr'])) and \
            check_iyr(int(i['iyr'])) and \
            check_eyr(int(i['eyr'])) and \
            check_hgt(i['hgt']) and \
            check_hcl(i['hcl']) and \
            check_ecl(i['ecl']) and \
            check_pid(i['pid']):
                valid += 1
    return valid

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
