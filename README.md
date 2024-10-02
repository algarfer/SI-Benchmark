<style>body {text-align: justify}</style>

<div align="center">
    <h1>SI-Benchmark</h1>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
</div>

**SI-Benchmark** is a Python project designed to automate the generation of CSV files with the execution results of
various intelligent algorithms.

## Table of Contents

1. [Installation](#installation)
2. [Base code](#base-code)
3. [Creating tasks](#creating-tasks)
4. [Custom classes](#custom-classes)
5. [Specifying the saved data](#specifying-the-saved-data)
6. [Running the project](#running-the-project)

### Installation
To install the project, you need to have Python installed on your system. Follow these steps to set up the environment:

```bash
python -m venv .venv
source .venv/bin/activate # For Linux/MacOS
.venv\Scripts\activate # For Windows
pip install -r requirements.txt
```

> [!IMPORTANT]  
> The `requirements.txt` file contains only the benchmark dependencies.
> If you wish to run specific algorithms, ensure to install the required dependencies for those algorithms separately.

### Base code
Place the algorithm code inside the benchmarking/code folder.

For students of the _Sistemas Inteligentes_ course at the _Universidad de Oviedo_, the Python code provided in the course's
Jupyter Notebooks (based on the [AIMA](https://github.com/aimacode/aima-python) code) should be placed here. You can organize
this code into a single Python file or multiple files. To steamline usage, export functions and variables via the `__init__.py` file.

### Creating tasks
Each algorithm should be encapsulated in a task.

A task can include more than just the algorithm code. The output of the task will be captured by the script and stored in a temporary file for further processing.

Each task must be a Python function with the followingn naming structure:
```python
def task_filter_n():
    # Code
    pass
```

Where `filter` is an alphanumeric string used to filter tasks and `n` is a unique identifier for the task.
This filter is helpful whe using the `run` method of the `Benchmark` class to specify which tasks to execute.

> [!TIP]
> If you need to save additional data beyond the algorithm's output, you can include extra `print` statements inside the task,
> as the script captures all printed output.

### Custom classes

To process the output of tasks and save it in a CSV file, you'll need to create a custom class that inherits from the `Benchmark` class.

In your custom class, implement the `_process` method to handle the task output and specify how to save it into the CSV.

### Specifying the saved data
You need to provide a dictionary of strings to the `Benchmark` class, where:
- `Keys`: Used in the `_process` method to access the task's output.
- `Values`: Used as headers for the CSV file.

These keys can also be employed to filter data in the temporary output file using string matching or regex.

### Running the project
Once you've created the tasks and custom class, process the tasks by creating an instance of the custom class and calling
the `run` method in a file such as `main.py`, located in the `benchmarking` folder.

To run the project, navigate to the parent directory and execute the script with the following command:
```bash
python -m benchmarking.main
```

Make sure to import the necessary task modules in your `main.py` file:
```python
from .tasks import tasks

benchmark = Benchmark(..., tasks, ...)
```

---

> [!NOTE]
> All import statements should use relative paths.

> [!TIP]
> For further clarity, refer to the examples provided in the [examples](examples) folder