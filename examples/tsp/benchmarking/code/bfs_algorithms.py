#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import time
from .problems_n_nodes import Node, expand, failure
from .queues import PriorityQueue


def best_first_search(problem, f):
    """Search nodes with minimum f(node) value first."""
    print("-----------------")
    NODES_EXPANDED = 0
    DUMMY_NODES = 0
    STATES_REEXPANDED = 0
    seconds = time.time()

    node = Node(problem.initial)
    frontier = PriorityQueue([node], key=f)
    reached = {problem.initial: node}
    expanded = {}

    while frontier:
        # node extraction, no  dummy nodes control
        node = frontier.pop()
        # Dummy nodes control
        while (node.path_cost > reached[node.state].path_cost):
            DUMMY_NODES += 1
            node = frontier.pop()
        # Reexpansion control, number of states reexpanded
        if node.state in expanded:
            STATES_REEXPANDED += 1
        else:
            expanded[node.state] = True

        # Counting expansions
        NODES_EXPANDED += 1
        # Monitoring expanded states and f-values
        print(node.state, "f()=", f(node))

        SOLUTION_COST = node.path_cost
        TIME_TAKEN = time.time() - seconds

        # if goal, show statistics
        if problem.is_goal(node.state):
            print("Time Taken: ", TIME_TAKEN)
            print("Nodes Expanded: ", NODES_EXPANDED)
            print("States Reached: ", len(reached))
            print("Nodes in Frontier: ", len(frontier))
            print("Solution Cost: ", SOLUTION_COST)
            print("Solution Length: ", len(node))
            print("Dummy Nodes: ", DUMMY_NODES)
            print("Reexpanded States: ", STATES_REEXPANDED)
            return node
        # node expansion
        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return failure


def best_first_tree_search(problem, f):
    """A version of best_first_search without the `reached` table."""
    frontier = PriorityQueue([Node(problem.initial)], key=f)
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            if not is_cycle(child):
                frontier.add(child)
    return failure


def g(n): return n.path_cost


def astar_search(problem, h=None):
    """Search nodes with minimum f(n) = g(n) + h(n)."""
    h = h or problem.h
    return best_first_search(problem, f=lambda n: g(n) + h(n))


def astar_tree_search(problem, h=None):
    """Search nodes with minimum f(n) = g(n) + h(n), with no `reached` table."""
    h = h or problem.h
    return best_first_tree_search(problem, f=lambda n: g(n) + h(n))


def weighted_astar_search(problem, h=None, weight=1.4):
    """Search nodes with minimum f(n) = g(n) + weight * h(n)."""
    h = h or problem.h
    return best_first_search(problem, f=lambda n: g(n) + weight * h(n))


def greedy_bfs(problem, h=None):
    """Search nodes with minimum h(n)."""
    h = h or problem.h
    return best_first_search(problem, f=h)


def uniform_cost_search(problem):
    """Search nodes with minimum path cost first."""
    return best_first_search(problem, f=g)


def breadth_first_bfs(problem):
    """Search shallowest nodes in the search tree first; using best-first."""
    return best_first_search(problem, f=len)


def depth_first_bfs(problem):
    """Search deepest nodes in the search tree first; using best-first."""
    return best_first_search(problem, f=lambda n: -len(n))


def is_cycle(node, k=30):
    """Does this node form a cycle of length k or less?"""

    def find_cycle(ancestor, k):
        return (ancestor is not None and k > 0 and
                (ancestor.state == node.state or find_cycle(ancestor.parent, k - 1)))

    return find_cycle(node.parent, k)
