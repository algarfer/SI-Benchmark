#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from .queues import PriorityQueue
from .problems_n_nodes import Node, expand, failure, path_states
from .bfs_algorithms import g
from .reporting import CountCalls
import copy

def bidirectional_best_first_search(problem_f, f_f, problem_b, f_b, terminated):
    node_f = Node(problem_f.initial)
    node_b = Node(problem_f.goal)
    frontier_f, reached_f = PriorityQueue([node_f], key=f_f), {node_f.state: node_f}
    frontier_b, reached_b = PriorityQueue([node_b], key=f_b), {node_b.state: node_b}
    solution = failure
    while frontier_f and frontier_b and not terminated(solution, frontier_f, frontier_b):
        def S1(node, f):
            return str(int(f(node))) + ' ' + str(path_states(node))
        print('Bi:', S1(frontier_f.top(), f_f), S1(frontier_b.top(), f_b))
        if f_f(frontier_f.top()) < f_b(frontier_b.top()):
            solution = proceed('f', problem_f, frontier_f, reached_f, reached_b, solution)
        else:
            solution = proceed('b', problem_b, frontier_b, reached_b, reached_f, solution)
    return solution

def inverse_problem(problem):
    if isinstance(problem, CountCalls):
        return CountCalls(inverse_problem(problem._object))
    else:
        inv = copy.copy(problem)
        inv.initial, inv.goal = inv.goal, inv.initial
        return inv

def bidirectional_uniform_cost_search(problem_f):
    def terminated(solution, frontier_f, frontier_b):
        n_f, n_b = frontier_f.top(), frontier_b.top()
        return g(n_f) + g(n_b) > g(solution)

    return bidirectional_best_first_search(problem_f, g, inverse_problem(problem_f), g, terminated)


def bidirectional_astar_search(problem_f):
    def terminated(solution, frontier_f, frontier_b):
        nf, nb = frontier_f.top(), frontier_b.top()
        return g(nf) + g(nb) > g(solution)

    problem_f = inverse_problem(problem_f)
    return bidirectional_best_first_search(problem_f, lambda n: g(n) + problem_f.h(n),
                                           problem_b, lambda n: g(n) + problem_b.h(n),
                                           terminated)


def proceed(direction, problem, frontier, reached, reached2, solution):
    node = frontier.pop()
    for child in expand(problem, node):
        s = child.state
        print('proceed', direction, S(child))
        if s not in reached or child.path_cost < reached[s].path_cost:
            frontier.add(child)
            reached[s] = child
            if s in reached2:  # Frontiers collide; solution found
                solution2 = (join_nodes(child, reached2[s]) if direction == 'f' else
                             join_nodes(reached2[s], child))
                # print('solution', path_states(solution2), solution2.path_cost,
                # path_states(child), path_states(reached2[s]))
                if solution2.path_cost < solution.path_cost:
                    solution = solution2
    return solution


S = path_states


# A-S-R + B-P-R => A-S-R-P + B-P
def join_nodes(nf, nb):
    """Join the reverse of the backward node nb to the forward node nf."""
    # print('join', S(nf), S(nb))
    join = nf
    while nb.parent is not None:
        cost = join.path_cost + nb.path_cost - nb.parent.path_cost
        join = Node(nb.parent.state, join, nb.action, cost)
        nb = nb.parent
        # print('  now join', S(join), 'with nb', S(nb), 'parent', S(nb.parent))
    return join

