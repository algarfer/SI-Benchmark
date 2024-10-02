#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os, pathlib
import re
import multiprocessing, sys
import tempfile
from halo import Halo

class Benchmark:
    """
    Benchmark class to run tasks and measure their performance and other parameters
    :author: algarfer
    :version: 02/10/2024
    """
    COLLISION_NAME_TEMPLATE = "{0} ({1}).csv"
    TASK_REGEX = r'task_([0-9a-zA-Z]+)_\d+' # Task names should be in the format task_{task_indicator}_{task_number}

    def __init__(self, filename: str, module, columns: dict[str, str], outputdir: str="out", timeout: float=60) -> None:
        """
        Creates a Benchmark object
        :param filename: Name of the CSV file (without extension)
        :param module: Module containing the tasks to be run
        :param columns: Diccionary with the columns of the CSV file
        :param outputdir: Directory where the CSV file will be saved (default will be an out folder in the current directory)
        :param timeout: Maximum time (seconds) to run a task (default is 60 seconds) (-1 to disable)
        """
        self.outputdir = os.path.join(os.path.curdir, outputdir) if outputdir.startswith(".") else outputdir
        self.filename = os.path.join(self.outputdir, f"{filename}.csv")
        self.module = module
        self.timeout = timeout
        self.columns = columns

        # Creates the output directory if it does not exist
        if not os.path.exists(self.outputdir): pathlib.Path(self.outputdir).mkdir(parents=True, exist_ok=True)

        # Check if the file already exists and if so, create a new one with a different name "original_name (n).csv"
        index = 1
        while os.path.exists(self.filename) and os.path.isfile(self.filename):
            self.filename = os.path.join(self.outputdir, self.COLLISION_NAME_TEMPLATE.format(filename, index))
            index += 1

    @staticmethod
    def _log(*args, **kwargs) -> None:
        """
        Prints an info message
        :param args:
        :param kwargs:
        """
        print("[+] ", *args, **kwargs)

    @staticmethod
    def _write_data(filename: str, data: list[str], mode: str = 'a') -> None:
        """
        Writes a row to the CSV file
        :param filename: Name of the CSV file
        :param data: List of values to write
        :param mode: Mode to open the file (default is 'a')
        """
        with open(filename, mode, encoding="utf-8") as f:
            output = ""
            for value in data:
                output += f"{value},"
            if output.endswith(","):
                output = output[:-1]
            f.write(f"{output}\n")

    @staticmethod
    def _task_wrapper(function, tmp_file: str, task: str) -> None:
        """
        Wrapper to run a task and write the output to a temporary file
        :param function: Function to be executed
        :param tmp_file: Path to the temporary file
        :param task: Task name for logging purposes
        """
        f = open(tmp_file, "w+")
        old_std = sys.stdout
        sys.stdout = f # Changes the standard output to the temporary file

        try:
            function()
        except Exception as e:
            sys.stdout = old_std
            Benchmark._log(f"An error occurred while running task {task}:\n{e}")
        finally:
            sys.stdout.flush() # Restores the standard output
            sys.stdout = old_std
            f.close()

    def get_tasks(self, task_indicator: str=None) -> list[str]:
        """
        Returns a list of tasks names
        :param task_indicator: Task indicator to filter the tasks of the module, if not provided, all tasks will be returned
        :return: A list with the task names
        """
        if task_indicator:
            return [a for a in dir(self.module) if
                    (match := re.search(self.TASK_REGEX, a)) and match.group(1) == task_indicator]
        return [a for a in dir(self.module) if re.search(self.TASK_REGEX, a)]

    def run(self, task_indicator:str=None) -> None:
        """
        Runs the tasks that match the task_indicator and writes the results to a CSV file
        :param task_indicator: Indicates what tasks of the module should be runned
        """
        Benchmark._log(f"Creating report file at {self.filename}")
        Benchmark._write_data(self.filename, list(self.columns.values()), 'w')

        for t in self.get_tasks(task_indicator):
            with (tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False) as tmp_file,
                  Halo(text=f"Running task {t}", spinner={
                      "interval": 80,
                      "frames": [ "⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏" ]
                  }) as spinner):
                try:
                    # Creates a new process to run the task
                    p = multiprocessing.Process(target=Benchmark._task_wrapper,
                                                args=(self.module.__dict__[t], tmp_file.name, t))
                    p.start()
                    # The task will not exceed the time specified in the timeout parameter
                    p.join(None if self.timeout == -1 else self.timeout)

                    if p.is_alive(): # If the task is still running after the timeout, it will be terminated
                        spinner.fail(f"Time exceeded for task {t}")
                        p.terminate()
                        p.join()
                        for _ in self.columns.keys():
                            Benchmark._write_data(self.filename,
                                  [f"Time exceeded for task {t}" for _ in range(len(self.columns.keys()))], 'a')
                        continue

                    spinner.succeed(f"Task {t} completed")
                    Benchmark._log(f"Processing log file of task {t}")
                    self._process(tmp_file)
                    Benchmark._log(f"Log file processed correctly")
                finally:
                    tmp_file.close()
                    Benchmark._log(f"Cleaning up")
                    os.remove(tmp_file.name)
                    Benchmark._log(f'{"=" * 50}\n')

        Benchmark._log(f"Measuring ended")
        Benchmark._log(f"Final report can be found at {self.filename}")

    def _process(self, tmp_file) -> None:
        """
        "Abstract" method to process the temporary file and write the results to the CSV file
        Should be implemented based on the output structure of the tasks
        :param tmp_file: Temporary file with the log of the task
        """
        tmp_file.seek(0)
