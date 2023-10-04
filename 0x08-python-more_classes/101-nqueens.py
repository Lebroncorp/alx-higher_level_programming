#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N must be an integer greater than or equal to 4.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively,
where a queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chessboard = []
    [chessboard.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chessboard]
    return (chessboard)


def board_deepcopy(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(board_deepcopy, chessboard))
    return (chessboard)


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    answer = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                answer.append([r, c])
                break
    return (answer)


def xout(chessboard, row, column):
    """X out spots on a chessboard. All spots where
    non-attacking queens can no longer be played are X-ed out.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(column + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # X out all backwards spots
    for c in range(column - 1, -1, -1):
        chessboard[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][column] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][column] = "x"
    # X out all spots diagonally down to the right
    c = column + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = column - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = column + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = column - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
