# importing-demo

A compact, hands‑on project that teaches Python importing, module/package layout, and common import techniques.

Contents
- src/importing_demo: the package you'll import from
- scripts/run_demo.py: run examples
- tests/test_imports.py: pytest tests demonstrating imports
- pyproject.toml: lightweight packaging and editable install

What you'll learn
- Absolute imports vs relative imports
- Package layout (src/ pattern) and __init__.py
- Namespace packages (PEP 420) and when __init__.py is required
- Importing package data (importlib.resources)
- Editable installs (pip install -e .) and PYTHONPATH
- importlib.reload, import caching, and avoiding circular imports
- Best practices for public APIs and __all__

Quick start (recommended)
1. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows

2. Install in editable mode:
   pip install -e .

3. Run the demo script:
   python scripts/run_demo.py

4. Run tests (requires pytest):
   pip install pytest
   pytest -q

If you prefer not to install, you can also:
- Run examples by adding the project root to PYTHONPATH:
  PYTHONPATH="$(pwd)/src" python -c "import importing_demo; print(importing_demo.__version__)"

Project layout
- src/importing_demo/__init__.py: package metadata + public API
- src/importing_demo/utils.py: helper functions (used with relative import)
- src/importing_demo/math_ops/add.py: add function
- src/importing_demo/math_ops/mul.py: multiply function (demonstrates relative imports)
- src/importing_demo/math_ops/__init__.py: re-exports math_ops public symbols
- src/importing_demo/data/sample.txt: package data accessed via importlib.resources
- scripts/run_demo.py: shows absolute and relative import usage and package data access
- tests/test_imports.py: tests showing different import styles

Exercises
1. Remove src/importing_demo/math_ops/__init__.py and try importing. Observe behavior (namespace package).
2. Modify a module and use `importlib.reload()` from a REPL to see changes without restarting the REPL.
3. Create a sibling package (outside `importing_demo`) and import across packages using absolute imports.

Notes and tips
- Use absolute imports for public APIs: `from importing_demo.math_ops import add`
- Use explicit relative imports for intra‑package references: `from .add import add`
- Keep package public surface small; re-export in __init__.py and document with __all__
- Avoid putting business code in __init__.py; keep __init__ light to reduce import cost and circular import pain
- For package data, prefer importlib.resources (Py3.7+) instead of reading files by path

Happy learning!