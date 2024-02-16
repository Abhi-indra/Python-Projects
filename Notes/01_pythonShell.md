# Python Shell Documentation

Welcome to the Python Shell documentation! This documentation provides an overview of Python's interactive shell, which allows users to execute Python code in an interactive manner. This document covers basic usage, features, and best practices.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic Usage](#basic-usage)
3. [Features](#features)
4. [Best Practices](#best-practices)
5. [Examples](#examples)

## Introduction

Python provides an interactive shell that allows users to execute Python code statements and expressions line by line. This shell provides a convenient way to experiment with Python code, test algorithms, and debug programs interactively.

## Basic Usage

To start the Python interactive shell, open a terminal or command prompt and type `python` or `python3` depending on your Python installation. This will launch the Python shell, and you'll see a prompt (`>>>`) where you can start typing Python code.

```bash
$ python
Python 3.9.5 (default, May 18 2021, 14:45:23)
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Once you see the prompt (`>>>`), you can start typing Python code and press `Enter` to execute it.

## Features

- **Tab Completion**: Python shell supports tab completion, which helps in exploring available modules, classes, functions, and methods. Pressing the `Tab` key will show available completions.
- **History**: Previous commands can be accessed using the up and down arrow keys.
- **Help**: The `help()` function provides information about objects, modules, functions, classes, etc.
- **Multiline Statements**: Python shell supports multiline statements. To continue a statement on the next line, use the ellipsis (`...`) prompt.
- **Documentation Access**: You can access Python's official documentation directly from the shell by typing `help()` or `?`.

## Best Practices

- **Experiment**: Python shell is an excellent tool for experimentation. Use it to test small code snippets and explore Python features.
- **Documentation**: Utilize the built-in `help()` function to get information about Python objects and modules.
- **Use Tab Completion**: Take advantage of tab completion to explore available modules, functions, and attributes.
- **Keep it Clean**: Avoid cluttering the shell with unnecessary code. Clear the screen (`Ctrl + L` or `Cmd + K`) when needed.

## Examples

### Simple Arithmetic Operations

```python
>>> 2 + 3
5
>>> 10 - 4
6
>>> 5 * 3
15
>>> 20 / 4
5.0
```

### String Manipulation

```python
>>> greeting = "Hello"
>>> name = "Alice"
>>> greeting + ", " + name + "!"
'Hello, Alice!'
```

### List Operations

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> sum(numbers)
15
>>> len(numbers)
5
>>> numbers.append(6)
>>> numbers
[1, 2, 3, 4, 5, 6]
```

### Function Definition and Invocation

```python
>>> def greet(name):
...     return "Hello, " + name + "!"
...
>>> greet("Bob")
'Hello, Bob!'
```

### Tab Completion

```python
>>> import math
>>> math.
math.acos    math.acosh   math.asin    math.asinh
math.atan    math.atan2   math.atanh   math.ceil
math.comb    math.copysign    math.cos     math.cosh
math.degrees    math.dist    math.erf     math.erfc
...
```

This concludes the documentation for Python Shell. Happy coding! 🐍✨