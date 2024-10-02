#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ..code import weighted_astar_search, path_states, SymmetricTSP, Grafo

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
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_2():
    print("Heuristic: h_POBRE")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_3():
    print("Heuristic: h_POBRE")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_4():
    print("Heuristic: h_POBRE")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_5():
    print("Heuristic: h_POBRE")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_6():
    print("Heuristic: h_POBRE")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_7():
    print("Heuristic: h_POBRE")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_8():
    print("Heuristic: h_POBRE")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_9():
    print("Heuristic: h_POBRE")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_10():
    print("Heuristic: h_POBRE")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_11():
    print("Heuristic: h_POBRE")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_POBRE(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr17_12():
    print("Heuristic: h1")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_13():
    print("Heuristic: h1")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_14():
    print("Heuristic: h1")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_15():
    print("Heuristic: h1")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_16():
    print("Heuristic: h1")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_17():
    print("Heuristic: h1")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_18():
    print("Heuristic: h1")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_19():
    print("Heuristic: h1")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_20():
    print("Heuristic: h1")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_21():
    print("Heuristic: h1")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_22():
    print("Heuristic: h1")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h1(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr17_23():
    print("Heuristic: h2")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_24():
    print("Heuristic: h2")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_25():
    print("Heuristic: h2")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_26():
    print("Heuristic: h2")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_27():
    print("Heuristic: h2")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_28():
    print("Heuristic: h2")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_29():
    print("Heuristic: h2")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_30():
    print("Heuristic: h2")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_31():
    print("Heuristic: h2")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_32():
    print("Heuristic: h2")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_33():
    print("Heuristic: h2")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h2(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr17_34():
    print("Heuristic: h_MST")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_35():
    print("Heuristic: h_MST")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_36():
    print("Heuristic: h_MST")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_37():
    print("Heuristic: h_MST")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_38():
    print("Heuristic: h_MST")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_39():
    print("Heuristic: h_MST")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_40():
    print("Heuristic: h_MST")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_41():
    print("Heuristic: h_MST")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_42():
    print("Heuristic: h_MST")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_43():
    print("Heuristic: h_MST")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_44():
    print("Heuristic: h_MST")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_MST(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr17_56():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_57():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_58():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_59():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_60():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_61():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_62():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_63():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_64():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_65():
    print("Heuristic: h_HUNGARO")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_66():
    print("Heuristic: h_HUNGARO")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_HUNGARO(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr17_67():
    print("Heuristic: h_NN")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_68():
    print("Heuristic: h_NN")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_69():
    print("Heuristic: h_NN")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_70():
    print("Heuristic: h_NN")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_71():
    print("Heuristic: h_NN")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_72():
    print("Heuristic: h_NN")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_73():
    print("Heuristic: h_NN")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_74():
    print("Heuristic: h_NN")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_75():
    print("Heuristic: h_NN")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_76():
    print("Heuristic: h_NN")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_77():
    print("Heuristic: h_NN")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_NN(x)
    path_states(weighted_astar_search(instance, weight=2))

def task_gr17_78():
    print("Heuristic: h_BI")
    print("Weight: 1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1))

def task_gr17_79():
    print("Heuristic: h_BI")
    print("Weight: 1.1")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.1))

def task_gr17_80():
    print("Heuristic: h_BI")
    print("Weight: 1.2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.2))

def task_gr17_81():
    print("Heuristic: h_BI")
    print("Weight: 1.3")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.3))

def task_gr17_82():
    print("Heuristic: h_BI")
    print("Weight: 1.4")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.4))

def task_gr17_83():
    print("Heuristic: h_BI")
    print("Weight: 1.5")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.5))

def task_gr17_84():
    print("Heuristic: h_BI")
    print("Weight: 1.6")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.6))

def task_gr17_85():
    print("Heuristic: h_BI")
    print("Weight: 1.7")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.7))

def task_gr17_86():
    print("Heuristic: h_BI")
    print("Weight: 1.8")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.8))

def task_gr17_87():
    print("Heuristic: h_BI")
    print("Weight: 1.9")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=1.9))

def task_gr17_88():
    print("Heuristic: h_BI")
    print("Weight: 2")
    instance = SymmetricTSP(Grafo(gr17))
    instance.h = lambda x: instance.h_BI(x)
    path_states(weighted_astar_search(instance, weight=2))
