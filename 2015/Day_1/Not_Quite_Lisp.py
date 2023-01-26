"""A python solution of Advent of Code 2015 dDy 1
https://adventofcode.com/2015/day/1
"""


def get_final_pos(text):
    """return the final position of santa
    i.e. the difference in number of `(` and `)`"""
    return text.count("(") - text.count(")")


def get_first_basement(text):
    """"the position in the text where Santa first enters the basement"""

    floor = 0
    for i, c in enumerate(text):
        if c == "(":
            floor += 1
        else:
            floor -= 1

        if floor < 0:
            return i


if __name__ == "__main__":
    with open('./2015/Day_1/puzzle_input.txt', 'r') as f:
        text = f.readline()
        final_pos = get_final_pos(text)
        first_basement_pos = get_first_basement(text)

        print("Final position: ", final_pos)
        print("Position of the char that causes Santa to first enter the basement: ",
              first_basement_pos)
