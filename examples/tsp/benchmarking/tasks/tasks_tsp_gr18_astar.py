#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..code import astar_search, path_states,SymmetricTSP, Grafo

gr18 = [
    0,
    510, 0,
    635, 355, 0,
    91, 415, 605, 0,
    385, 585, 390, 350, 0,
    155, 475, 495, 120, 240, 0,
    110, 480, 570, 78, 320, 96, 0,
    130, 500, 540, 97, 285, 36, 29, 0,
    490, 605, 295, 460, 120, 350, 425, 390, 0,
    370, 320, 700, 280, 590, 365, 350, 370, 625, 0,
    155, 380, 640, 63, 430, 200, 160, 175, 535, 240, 0,
    68, 440, 575, 27, 320, 91, 48, 67, 430, 300, 90, 0,
    610, 360, 705, 520, 835, 605, 590, 610, 865, 250, 480, 545, 0,
    655, 235, 585, 555, 750, 615, 625, 645, 775, 285, 515, 585, 190, 0,
    480, 81, 435, 380, 575, 440, 455, 465, 600, 245, 345, 415, 295, 170, 0,
    265, 480, 420, 235, 125, 125, 200, 165, 230, 475, 310, 205, 715, 650, 475, 0,
    255, 440, 755, 235, 650, 370, 320, 350, 680, 150, 175, 265, 400, 435, 385, 485, 0,
    450, 270, 625, 345, 660, 430, 420, 440, 690, 77, 310, 380, 180, 215, 190, 545, 225, 0,
]

def task_gr18_1():
    print("Heuristic: h_POBRE")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(astar_search(instance))

def task_gr18_2():
    print("Heuristic: h1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(astar_search(instance))

def task_gr18_3():
    print("Heuristic: h2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(astar_search(instance))

def task_gr18_4():
    print("Heuristic: h_MST")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(astar_search(instance))

def task_gr18_5():
    print("Heuristic: h_HUNGARO")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(astar_search(instance))

def task_gr18_6():
    print("Heuristic: h_NN")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(astar_search(instance))

def task_gr18_7():
    print("Heuristic: h_BI")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(astar_search(instance))
