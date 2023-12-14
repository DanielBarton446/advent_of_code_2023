import re

def translate_word(word: str) -> int:
    if len(word) == 1:
        return int(word)
    else:
        match word:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9
    raise ValueError("Couldnt' find a digit in: " + word)



def get_first(line: str) -> int:
    forward_regex = r"one|two|three|four|five|six|seven|eight|nine|\d"
    groups = re.search(forward_regex, line)
    if groups is not None:
        return translate_word(groups[0])
    raise ValueError("Unable to parse a number")


def get_last(line: str) -> int:
    backwards_regex = r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d"
    line = line[::-1] # inverse the line
    groups = re.search(backwards_regex, line)
    if groups is not None:
        to_check = groups[0]
        return translate_word(to_check[::-1])
    raise ValueError("Unable to parse a number")


def main():
    lines = open("input.txt").readlines()
    vals = []
    for line in lines:
        # print("Line: " + str(line).strip('\n')) 
        first = get_first(line)
        # print("First:" + str(first))
        last = get_last(line)
        # print("Last:" + str(last))
        val = (first * 10) + last 
        # print(val)
        vals.append(val)
    print(sum(vals))

if __name__ == "__main__":
    main()

