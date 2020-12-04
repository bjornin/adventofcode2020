def part1(numbers):
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i] * numbers[j]

def part2(numbers):
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            for k in range(j,len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]


numbers = []
with open('./input.txt', 'r') as f:
    numbers = [int(x) for x in f]

print(part1(numbers))
print(part2(numbers))
