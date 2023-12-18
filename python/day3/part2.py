from typing import List


# let's just do everything as though it were flattened, and
# then do math on it since we have a non-jagged map
class IslandNode:

    def __init__(self, width, height, idx) -> None:
        self.neighbor_indicies: List[int] = []
        self.island_node_indicies: List[int] = []
        self.add_neighbors(width, height, idx)

    def add_neighbors(self, width, height, idx):
        # add the node to our island
        self.island_node_indicies.append(idx)

        if idx in self.neighbor_indicies:
            # we have another node in our island
            self.neighbor_indicies.remove(idx)

        row = idx // width
        col = idx % width
        relative_positions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        for dx, dy in relative_positions:
            new_row = row + dx
            new_col = col + dy

            # simply make sure it's within bounds
            if 0 <= new_row < height and 0 <= new_col < width:
                pos = new_row * width + new_col
                self.neighbor_indicies.append(pos)


class Islands:
    width: int = 0
    height: int = 0
    islands: List[IslandNode] = []
    checks: List[int] = []
    map: str = ""


    def __init__(self, width, height, map: str) -> None:
        self.width = width
        self.height = height
        self.map = map
        for idx,c in enumerate(map):
            sovereign_island = True
            if c.isdigit():
                # ew. We should have a better datastructure
                for land in self.islands:
                    if idx in land.neighbor_indicies:
                        land.add_neighbors(self.width, self.height, idx)
                        sovereign_island = False
                if sovereign_island:
                    new_island = IslandNode(self.width, self.height, idx)
                    self.islands.append(new_island)
            if c in "*":
                self.checks.append(idx)

    def island_value(self, island_id: int) -> int:
        isl = self.islands[island_id]
        power = 0
        accum = 0
        for x in range(len(isl.island_node_indicies) - 1, -1, -1):
            accum += int(self.map[isl.island_node_indicies[x]]) * pow(10, power)
            power += 1
        return accum

            

def parse_input(filename: str) -> str:
    single_line = ""
    with open(filename) as f:
        single_line = f.read().replace("\n", '')
    return single_line


def main():
    # world = parse_input("test.txt")
    world = parse_input("input.txt")
    # mapified = Islands(10, 10, world)
    mapified = Islands(140, 140, world)
    # ew
    accum = 0
    for check in mapified.checks:
        ids = []
        for id,land in enumerate(mapified.islands):
            if check in land.neighbor_indicies:
                ids.append(id)
        if len(ids) == 2:
            first = mapified.island_value(ids[0]) 
            second = mapified.island_value(ids[1]) 
            accum += first * second

    print(accum)


if __name__ == "__main__":
    main()
