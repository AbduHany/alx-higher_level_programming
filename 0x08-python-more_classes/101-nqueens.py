#!/usr/bin/python3
"""This module solves the N queens problem
"""


import sys

if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    exit(1)
N = int(sys.argv[1])
if (type(N) is not int):
    print("N must be a number")
    exit(1)
if (N < 4):
    print("N must be at least 4")
    exit(1)

# create board (list of lists to hold queens)
board = [[0 for i in range(N)] for i in range(N)]
# results array
res = []

col = set()
rightdiag = set()
leftdiag = set()


def backtrack(row):
    if row == N:
        sol = []
        for i in range(len(board)):
            pos = []
            for column in range(len(board[i])):
                if board[i][column] == 1:
                    pos += [[i, column]]
            sol += pos
        res.append(sol)
        return

    for c in range(N):
        if c in col or (row + c) in rightdiag or (row - c) in leftdiag:
            continue

        col.add(c)
        rightdiag.add(row + c)
        leftdiag.add(row - c)
        board[row][c] = 1

        backtrack(row + 1)

        col.remove(c)
        rightdiag.remove(row + c)
        leftdiag.remove(row - c)
        board[row][c] = 0


backtrack(0)
for sol in res:
    print(sol)
