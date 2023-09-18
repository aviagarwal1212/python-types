from dataclasses import dataclass
from typing import TypeAlias, Callable, Literal

OptionalStr: TypeAlias = str | None
Mode: TypeAlias = Literal["r"]

Printer: TypeAlias = Callable[[str], None]

FruitType: TypeAlias = "Fruit"


@dataclass
class Fruit:
    name: str

    def fruit_method(self) -> FruitType:
        return self
