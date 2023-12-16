
from typing import Tuple, List, Set, Any


def parse_seeds(line: str) -> Set[int]:
    aux = line.split(": ")
    seeds = aux[1].split(" ")
    int_seeds = [int(x) for x in seeds]
    return set(int_seeds)

# On the seeds given, just do (seed, seed) as first, then (seed, soil) for the second set
def update_tuples(first: List[Tuple[int, int]] | Set[Tuple[int, int]],
                 second: List[Tuple[int, int]] | Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    # Surely there could be some set subtraction here or something
    updated_set = set()
    for a,b in first:
        missing_flag = True
        for x,y in second:
            if b == x:
                updated_set.add((a,y))
                missing_flag = False
        # Not certain we need this
        if missing_flag:
            updated_set.add((b,b))
    return updated_set

def create_mapping_list(dest_source_range: Any) -> List[Tuple[int, int]]:
    mapping_list = []
    dest = dest_source_range[0]
    source = dest_source_range[1]
    distance = dest_source_range[2]
    for i in range(0, distance):
        mapping_list.append((source + i, dest + i))

    return mapping_list

def parse_mapping_list(group: str):
    header_vals = group.split(":")
    vals = header_vals[1].split("\n")
    # clear up the /n splits getting '' in start
    vals.pop(0)
    maps = []
    for mapping in vals:
        str_list = mapping.split(" ")
        # hack because idk how to clean this better
        if str_list == ['']:
            continue
        int_list = [int(x) for x in str_list]

        mp = create_mapping_list(tuple(int_list))
        for val in mp:
            maps.append(val)
    return maps

def parse_input():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")

        seeds = parse_seeds(groups[0])
        seeds_set = [(x,x) for x in seeds]
        # Get mappings
        # Mappings
        final_list_mappings = seeds_set
        for g in groups[1::]:
            new_map = parse_mapping_list(g)
            final_list_mappings = update_tuples(final_list_mappings, new_map)
        print("SOLUTION:")
        print(min(final_list_mappings, key = lambda t: t[1]))



def main():
    parse_input()


if __name__ == "__main__":
    main()
