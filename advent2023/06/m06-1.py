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


class Race:

    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance

    def successfulTimesCount(self):
        ret = 0
        for i in range(self.time):
            v = i
            t = self.time - i
            s = t * v
            if s > self.distance:
                ret += 1
        return ret


lines = read_file("/Users/mc/Desktop/advent2023/06/input.txt")
lines = [string for string in lines if string != ""]
times = stringToInts(lines[0].split(":")[1])
distances = stringToInts(lines[1].split(":")[1])
races = []

for i in range(len(times)):
    races.append(Race(times[i], distances[i]))

counts = list(map(lambda x: x.successfulTimesCount(), races))
p = reduce(lambda x, y: x * y, counts)
print(p)
