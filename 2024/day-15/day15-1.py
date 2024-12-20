#!/usr/bin/env python3

"""
--- Day 15: Warehouse Woes ---

You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; 
maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer inspection, they seem quite anxious, 
so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. 
That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important 
warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or 
lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, 
if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make (your puzzle input). 
The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot 
difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^

As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes. 
However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead, including the robot. 
The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will attempt to make, 
in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. 
Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<

Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########

The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. 
The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from 
the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 from the left edge of the map, 
resulting in a GPS coordinate of 100 * 1 + 4 = 104.

#######
#...O..
#......

The lanternfish would like to know the sum of all boxes' GPS coordinates after the robot finishes moving. In the larger example, 
the sum of all boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of 
all boxes' GPS coordinates?


Solution:
Create "Warehouse" class representing warehouse map and "Robot" class representing the robot.
Provide "Robot" instance access to the warehouse instance.
Create move methods for the Robot. These methods verify if move is possible, update warehouse map and robot's coordinates.
Create warehouse method to visualize current status.
"""


import sys
import os
import time
from colorama import just_fix_windows_console, Fore, Back, Style
sys.path.append('..')
from aoc import load_input


class Warehouse:
    """Class representing warehouse
    """
    def __init__(self, input: list[str]) -> None:
        self.map = []     # warehouse map
        self.moves = ''   # robot's moves
        # Load warehouse map and robot's movements
        for line_number, input_line in enumerate(input):
            if input_line == '':
                continue
            elif input_line[0] == '#':
                self.map.append(list(input_line))
            elif input_line[0] in '<^>v':
                self.moves += input_line
        # get warehouse size
        self.x_size = len(self.map[0])
        self.y_size = len(self.map)

    def get_robot(self) -> tuple[int, int]:
        """Find robot's coordinates on the warehouse map

        Raises:
            ValueError: if robot is missing

        Returns:
            tuple[int, int]: x and y coordinates of the robot
        """
        for y_coordinate, row in enumerate(self.map):
            try:
                x_coordinate = row.index('@')
            except ValueError:
                # continue if robot isn't found in current row
                continue
            return x_coordinate, y_coordinate
        raise ValueError("Robot wasn't found in the warehouse.")
    
    def show(self, movement: str) -> None:
        _ = os.system("clear")
        for row in self.map:
            print(''.join(row).replace('@', f"{Fore.RED + movement + Style.RESET_ALL}"))

    def calculate_gps_coordinates(self) -> int:
        total = 0
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == 'O':
                    total += 100 * y + x
        return total

class Robot:
    """Class representing robot
    """
    def __init__(self, warehouse: Warehouse, coordinates: tuple[int, int]) -> None:
        self.warehouse = warehouse         # link warehouse instance to the robot instance
        self.x_coordinate = coordinates[0] # robot's current coordinates
        self.y_coordinate = coordinates[1] # robot's current coordinates

    def move(self, direction: str) -> None:
        Robot.move_method[direction](self)

    def move_up(self) -> None:
        next_cell = self.warehouse.map[self.y_coordinate-1][self.x_coordinate]
        if next_cell == '.':
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
            self.y_coordinate -= 1
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
        elif next_cell == 'O':
            for y in range(self.y_coordinate-1, 0, -1):
                if self.warehouse.map[y][self.x_coordinate] == '#':
                    break
                elif self.warehouse.map[y][self.x_coordinate] == '.':
                    self.warehouse.map[y][self.x_coordinate] = 'O'
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
                    self.y_coordinate -= 1
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
                    break

    def move_down(self) -> None:
        next_cell = self.warehouse.map[self.y_coordinate+1][self.x_coordinate]
        if next_cell == '.':
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
            self.y_coordinate += 1
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
        elif next_cell == 'O':
            for y in range(self.y_coordinate+1, self.warehouse.y_size):
                if self.warehouse.map[y][self.x_coordinate] == '#':
                    break
                elif self.warehouse.map[y][self.x_coordinate] == '.':
                    self.warehouse.map[y][self.x_coordinate] = 'O'
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
                    self.y_coordinate += 1
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
                    break

    def move_right(self) -> None:
        next_cell = self.warehouse.map[self.y_coordinate][self.x_coordinate+1]
        if next_cell == '.':
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
            self.x_coordinate += 1
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
        elif next_cell == 'O':
            for x in range(self.x_coordinate+1, self.warehouse.x_size):
                if self.warehouse.map[self.y_coordinate][x] == '#':
                    break
                elif self.warehouse.map[self.y_coordinate][x] == '.':
                    self.warehouse.map[self.y_coordinate][x] = 'O'
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
                    self.x_coordinate += 1
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
                    break

    def move_left(self) -> None:
        next_cell = self.warehouse.map[self.y_coordinate][self.x_coordinate-1]
        if next_cell == '.':
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
            self.x_coordinate -= 1
            self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
        elif next_cell == 'O':
            for x in range(self.x_coordinate-1, 0, -1):
                if self.warehouse.map[self.y_coordinate][x] == '#':
                    break
                elif self.warehouse.map[self.y_coordinate][x] == '.':
                    self.warehouse.map[self.y_coordinate][x] = 'O'
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '.'
                    self.x_coordinate -= 1
                    self.warehouse.map[self.y_coordinate][self.x_coordinate] = '@'
                    break
    
    # map of move symbols to the robot's move methods
    move_method = {
        '^': move_up,
        'v': move_down,
        '<': move_left,
        '>': move_right,
    }


def main() -> None:
    just_fix_windows_console()   # enable ASCII color sequences on the windows
    input = load_input()
    warehouse = Warehouse(input)
    robot_coordinates = warehouse.get_robot()
    robot = Robot(warehouse, robot_coordinates)
    for movement in warehouse.moves:
        robot.move(movement)
        warehouse.show(movement)
        time.sleep(0.2)

    gps_sum = warehouse.calculate_gps_coordinates()

    print(f"Sum of all GPS coordinates: {gps_sum}")


if __name__ == "__main__":
    main()
