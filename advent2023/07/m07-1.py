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


cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:

    def __init__(self, hand, bid):
        self.hand = list(hand)
        self.bid = bid

        self.cardTypeCounts = {}

        for card in hand:
            self.cardTypeCounts[card] = self.cardTypeCounts.get(card, 0) + 1

        self.sortedCardTypeCounts = list(reversed(sorted(list(self.cardTypeCounts.values()))))

    def type(self):
        if len(self.sortedCardTypeCounts) == 1:
            return 7

        if self.sortedCardTypeCounts[0] == 4:
            return 6

        if len(self.sortedCardTypeCounts) == 2 and self.sortedCardTypeCounts[0] == 3:
            return 5

        if len(self.sortedCardTypeCounts) == 3 and self.sortedCardTypeCounts[0] == 3:
            return 4

        if len(self.sortedCardTypeCounts) == 3 and self.sortedCardTypeCounts[0] == 2:
            return 3

        if len(self.sortedCardTypeCounts) == 4:
            return 2

        return 1

    def __lt__(self, other):
        if self.type() != other.type():
            return self.type() > other.type()

        for i in range(5):
            myCard = self.hand[i]
            otherCard = other.hand[i]
            myIndex = cards.index(myCard)
            otherIndex = cards.index(otherCard)
            if myIndex != otherIndex:
                return myIndex < otherIndex

        return False

    def __eq__(self, other):
        return self.hand == other.hand and self.bid == other.bid

    def rank(self):
        print("1")


lines = read_file("/Users/mc/Desktop/aoc-2023/advent2023/07/input.txt")
hands = list(map(lambda x: Hand(x.split()[0], int(x.split()[1])), lines))
sortedHands = list(reversed(sorted(hands)))

sum = 0
for i in range(len(sortedHands)):
    hand = sortedHands[i]
    sum += hand.bid * (i+1)

print(sum)
