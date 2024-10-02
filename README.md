<div align="center">
    <h1>SI-Benchmark</h1>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
</div>

<p align="justify">
    <b>SI-Benchmark</b> is a Python project designed to automate the generation of CSV files with the execution results of
    various intelligent algorithms.
</p>

## Table of Contents

1. [Installation](#installation)
2. [Base code](#base-code)
3. [Creating tasks](#creating-tasks)
4. [Custom classes](#custom-classes)
5. [Specifying the saved data](#specifying-the-saved-data)
6. [Running the project](#running-the-project)

### Installation

<p align="justify">
    To install the project, you need to have Python installed on your system. Follow these steps to set up the environment:
</p>

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

<div align="justify">
    <p>Place the algorithm code inside the benchmarking/code folder.</p>
    <p>
        For students of the <i>Sistemas Inteligentes</i> course at the <i>Universidad de Oviedo</i>, the Python code provided in the course's
        Jupyter Notebooks (based on the <a href="https://github.com/aimacode/aima-python">AIMA</a> code) should be placed here. You can organize
        this code into a single Python file or multiple files. To steamline usage, export functions and variables via the <tt>__init__.py</tt> file.
    </p>
</div>

### Creating tasks

<div align="justify">
    <p>Each algorithm should be encapsulated in a task.</p>
    <p>A task can include more than just the algorithm code. The output of the task will be captured by the script and stored in a temporary file for further processing.</p>
    <p>Each task must be a Python function with the followingn naming structure:</p>
</div>

```python
def task_filter_n():
    # Code
    pass
```

<p align="justify">
    Where <tt>filter</tt> is an alphanumeric string used to filter tasks and <tt>n</tt> is a unique identifier for the task.
    This filter is helpful whe using the <tt>run</tt> method of the <tt>Benchmark</tt> class to specify which tasks to execute.
</p>

> [!TIP]
> If you need to save additional data beyond the algorithm's output, you can include extra `print` statements inside the task,
> as the script captures all printed output.

### Custom classes

<div align="justify">
    <p>
        To process the output of tasks and save it in a CSV file, you'll need to create a custom class that inherits from the <tt>Benchmark</tt> class.
    </p>
    <p>
        In your custom class, implement the <tt>_process</tt> method to handle the task output and specify how to save it into the CSV.
    </p>
</div>

### Specifying the saved data

<div align="justify">
    <p>You need to provide a dictionary of strings to the <tt>Benchmark</tt> class, where:</p>
    <ul>
        <li><tt>Keys</tt>: Used in the <tt>_process</tt> method to access the task's output.</li>
        <li><tt>Values</tt>: Used as headers for the CSV file.</li>
    </ul>
    <p>These keys can also be employed to filter data in the temporary output file using string matching or regex.</p>
</div>

### Running the project

<div align="justify">
    <p>
        Once you've created the tasks and custom class, process the tasks by creating an instance of the custom class and calling
        the <tt>run</tt> method in a file such as <tt>main.py</tt>, located in the <tt>benchmarking</tt> folder.
    </p>
    <p>To run the project, navigate to the parent directory and execute the script with the following command:</p>
</div>

```bash
python -m benchmarking.main
```

<p align="justify">
    Make sure to import the necessary task modules in your <tt>main.py</tt> file:
</p>

```python
from .tasks import tasks

benchmark = Benchmark(..., tasks, ...)
```
---

> [!NOTE]
> All import statements should use relative paths.

> [!TIP]
> For further clarity, refer to the examples provided in the [examples](examples) folder