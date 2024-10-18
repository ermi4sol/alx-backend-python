# Asynchronous Python Project

This project focuses on implementing and understanding asynchronous programming in Python using the `asyncio` module. It covers various aspects of async programming, including coroutines, tasks, and concurrent execution.

## Learning Objectives

By the end of this project, you should be able to explain:

- The syntax and usage of `async` and `await`
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module in the context of async programming

## Requirements

### General

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a newline character
- The first line of all files should be `#!/usr/bin/env python3`
- A `README.md` file at the root of the project directory is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- All modules, functions, and coroutines must be type-annotated
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

## Files and Descriptions

1. `0-basic_async_syntax.py`: Implements a basic asynchronous coroutine.
2. `1-concurrent_coroutines.py`: Executes multiple coroutines concurrently.
3. `2-measure_runtime.py`: Measures the runtime of asynchronous executions.
4. `3-tasks.py`: Creates asyncio Tasks.
5. `4-tasks.py`: Implements a variation of wait_n using Tasks.

## Usage

Each file can be run independently. For example:

```bash
./0-main.py
./1-main.py
# ... and so on for each task
```

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Author

Ermiyas SOlomon