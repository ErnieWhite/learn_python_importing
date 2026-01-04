"""
Pytest tests demonstrating import usage.

Run with:
    pytest -q
"""

def test_absolute_imports():
    import importing_demo
    from importing_demo.math_ops import add
    assert add.add(1, 2) == 3

def test_relative_behavior_within_package():
    # Importing a module that uses a relative import internally
    from importing_demo.math_ops.add import add_and_greet
    assert "sum is 3" in add_and_greet(1, 2, name="Tester")

def test_package_data_access():
    import importing_demo
    text = importing_demo.read_sample()
    assert "sample package data" in text

def test_utils_import():
    from importing_demo import utils
    assert utils.greet("X") == "Hello, X!"