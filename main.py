import os
from time import sleep

base_grid = [[3, 0, 0, 6, 0, 8, 0, 0, 0],
             [0, 0, 0, 7, 0, 0, 2, 0, 9],
             [0, 4, 0, 0, 0, 2, 0, 1, 0],
             [0, 0, 6, 0, 0, 9, 7, 2, 0],
             [2, 5, 3, 4, 0, 0, 0, 8, 0],
             [1, 0, 0, 0, 0, 0, 5, 0, 0],
             [0, 0, 2, 0, 4, 0, 0, 7, 0],
             [5, 0, 0, 0, 0, 0, 1, 0, 0],
             [6, 1, 0, 0, 0, 0, 0, 0, 0]
             ]


def valid(grid: list, row: int, col: int, number: int):
    for x in range(9):
        if grid[row][x] == number:  # check column
            return False

    for x in range(9):
        if grid[x][col] == number:  # check row
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3
    for i in range(3):  # check square
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False

    return True


def solve(grid: list, row: int, col: int):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for number in range(1, 10):
        if valid(grid, row, col, number):
            grid[row][col] = number
            # print_grid(grid)
            # sleep(0.5)
            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False


def print_grid(grid):
    for i in range(9):
        for j in range(9):
            if j == 3 or j == 6:
                print('|', end=' ')
            print(grid[i][j], end=' ')
        print()
        if i == 2 or i == 5:
            print("---------------------")
    print()


if __name__ == "__main__":
    grid = base_grid
    print_grid(grid)

    if solve(grid, 0, 0):
        print_grid(grid)
    else:
        print("no solution")
