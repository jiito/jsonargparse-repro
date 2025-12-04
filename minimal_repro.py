"""
MINIMAL REPRODUCTION: jsonargparse Protocol bug

jsonargparse version: 4.42.0

BUG: jsonargparse fails with "does not implement protocol" when a Protocol
method signature contains a user-defined class as a type annotation.

WORKS:
  - Protocol methods with no typed parameters
  - Protocol methods with built-in types (int, str, etc.)
  - Protocol methods with typing.Any

FAILS:
  - Protocol methods with user-defined class types
  - Protocol methods with Union of user-defined classes

Run to reproduce:
    uv run python minimal_repro.py --config minimal_repro.yaml
"""

from typing import Protocol, runtime_checkable
from jsonargparse import CLI


class Model:
    """A simple user-defined class - THIS triggers the bug."""

    pass


@runtime_checkable
class Converter(Protocol):
    # Using "Model" (a user-defined class) causes the bug
    def convert(self, model: Model) -> None: ...


class MyConverter:
    def __init__(self, name: str):
        self.name = name

    # Even with matching signature, it fails
    def convert(self, model: Model) -> None:
        pass


def main(converter: Converter):
    print(f"Success! converter={converter}")


if __name__ == "__main__":
    CLI(main)
