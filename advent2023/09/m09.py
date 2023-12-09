from functools import reduce


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def stringToInts(string):
    return [int(s.strip()) for s in string.split() if s.strip()]


lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/09/input.txt"))


def process(line):
    # nums = stringToInts(line) # part 1
    nums = list(reversed(stringToInts(line))) # part 2

    allZeros = False
    diffs = []
    diffs.append(nums)
    while not allZeros:
        diff = []
        for i in range(len(nums) - 1):
            x1 = nums[i]
            x2 = nums[i + 1]
            dx = x2 - x1
            diff.append(dx)
        allZeros = all(list(map(lambda x: x == 0, diff)))
        diffs.append(diff)
        nums = diff

    for i in reversed(range(len(diffs))):
        if i == len(diffs) - 1:
            diffs[i].append(0)
            continue

        diffs[i].append(diffs[i + 1][-1] + diffs[i][-1])

    return diffs[0][-1]


sum = 0
for l in lines:
    sum += process(l)

print(sum)
