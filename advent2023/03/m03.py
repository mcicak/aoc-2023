from array import array
from functools import reduce


class SchematicNumber:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.digits = len(str(value))

    def __repr__(self) -> str:
        return "(" + str(self.value) + ", " + str(self.x) + ", " + str(self.y) + ")"

    def isAdjacentToStar(self):
        if self.digits == 3:
            return True

        if self.digits == 2:
            return self.x in [1, 2, 3, 4]

        if self.digits == 1:
            return self.x in [2, 3, 4]

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def sumValidNumbers():
    sum = 0
    startIndex = 0
    endIndex = 0
    for num in numbers:
        lines1 = []
        block = ""

        if num.y > 0:
            lines1.append(lines[num.y - 1])
        lines1.append(lines[num.y])

        if num.y < 139:
            lines1.append(lines[num.y + 1])

        startIndex = num.x
        endIndex = num.x + num.digits

        if num.x > 0:
            startIndex -= 1

        if num.x + num.digits < 139:
            endIndex += 1

        lines1 = list(map(lambda x: x[startIndex:endIndex], lines1))
        block = block.join(lines1)

        for char in block:
            if not char.isnumeric() and not char == '.':
                sum += num.value
    return sum


def extractNumbers(lines):
    ret = []
    y = 0
    for line in lines:
        numBuilder = ""
        x = 0
        numX = 0

        for char in line:
            if char.isnumeric():
                if len(numBuilder) == 0:
                    numX = x
                numBuilder += char

                if x == len(line) - 1:
                    value = int(numBuilder)
                    ret.append(SchematicNumber(numX, y, value))
                    numBuilder = ""

            elif len(numBuilder) > 0:
                value = int(numBuilder)
                ret.append(SchematicNumber(numX, y, value))
                numBuilder = ""
            x += 1
        y += 1

    return ret


path = "/Users/mc/Desktop/advent2023/03/input.txt"
lines = list(read_file(path))
numbers = extractNumbers(lines)
sum = sumValidNumbers()


class Gear:
    num1 = 0
    num2 = 0
    starX = 0
    starY = 0


class Star:
    def __init__(self, x, y, starmap: []):
        self.x = x
        self.y = y
        self.starMap: array[str] = starmap
        self.gearNumbers = []
        self.numbers: array[SchematicNumber] = []

    def isGear(self):
        return len(self.gearNumbers) == 2

    def getRatio(self):
        return self.gearNumbers[0].value * self.gearNumbers[1].value

    def starmapAsString(self):
        return '\n'.join(self.starMap)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def extractNumbers(self):
        self.numbers = extractNumbers(self.starMap)

    def extractGearNumbers(self):
        self.gearNumbers = list(filter(lambda x: x.isAdjacentToStar(), self.numbers))

def extractStars(lines):
    ret = []
    y = 0

    for line in lines:
        x = 0
        for char in line:
            if char == '*':
                sm1 = lines[y - 1][x - 3:x + 4]
                sm2 = lines[y][x - 3:x + 4]
                sm3 = lines[y + 1][x - 3:x + 4]
                starmap = [sm1, sm2, sm3]
                ret.append(Star(x, y, starmap))
            x += 1
        y += 1

    return ret


print("START")

stars = extractStars(lines)

for star in stars:
    star.extractNumbers()
    star.extractGearNumbers()

gears = list(filter(lambda x: x.isGear(), stars))
sum = reduce(lambda x, y: x + y,list(map(lambda x: x.getRatio(), gears)))

print("∑ = " + str(sum))
