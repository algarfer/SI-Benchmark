#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from .Benchmark import Benchmark

class BenchmarkTSP(Benchmark):
    """
    Implementation of the Benchmark class for the TSP domain.
    :author: algarfer
    :version: 02/10/2024
    """

    def _process(self, tmp_file) -> None:
        """
        Processes the log file of a task.
        :param tmp_file: the temporary file containing the log of the task.
        """
        super()._process(tmp_file)
        lines = tmp_file.readlines()

        data = {}

        # Initializes all the keys in order to detect missing values
        for k in self.columns.keys():
            data[k] = None

        for line in lines:
            for k in self.columns.keys():
                if line.startswith(k):
                    data[k] = line.split(": ")[1].strip()

        # Missing values will be replaced by N/A
        BenchmarkTSP._write_data(self.filename, [a if a is not None else "N/A" for a in list(data.values())], 'a')