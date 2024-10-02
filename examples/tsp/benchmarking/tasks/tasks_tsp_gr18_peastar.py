#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..code import weighted_astar_search, path_states, SymmetricTSP, Grafo

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
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_2():
    print("Heuristic: h_POBRE")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_3():
    print("Heuristic: h_POBRE")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_4():
    print("Heuristic: h_POBRE")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_5():
    print("Heuristic: h_POBRE")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_6():
    print("Heuristic: h_POBRE")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_7():
    print("Heuristic: h_POBRE")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_8():
    print("Heuristic: h_POBRE")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_9():
    print("Heuristic: h_POBRE")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_10():
    print("Heuristic: h_POBRE")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_11():
    print("Heuristic: h_POBRE")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr18_12():
    print("Heuristic: h1")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_13():
    print("Heuristic: h1")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_14():
    print("Heuristic: h1")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_15():
    print("Heuristic: h1")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_16():
    print("Heuristic: h1")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_17():
    print("Heuristic: h1")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_18():
    print("Heuristic: h1")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_19():
    print("Heuristic: h1")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_20():
    print("Heuristic: h1")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_21():
    print("Heuristic: h1")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_22():
    print("Heuristic: h1")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr18_23():
    print("Heuristic: h2")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_24():
    print("Heuristic: h2")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_25():
    print("Heuristic: h2")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_26():
    print("Heuristic: h2")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_27():
    print("Heuristic: h2")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_28():
    print("Heuristic: h2")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_29():
    print("Heuristic: h2")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_30():
    print("Heuristic: h2")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_31():
    print("Heuristic: h2")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_32():
    print("Heuristic: h2")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_33():
    print("Heuristic: h2")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr18_34():
    print("Heuristic: h_MST")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_35():
    print("Heuristic: h_MST")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_36():
    print("Heuristic: h_MST")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_37():
    print("Heuristic: h_MST")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_38():
    print("Heuristic: h_MST")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_39():
    print("Heuristic: h_MST")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_40():
    print("Heuristic: h_MST")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_41():
    print("Heuristic: h_MST")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_42():
    print("Heuristic: h_MST")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_43():
    print("Heuristic: h_MST")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_44():
    print("Heuristic: h_MST")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr18_45():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_46():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_47():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_48():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_49():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_50():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_51():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_52():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_53():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_54():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_55():
    print("Heuristic: h_HUNGARO")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr18_56():
    print("Heuristic: h_NN")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_57():
    print("Heuristic: h_NN")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_58():
    print("Heuristic: h_NN")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_59():
    print("Heuristic: h_NN")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_60():
    print("Heuristic: h_NN")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_61():
    print("Heuristic: h_NN")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_62():
    print("Heuristic: h_NN")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_63():
    print("Heuristic: h_NN")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_64():
    print("Heuristic: h_NN")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_65():
    print("Heuristic: h_NN")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_66():
    print("Heuristic: h_NN")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr18_67():
    print("Heuristic: h_BI")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr18_68():
    print("Heuristic: h_BI")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr18_69():
    print("Heuristic: h_BI")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr18_70():
    print("Heuristic: h_BI")
    print("Weight: 1..3")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr18_71():
    print("Heuristic: h_BI")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr18_72():
    print("Heuristic: h_BI")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr18_73():
    print("Heuristic: h_BI")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr18_74():
    print("Heuristic: h_BI")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr18_75():
    print("Heuristic: h_BI")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr18_76():
    print("Heuristic: h_BI")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr18_77():
    print("Heuristic: h_BI")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr18))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=2))
