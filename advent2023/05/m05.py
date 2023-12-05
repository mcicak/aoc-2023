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


class MapItem:

    def __init__(self, source, destination, range):
        self.source = source
        self.destination = destination
        self.range = range

    @staticmethod
    def createItem(itemString: str):
        return MapItem(0, 0, 0)


class AlmanacMap:

    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.map = {}

    def destForSource(self, source) -> int:
        for item in self.items:
            if source >= item.source and source < item.source + item.range:
                return item.destination + source - item.source

        return source


class Almanac:
    def __init__(self, seeds, maps):
        self.seeds = seeds
        self.maps = maps


#lines = read_file("/Users/mc/Desktop/advent2023/05/input-small.txt")
lines = read_file("/Users/mc/Desktop/advent2023/05/input.txt")
lines = [string for string in lines if string != ""]

almanacMaps = []
seeds = []
almanacMap = AlmanacMap("", [])

for line in lines:

    if line.startswith("seeds"):
        seeds = stringToInts(line.split(":")[1])
        seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    if line.endswith("map:"):
        partName = line.replace(" map:", "")
        if len(almanacMap.items) > 0:
            almanacMaps.append(almanacMap)
        almanacMap = AlmanacMap(partName, [])

    if line[0].isnumeric():
        values = stringToInts(line)
        almanacMap.items.append(MapItem(values[1], values[0], values[2]))

almanacMaps.append(almanacMap)
almanac = Almanac(seeds, almanacMaps)

locations = []

for seedRange in almanac.seeds:
    for seed in range(seedRange[0], seedRange[0] + seedRange[1]):
        if seed == 82:
            print("stop")
        hasNextMap = True
        i = 0
        source = seed
        while hasNextMap:
            nextMap = almanac.maps[i]
            i += 1
            source = nextMap.destForSource(source)
            hasNextMap = len(almanac.maps) > i
            if not hasNextMap:
                locations.append(source)

print(min(locations))
