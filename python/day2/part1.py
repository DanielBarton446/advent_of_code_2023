from typing import Any

MAX_VALS = {"red": 12, "green": 13, "blue": 14}

def parse_line(line: str) -> Any:
    game_data = line.split(":")
    # game = game_data[0]
    data = game_data[1]

    rounds = data.split(";")

    max_vals = {}

    for round in rounds:
        actions = round.split(",")
        
        for a in actions:
            a = a.strip()            
            color_val = a.split(" ")
            data_point = [int(color_val[0]), color_val[1]]
            insert_max(max_vals, data_point)
    return max_vals

# TODO: make vals be Tuple[int, str]
def insert_max(d: dict, vals: Any): 
    number_of_cubes = vals[0]
    color = vals[1]
    if color in d.keys():
        if number_of_cubes > d.get(color):
            d.pop(color)
            d[color] = number_of_cubes
    else:
        d[color] = number_of_cubes


def is_valid_game(max_game_dict: dict) -> bool:
    for k,v in MAX_VALS.items():
        if v < max_game_dict[k]:
            return False
    return True
    

def main():
    with open("input.txt") as f:
        acc = 0
        for i,line in enumerate(f):
            max = parse_line(line)
            # print(max)
            if is_valid_game(max):
                acc += (i + 1)
        print(acc)

if __name__ == "__main__":
    main()
