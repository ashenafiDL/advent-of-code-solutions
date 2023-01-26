"""A python solution of Advent of Code 2015 dDy 1
https://adventofcode.com/2015/day/2
"""


def get_area(line):
    sides = line.split('x')

    area1 = 2 * int(sides[0]) * int(sides[1])
    area2 = 2 * int(sides[0]) * int(sides[2])
    area3 = 2 * int(sides[1]) * int(sides[2])

    return area1 + area2 + area3 + (min(area1, area2, area3) // 2)


def get_length(line):
    sides = [int(i) for i in line.split('x')]
    sides = sorted(sides)

    ribbon = (2*sides[0]) + (2*sides[1])
    bow = sides[0] * sides[1] * sides[2]

    return ribbon + bow


if __name__ == "__main__":
    with open("./2015/Day_2/puzzle_input.txt", 'r') as f:

        line = f.readline()
        total_area = 0
        total_length = 0

        while line != "":
            area = get_area(line.strip())
            length = get_length(line.strip())

            total_area += area
            total_length += length

            line = f.readline()

        print("Total area: ", total_area)
        print("Total length: ", total_length)
