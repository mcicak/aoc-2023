def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


class GameSet:

    def __init__(self, red, green, blue):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue

    def isValid(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14

    def power(self):
        return self.red * self.green * self.blue

    def __str__(self):
        return f"GameSet(red={self.red}, green={self.green}, blue={self.blue})"

class Game:

    def __init__(self, id):
        self.id = id
        self.sets = []

    def __str__(self) -> str:
        return str(id)

    def hasValidSet(self):
        return all(list(map(lambda game_set: game_set.isValid(), self.sets)))

    def minimumSet(self) -> GameSet:
        red = max(list(map(lambda x: x.red, self.sets)))
        green = max(list(map(lambda x: x.green, self.sets)))
        blue = max(list(map(lambda x: x.blue, self.sets)))
        return GameSet(red, green, blue)

def convertToGame(line):
    components = line.split(":")
    idString = components[0].replace("Game ", "")
    id = int(idString)
    game = Game(id)

    setsString = components[1]
    setsArray = list(map(lambda x: x.strip(), setsString.split(";")))

    for set in setsArray:
        cubeColorStrings = list(map(lambda x: x.strip(), set.split(",")))

        red = 0
        blue = 0
        green = 0
        for ccString in cubeColorStrings:
            if ccString.find("red") != -1:
                s1 = ccString.replace(" red", "")
                red = int(s1)

            if ccString.find("green") != -1:
                s1 = ccString.replace(" green", "")
                green = int(s1)

            if ccString.find("blue") != -1:
                s1 = ccString.replace(" blue", "")
                blue = int(s1)

        game.sets.append(GameSet(red, green, blue))

    return game


file_path = '/Users/mc/Desktop/advent2023/02/input.txt'
lines = read_file(file_path)

games = list(map(convertToGame, lines))

sum1 = 0
for game in games:
    if game.hasValidSet():
        sum1 += game.id

print(sum1)

minSets = list(map(lambda x: x.minimumSet(), games))
powers = sum(list(map(lambda x: x.power(), minSets)))
print(powers)
