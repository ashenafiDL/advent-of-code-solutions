"""A python solution of Advent of Code 2015 dDy 1
https://adventofcode.com/2015/day/3
"""


def at_least_one_present(text):
    x, y = 0, 0

    pos = (x, y)
    pos_list = set()
    pos_list.add(pos)

    for c in text:
        if c == '<':
            x -= 1
        elif c == ">":
            x += 1
        elif c == "^":
            y += 1
        elif c == "v":
            y -= 1

        pos = (x, y)
        pos_list.add(pos)

    return len(pos_list)


def with_robot_santa(text):
    x_santa, y_santa, x_robot, y_robot = 0, 0, 0, 0

    pos_santa = (x_santa, y_santa)
    pos_robot = (x_robot, y_robot)

    pos_list = set()
    pos_list.add(pos_santa)
    pos_list.add(pos_robot)

    for i, c in enumerate(text):

        if i % 2 == 0:
            if c == '<':
                x_santa -= 1
            elif c == ">":
                x_santa += 1
            elif c == "^":
                y_santa += 1
            elif c == "v":
                y_santa -= 1

            pos_santa = (x_santa, y_santa)
            pos_list.add(pos_santa)
        else:
            if c == '<':
                x_robot -= 1
            elif c == ">":
                x_robot += 1
            elif c == "^":
                y_robot += 1
            elif c == "v":
                y_robot -= 1

            pos_robot = (x_robot, y_robot)
            pos_list.add(pos_robot)

    return len(pos_list)


if __name__ == "__main__":
    with open("./2015/Day_3/puzzle_input.txt", 'r') as f:
        text = f.readline()

        print("No of houses that receive at least one present: ",
              at_least_one_present(text))
        print("With the help of Robot Santa: ", with_robot_santa(text))
