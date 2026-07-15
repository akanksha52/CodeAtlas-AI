from app.parser.python_parser import PythonParser

parser = PythonParser()

code = b"""
import os
from pathlib import Path


class User:

    def login(self, username, password):
        print("Logging in")


def add(a, b):
    result = a + b
    return result
"""

symbols = parser.parse(code)

print("=" * 80)
print("Extracted Symbols")
print("=" * 80)

for symbol in symbols:
    print(symbol)

    if hasattr(symbol, "source_code"):
        print("\nSource Code:")
        print(symbol.source_code)

    print("-" * 80)