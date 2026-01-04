"""
importing_demo package

This file exposes a minimal public API for the package.
Keep it light to avoid heavy import costs and circular imports.
"""

__all__ = ["math_ops", "utils", "read_sample", "__version__"]

# package metadata
__version__ = "0.1.0"

# Re-export subpackages / modules for a nice top-level API
# Use absolute imports for clarity
from importing_demo import utils  # public utils
from importing_demo import math_ops  # math_ops subpackage

# A convenience function that uses importlib.resources to read bundled data
def read_sample():
    try:
        # Python >=3.9: importlib.resources.files
        import importlib.resources as resources
        return resources.files("importing_demo").joinpath("data").joinpath("sample.txt").read_text()
    except Exception:
        # fallback for older stdlib variations
        import pkgutil
        data = pkgutil.get_data("importing_demo", "data/sample.txt")
        return data.decode() if data else None