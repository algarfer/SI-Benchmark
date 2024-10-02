#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from .problems_n_nodes import Problem
from itertools import combinations

class EightPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank, trying to reach a goal configuration.
    A board state is represented as a tuple of length 9, where the element at index i
    represents the tile number at index i, or 0 if for the empty square, e.g. the goal:
        1 2 3
        4 5 6 ==> (1, 2, 3, 4, 5, 6, 7, 8, 0)
        7 8 _
    """

    # def __init__(self, initial, goal=(1, 2, 3, 8, 0, 4, 7, 6, 5)):
    def __init__(self, initial, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
        # assert inversions(initial) % 2 == inversions(goal) % 2 # Parity check
        self.initial, self.goal = initial, goal

    def actions(self, state):
        """The indexes of the squares that the blank can be moved to."""
        moves = ((1, 3), (0, 2, 4), (1, 5),
                 (0, 4, 6), (1, 3, 5, 7), (2, 4, 8),
                 (3, 7), (4, 6, 8), (7, 5))
        blank = state.index(0)
        return moves[blank]

    def result(self, state, action):
        """Swap the blank with the square numbered `action`."""
        s = list(state)
        blank = state.index(0)
        s[action], s[blank] = s[blank], s[action]
        return tuple(s)

    # action cost other than default 1
    # def action_cost(self, s, a, s1): return math.exp(s[a]);
    # def action_cost(self, s, a, s1): return s[a]

    # heuristic functions
    def h0(self, node):
        """The null heuristic."""
        return 0

    def h1(self, node):
        """The misplaced tiles heuristic. It has a bug as it counts 0 as a valid tide!!"""
        return hamming_distance(node.state, self.goal)

    def h2_0(self, node):
        """The Manhattan heuristic for goal (0, 1, 2, 3, 4, 5, 6, 7, 8)"""
        X = (0, 1, 2, 0, 1, 2, 0, 1, 2)
        Y = (0, 0, 0, 1, 1, 1, 2, 2, 2)
        return sum(abs(X[s] - X[g]) + abs(Y[s] - Y[g])
                   for (s, g) in zip(node.state, self.goal) if s != 0)
        # g = 0, 1, ..., 8 (tuple positions, or tildes in goal.state)
        # s = gth tilde in the node.state
        # X[g],Y[g] = board position of tilde s in node.state
        # X[s],Y[s] = board position of tilde s in goal.state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    def h2(self, node):
        # sirve para cualquier estado objetivo
        suma = 0
        # para cada ficha 1, 2, ..., 8 calcular las distancia de su posicion en node.state a su posicion en self.goal

        for j in range(1, 9):
            posInicial = node.state.index(j)
            xInicial = posInicial % 3
            yInicial = posInicial // 3

            posFinal = self.goal.index(j)
            xFinal = posFinal % 3
            yFinal = posFinal // 3

            suma += abs(xInicial - xFinal) + abs(yInicial - yFinal)

        return suma

    def h3(self, node):
        # suma 2 por cada ficha a distancia 2 de su posicion en el objetivo
        # sirve para cualquier estado objetivo
        suma = 0
        # para cada ficha 1, 2, ..., 8 calcular las distancia de su posicion en node.state a su posicion en self.goal

        for j in range(1, 9):
            posInicial = node.state.index(j)
            xInicial = posInicial % 3
            yInicial = posInicial // 3

            posFinal = self.goal.index(j)
            xFinal = posFinal % 3
            yFinal = posFinal // 3

            if abs(xInicial - xFinal) + abs(yInicial - yFinal) == 2:
                suma += 2

        return suma

    # Actual heuristic
    def h(self, node):
        return self.h3(node)


def hamming_distance(A, B):
    "Number of positions where vectors A and B are different."
    return sum(a != b and a != 0 for a, b in zip(A, B))


def inversions(board):
    "The number of times a piece is a smaller number than a following piece."
    return sum((a > b and a != 0 and b != 0) for (a, b) in combinations(board, 2))


def board8(board, fmt=(3 * '{} {} {}\n')):
    "A string representing an 8-puzzle board"
    return fmt.format(*board).replace('0', '_')

