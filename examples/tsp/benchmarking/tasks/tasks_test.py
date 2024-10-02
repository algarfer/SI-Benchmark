#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..code import astar_search, path_states, SymmetricTSP, Grafo

ejemploClase = [
    0,
    21, 0,
    12, 7, 0,
    15, 32, 5, 0,
    113, 25, 18, 180, 0,
    92, 9, 20, 39, 17, 0
]

def task_ejemploClase_1():
    print(f"Heuristic: h_POBRE")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(astar_search(instance))

def task_ejemploClase_2():
    print(f"Heuristic: h1")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h1(x)
    path_states(astar_search(instance))

def task_ejemploClase_3():
    print(f"Heuristic: h2")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h2(x)
    path_states(astar_search(instance))

def task_ejemploClase_4():
    print(f"Heuristic: h_MST")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h_MST(x)
    path_states(astar_search(instance))

def task_ejemploClase_5():
    print(f"Heuristic: h_HUNGARO")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(astar_search(instance))

def task_ejemploClase_6():
    print(f"Heuristic: h_NN")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h_NN(x)
    path_states(astar_search(instance))

def task_ejemploClase_7():
    print(f"Heuristic: h_BI")
    instance = SymmetricTSP(Grafo(ejemploClase))
    instance.h = lambda x: instance.h_BI(x)
    path_states(astar_search(instance))
