
from typing import Tuple, List, Set, Any


def parse_seeds(line: str) -> Set[int]:
    aux = line.split(": ")
    seeds = aux[1].split(" ")
    int_seeds = [int(x) for x in seeds]
    return set(int_seeds)

def transform_if_in_range(dest_source_ranges: List[Tuple[int, int, int]], cur: int, solutions: List[int]) -> int:
    for dsr in dest_source_ranges:
        dest = dsr[0]
        source = dsr[1]
        distance = dsr[2]
        if source <= cur and cur <= source + distance:
            potential_answer = dest + (cur - source)
            solutions.append(potential_answer)
            if cur in solutions:
                solutions.remove(cur)
            return potential_answer
    if cur not in solutions:
        solutions.append(cur)
    return cur

def parse_range_tuples(group: str) -> List[Tuple[int, int, int]]:
    header_vals = group.split(":")
    vals = header_vals[1].split("\n")
    range_tuples = []
    for mapping in vals:
        # hack for dealing with things I should have cleaned
        if mapping == '':
            continue
        str_list = mapping.split(" ")
        int_list = [int(x) for x in str_list]
        range_tuples.append(tuple(int_list))
    return range_tuples


def parse_input():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")

        seeds = parse_seeds(groups[0])
        # Get mappings
        # Mappings
        solutions = []
        for s in seeds:
            cur = s
            for g in groups[1::]:
                new_map = parse_range_tuples(g)
                cur = transform_if_in_range(new_map, cur, solutions)
        print("SOLUTION:")
        print(solutions)
        print(min(solutions))



def main():
    parse_input()


if __name__ == "__main__":
    main()
