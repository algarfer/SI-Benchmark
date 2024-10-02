#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from .BenchmarkTSP import BenchmarkTSP
from .tasks import tasks_tsp_gr17_astar, tasks_tsp_gr18_astar, tasks_tsp_gr21_astar
from .tasks import tasks_tsp_gr17_peastar, tasks_tsp_gr18_peastar, tasks_tsp_gr21_peastar

headers_astar = {
    "Heuristic:": "Heuristic",
    "Solution Cost:": "Solution Cost",
    "Nodes Expanded:": "Nodes Expanded",
    "Time Taken:": "Time Taken (s)",
    "Reexpanded States:": "Reexpanded States",
}
headers_pea = {
    "Heuristic:": "Heuristic",
    "Weight:": "Weight",
    "Solution Cost:": "Solution Cost",
    "Nodes Expanded:": "Nodes Expanded",
    "Time Taken:": "Time Taken (s)",
    "Reexpanded States:": "Reexpanded States",
}

timeout = 15 * 60 # 15 minutes

if __name__ == "__main__":
    # A* tasks
    BenchmarkTSP("times_gr17_astar", tasks_tsp_gr17_astar, headers_astar, timeout=timeout).run()
    BenchmarkTSP("times_gr18_astar", tasks_tsp_gr18_astar, headers_astar, timeout=timeout).run()
    BenchmarkTSP("times_gr21_astar", tasks_tsp_gr21_astar, headers_astar, timeout=timeout).run()

    # PEA* tasks
    BenchmarkTSP("times_gr17_peastar", tasks_tsp_gr17_peastar, headers_pea, timeout=timeout).run()
    BenchmarkTSP("times_gr18_peastar", tasks_tsp_gr18_peastar, headers_pea, timeout=timeout).run()
    BenchmarkTSP("times_gr21_peastar", tasks_tsp_gr21_peastar, headers_pea, timeout=timeout).run()

