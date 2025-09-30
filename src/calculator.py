"""
TinyTools Calculator library: add, subtract, multiply, divide.
"""
from __future__ import annotations

def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return a / b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
