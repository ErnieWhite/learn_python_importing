# mul.py demonstrates a sibling import (absolute or relative both work)
# We'll use absolute import here to show the contrast
from importing_demo.utils import greet  # absolute import (works once package is installed / on PYTHONPATH)

def mul(a, b):
    """Multiply two numbers."""
    return a * b

def mul_and_greet(a, b, name="Learner"):
    """Example combining a math function and a util."""
    p = mul(a, b)
    return f"{greet(name)} The product is {p}"