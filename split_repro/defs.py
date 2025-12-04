from typing import Protocol, runtime_checkable

class Model:
    """A simple user-defined class."""
    pass

@runtime_checkable
class Converter(Protocol):
    def convert(self, model: Model) -> None: ...

class MyConverter:
    def __init__(self, name: str):
        self.name = name

    def convert(self, model: Model) -> None:
        pass

