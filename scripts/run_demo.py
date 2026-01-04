"""
Demo script showing different import styles and package data access.

Run after installing the package in editable mode:
    pip install -e .
Then:
    python scripts/run_demo.py
"""

# Absolute import of subpackage
import importing_demo
from importing_demo.math_ops import add, mul  # absolute import from public API
from importing_demo import utils

print("Package version:", importing_demo.__version__)

print("Absolute import add:", add.add(2, 3))
print("Absolute import mul:", mul.mul(4, 5))

# Using a convenience function defined in __init__.py that reads package data
print("--- package data sample.txt ---")
print(importing_demo.read_sample())

# Using a function that uses relative import internally
from importing_demo.math_ops.add import add_and_greet
print(add_and_greet(1, 2, name="Ernie"))

# Demonstrate importlib.reload to reflect code changes at runtime (interactive use)
import importlib
print("Reloading importing_demo.math_ops...")
importlib.reload(importing_demo.math_ops)
print("Done reload.")