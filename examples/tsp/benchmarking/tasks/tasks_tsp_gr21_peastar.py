#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..code import weighted_astar_search, path_states, SymmetricTSP, Grafo

gr21 = [
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
    170, 445, 750, 160, 495, 265, 220, 240, 600, 235, 125, 170, 485, 525, 405, 375, 87, 315, 0,
    240, 290, 590, 140, 480, 255, 205, 220, 515, 150, 100, 170, 390, 425, 255, 395, 205, 220, 155, 0,
    380, 140, 495, 280, 480, 340, 350, 370, 505, 185, 240, 310, 345, 280, 105, 380, 280, 165, 305, 150, 0,
]

def task_gr21_1():
    print("Heuristic: h_POBRE")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_2():
    print("Heuristic: h_POBRE")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_3():
    print("Heuristic: h_POBRE")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_4():
    print("Heuristic: h_POBRE")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_5():
    print("Heuristic: h_POBRE")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_6():
    print("Heuristic: h_POBRE")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_7():
    print("Heuristic: h_POBRE")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_8():
    print("Heuristic: h_POBRE")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_9():
    print("Heuristic: h_POBRE")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_10():
    print("Heuristic: h_POBRE")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_11():
    print("Heuristic: h_POBRE")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr21_12():
    print("Heuristic: h1")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_13():
    print("Heuristic: h1")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_14():
    print("Heuristic: h1")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_15():
    print("Heuristic: h1")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_16():
    print("Heuristic: h1")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_17():
    print("Heuristic: h1")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_18():
    print("Heuristic: h1")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_19():
    print("Heuristic: h1")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_20():
    print("Heuristic: h1")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_21():
    print("Heuristic: h1")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_22():
    print("Heuristic: h1")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr21_23():
    print("Heuristic: h2")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_24():
    print("Heuristic: h2")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_25():
    print("Heuristic: h2")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_26():
    print("Heuristic: h2")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_27():
    print("Heuristic: h2")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_28():
    print("Heuristic: h2")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_29():
    print("Heuristic: h2")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_30():
    print("Heuristic: h2")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_31():
    print("Heuristic: h2")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_32():
    print("Heuristic: h2")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_33():
    print("Heuristic: h2")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr21_34():
    print("Heuristic: h_MST")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_35():
    print("Heuristic: h_MST")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_36():
    print("Heuristic: h_MST")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_37():
    print("Heuristic: h_MST")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_38():
    print("Heuristic: h_MST")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_39():
    print("Heuristic: h_MST")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_40():
    print("Heuristic: h_MST")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_41():
    print("Heuristic: h_MST")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_42():
    print("Heuristic: h_MST")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_43():
    print("Heuristic: h_MST")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_44():
    print("Heuristic: h_MST")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr21_45():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_46():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_47():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_48():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_49():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_50():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_51():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_52():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_53():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_54():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_55():
    print("Heuristic: h_HUNGARO")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr21_56():
    print("Heuristic: h_NN")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_57():
    print("Heuristic: h_NN")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_58():
    print("Heuristic: h_NN")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_59():
    print("Heuristic: h_NN")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_60():
    print("Heuristic: h_NN")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_61():
    print("Heuristic: h_NN")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_62():
    print("Heuristic: h_NN")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_63():
    print("Heuristic: h_NN")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_64():
    print("Heuristic: h_NN")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_65():
    print("Heuristic: h_NN")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_66():
    print("Heuristic: h_NN")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr21_67():
    print("Heuristic: h_BI")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr21_68():
    print("Heuristic: h_BI")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr21_69():
    print("Heuristic: h_BI")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr21_70():
    print("Heuristic: h_BI")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr21_71():
    print("Heuristic: h_BI")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr21_72():
    print("Heuristic: h_BI")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr21_73():
    print("Heuristic: h_BI")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr21_74():
    print("Heuristic: h_BI")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr21_75():
    print("Heuristic: h_BI")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr21_76():
    print("Heuristic: h_BI")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr21_77():
    print("Heuristic: h_BI")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr21))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=2))
