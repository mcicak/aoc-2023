from functools import reduce

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


class Card:

    def __init__(self, line: str):
        self.id = int(line.split(":")[0].split()[-1])
        self.count = 1
        self.winning = [int(word.strip()) for word in line.split(":")[1].split("|")[0].split() if word.strip()]
        self.actual = [int(word.strip()) for word in line.split(":")[1].split("|")[1].split() if word.strip()]

    def winningNumbersCount(self):
        return len(set(self.winning).intersection(self.actual))

    def points(self) -> int:
        return int(2 ** (self.winningNumbersCount() - 1))


# PART 1
lines = read_file("/Users/mc/Desktop/advent2023/04/input.txt")
cards = list(map(lambda line: Card(line), lines))
# sum = reduce(lambda x, y: x + y, list(map(lambda x: x.points(), cards)))
# print("∑ = " + str(sum))

# PART 2

for i in range(len(cards)):
    card = cards[i]
    for j in range(card.winningNumbersCount()):
        card1 = cards[i + j + 1]
        card1.count += card.count

sum = reduce(lambda x, y: x + y, list(map(lambda x: x.count, cards)))
print(sum)
