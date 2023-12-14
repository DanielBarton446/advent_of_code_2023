def get_last(line: str) -> int:
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
    raise ValueError("No digit found")


def get_first(line: str) -> int:
    for c in line:
        if c.isdigit():
            return int(c)
    raise ValueError("No digit found")




def main():
    lines = open("input.txt").readlines()
    sum = 0
    for line in lines:
        first = get_first(line)
        last = get_last(line)
        sum += (first * 10) + last
    print(sum)


if __name__ == "__main__":
    main()
