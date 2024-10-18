# Python Async Comprehension

This project explores asynchronous comprehensions and generators in Python. It contains three main tasks that demonstrate the use of async generators, async comprehensions, and parallel execution of async functions.

## Learning Objectives

By the end of this project, you should be able to:

- Write an asynchronous generator
- Use async comprehensions
- Type-annotate generators

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- pycodestyle style (version 2.5.x)

## Files

1. `0-async_generator.py`: Contains an async generator that yields random numbers.
2. `1-async_comprehension.py`: Implements an async comprehension using the async generator.
3. `2-measure_runtime.py`: Measures the runtime of parallel async comprehensions.

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.

### 1. Async Comprehensions

Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

### 2. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

## Usage

To run the tasks, execute the corresponding main files:

```
./0-main.py
./1-main.py
./2-main.py
```

## Author

Ermiyas Solomon