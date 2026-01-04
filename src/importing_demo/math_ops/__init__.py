"""math_ops package

This package demonstrates:
- Relative imports within a package
- Re-exporting public API at the subpackage level
"""

# Explicitly export public symbols to define the subpackage public API
__all__ = ["add", "mul"]

# Re-export functions from sibling modules using relative imports
from .add import add
from .mul import mul