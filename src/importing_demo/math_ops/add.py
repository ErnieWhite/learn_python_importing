# add.py demonstrates a simple function and an intra-package relative import
from ..utils import greet  # relative import: go up one package and import utils

def add(a, b):
    """Add two numbers (simple example)."""
    return a + b

def add_and_greet(a, b, name="Learner"):
    """Small example using a cross-module call via relative import."""
    s = add(a, b)
    return f"{greet(name)} The sum is {s}"