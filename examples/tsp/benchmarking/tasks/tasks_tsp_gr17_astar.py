#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..code import astar_search, path_states, SymmetricTSP, Grafo

gr17 = [
    0,
    633, 0,
    257, 390, 0,
    91, 661, 228, 0,
    412, 227, 169, 383, 0,
    150, 488, 112, 120, 267, 0,
    80, 572, 196, 77, 351, 63, 0,
    134, 530, 154, 105, 309, 34, 29, 0,
    259, 555, 372, 175, 338, 264, 232, 249, 0,
    505, 289, 262, 476, 196, 360, 444, 402, 495, 0,
    353, 282, 110, 324, 61, 208, 292, 250, 352, 154, 0,
    324, 638, 437, 240, 421, 329, 297, 314, 95, 578, 435, 0,
    70, 567, 191, 27, 346, 83, 47, 68, 189, 439, 287, 254, 0,
    211, 466, 74, 182, 243, 105, 150, 108, 326, 336, 184, 391, 145, 0,
    268, 420, 53, 239, 199, 123, 207, 165, 383, 240, 140, 448, 202, 57, 0,
    246, 745, 472, 237, 528, 364, 332, 349, 202, 685, 542, 157, 289, 426, 483, 0,
    121, 518, 142, 84, 297, 35, 29, 36, 236, 390, 238, 301, 55, 96, 153, 336, 0,
]

def task_gr17_1():
    print("Heuristic: h_POBRE")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(astar_search(instance))

def task_gr17_2():
    print("Heuristic: h1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(astar_search(instance))

def task_gr17_3():
    print("Heuristic: h2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(astar_search(instance))

def task_gr17_4():
    print("Heuristic: h_MST")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(astar_search(instance))

def task_gr17_5():
    print("Heuristic: h_HUNGARO")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(astar_search(instance))

def task_gr17_6():
    print("Heuristic: h_NN")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(astar_search(instance))

def task_gr17_7():
    print("Heuristic: h_BI")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(astar_search(instance))
