# Python-Notes-And-Projects

## Python Inner working

When we create a python file (like - hello.py) and run it then the steps is happening are:

- It is firstly converted into `Byte Code` that is mostly hidden file( sometime it is visible) then it go to `Python VM` where your actual code is run.

**Note: Python Virtual Machine(PVM) it installed at the time of python installation**

```
- Step1: Compile to Byte code(It is low level code not a machine code and it is platform independent)

-> Byte code is runs faster 
    .pyc -> it is compiled file of python and it also known as (frozen binaries)

    __pycache__ -> It is organised folder created by Python itself to manages the source change and maintains the python version (by using some diffing algo).

-> Works only for imported files (.pyc files)
-> Not for top level files

```

**Python Virtual Machine**

- Code loop to iterate byte code.
- Runtime Engine
- Also known as python Interpreter

**Byte code is NOT machine code**
- Python specific interpretation
- cpython (Standard Implementation), jython, Iron Python, Stackles, PyPy




