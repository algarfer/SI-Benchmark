#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from bisect import insort
from .problems_n_nodes import Problem
from .hungarian_algorithm import hungarian_algorithm
import numpy as np

class EstadoTSP:
    def __init__(self, actual, visitadas):
        self.actual = actual
        self.visitadas = visitadas
        lista = visitadas.copy()
        lista.append(actual)
        self.state = tuple(lista)
        self.str = " [Visitadas: " + str(self.visitadas) + " Actual: " + str(self.actual) +"]"
    def __hash__(self):
        return hash(self.state)
    def __eq__(self,other):
        return (self.actual == other.actual) and (self.visitadas == other.visitadas)
    def __repr__(self):
        return f'{self.str}'

class Arco:
    def __init__(self,x,y,coste):
        self.x = x
        self.y = y
        self.coste = coste
        self.str = "[("+ str(self.x) + "," + str(self.y) +") " + str(self.coste) + "]"
    def __lt__(self,other):
        return self.coste < other.coste
    def __repr__(self):
        return f'{self.str}'
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y or self.x == other.y and self.y == other.x


class Grafo:
    """Un Grafo es un array bidimensional de tamño N*N, siendo N el número de ciudades,
    representadas por los valores 0,...,N-1; 0 se toma como ciudad de partida.
    El valor de la posición (i,j) es la distancia entre las ciudades i y j,
     que es el mismo que la distancia entre j e i """

    def __init__(self, lista):
        "N es el número de ciudades correspondiente a la lista de valores de una instancia en la sintaxis EDGE_WEIGHT_TYPE"
        self.N = int(((8 * len(lista) + 1) ** 0.5) - 1) / 2
        self.Total = 0
        # print(self.N)
        self.ciudades = list(range(int(self.N)))
        self.Dist = [[0] * int(self.N) for i in self.ciudades]
        x_acc = 0
        for x in range(int(self.N)):
            x_acc += x
            for y in range(x + 1):
                self.Dist[x][y] = self.Dist[y][x] = lista[x_acc + y]
                self.Total += 2 * lista[x_acc + y]

    def listaArcosOrdenados(self):
        lista = []
        for x in range(int(self.N)):
            for y in range(x):
                insort(lista, Arco(x, y, self.Dist[x][y]))
        # print(lista)
        return lista

    def listaCiudadesGrafoResidual(self, state):
        lista = [0]
        for x in range(int(self.N)):
            if (x not in state.visitadas and x != 0):
                lista.append(x)
        return lista

    def listaArcosGrafoResidual(self, state):
        listaCGR = self.listaCiudadesGrafoResidual(state)
        if (len(listaCGR) < 2):
            return []
        if (len(listaCGR) == 2):
            return [Arco(state.actual, 0, self.Dist[state.actual][0])]
        lista = []
        for x in listaCGR:
            for y in listaCGR:
                if (x < y and not (x == 0 and y == state.actual)):
                    insort(lista, Arco(x, y, self.Dist[x][y]))
        return lista

    def listaCiudadesAbandonar(self, state):
        lista = []
        for x in range(int(self.N)):
            if (x not in state.visitadas and x != 0):
                lista.append(x)
        return lista

    def listaCiudadesAlcanzar(self, state):
        lista = [0]
        for x in range(int(self.N)):
            if (x not in state.visitadas and x != state.actual):
                lista.append(x)
        return lista

    def matrizAsignacion(self, state):
        size = int(self.N - len(state.visitadas))  # dimension de la matriz de asignacion
        Asig = [[0] * size for i in range(size)]
        alcanzar = self.listaCiudadesAlcanzar(state)
        abandonar = self.listaCiudadesAbandonar(state)
        i = 0
        for x in range(int(self.N)):
            j = 0
            if (x in alcanzar):
                for y in range(int(self.N)):
                    if (y in abandonar):
                        if (x == y or (x == 0 and y == state.actual and size > 1)):
                            Asig[i][j] = self.Total  # infinito
                        else:
                            Asig[i][j] = self.Dist[x][y]
                        j += 1
                i += 1
        return Asig


class SymmetricTSP(Problem):
    """El problema consiste en encontrar un camino hamiltoniano en un grafo no dirigido
    y totalmente conectado, con costes positivos en los ejes. Las ciudades son 0,...,N-1
    La ciudad de partida es la 0"""

    def __init__(self, grafo):
        self.grafo = grafo
        self.initial = EstadoTSP(0, [])
        # print(self.__dir__initial)
        self.lArcos = grafo.listaArcosOrdenados()
        # print(self.lArcos)

    def actions(self, state):
        """Una accion por cada ciudad no visitada distinta de la actual, si todas visitadas -1"""
        noVisitadas = []
        for c in self.grafo.ciudades:
            if c not in state.visitadas and c != state.actual:
                noVisitadas.append(c)
        if len(noVisitadas) == 0:
            noVisitadas = [0]
        return noVisitadas

    def result(self, state, action):
        setVisitadas = list(state.visitadas)
        insort(setVisitadas, state.actual)
        return EstadoTSP(action, setVisitadas)

    def is_goal(self, state):
        return state.actual == 0 and len(state.visitadas) == self.grafo.N

    def action_cost(self, s, a, s1):
        return self.grafo.Dist[s.actual][a]

    # HEURISTICOS, LO MAS IMPORTANTE!!

    def h_POBRE(self, node):
        # heuristico muy poco informado, cuenta el numero de ciudades que faltan por visitar, es el valor N-k+1
        return self.grafo.N - len(node.state.visitadas)

    def h1(self, node):
        # Heuristico que considera los arcos minimos de las ciudades
        # que quedan por abandonar.
        # No responde a ninguna relajacion, aparentemente
        # Se puede mejorar si consideramos que las ciudades nunca se abandornaran hacia una ciudad ya visitada, excepto la inicial 0
        lista = self.grafo.listaCiudadesAbandonar(node.state)
        h = 0
        for x in lista:
            min = self.lArcos[-1].coste
            for y in range(int(self.grafo.N)):
                if (x != y and self.grafo.Dist[x][y] < min):
                    min = self.grafo.Dist[x][y]
            h += min
        return h

    def h2(self, node):
        # Relajacion R2, R3, R4.
        # Suma de los N-k+1 arcos de menos coste del grafo residual
        listaAGR = self.grafo.listaArcosGrafoResidual(node.state)
        Nk1 = self.grafo.N - len(node.state.visitadas)
        h = 0
        for i in range(int(Nk1)):
            a = listaAGR.pop(0)
            h += a.coste
        return h

    def h_MST(self, node):
        # Relajacion R3
        # Coste de un arbol de expansion minimo del grafo residual
        # Se calcula con el algoritmo de Kruskal
        if (node.state == self.initial or self.is_goal(node.state)):
            return 0
        listaAGR = self.grafo.listaArcosGrafoResidual(node.state)
        listaCGR = self.grafo.listaCiudadesGrafoResidual(node.state)
        c = {}
        for x in listaCGR:
            c[x] = x
        nA = self.grafo.N - len(node.state.visitadas)
        h = 0
        while (nA > 0):
            a = listaAGR.pop(0)
            cx = self.particion(c, a.x)
            cy = self.particion(c, a.y)
            # print(cx,cy)
            if (cx != cy):
                h += a.coste
                c[cx] = cy
                nA -= 1
        return h

    def particion(self, c, x):
        if (c[x] == x):
            return x
        else:
            return self.particion(c, c[x])

    def h_HUNGARO(self, node):
        # Relajacion R3
        # Coste de la asignacion minima entre los conjuntos
        # CIUDADES_NO_VISITADAS U {ACTUAL} y CIUDADES_NO_VISITADAS U {INICIAL}
        # Es una aproximacion al coste optimo del problema relajado (R3)
        # ya que pueden aparecer arcos repetidos en la solucion

        if (node.state == self.initial or self.is_goal(node.state)):
            return 0
        # print(node.state)
        cost_matrix = np.asarray(self.grafo.matrizAsignacion(node.state))
        asignacion = hungarian_algorithm(np.asarray(cost_matrix))
        coste = 0
        for asig in asignacion:
            coste += cost_matrix[asig[0], asig[1]]
        return coste

    def h_NN(self, node):
        # Calcula la mejor solucion del problema que representa el estado node.state con la estrategia "Nearest Neighbor"
        return 0

    def h_BI(self, node):
        # Calcula la mejor solucion del problema que representa el estado node.state con la estrategia "Best Insertion"
        return 0

    # Actual heuristic
    def h(self, node):
        return self.h_NN(node)
