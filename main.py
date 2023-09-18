from typing import Protocol
from dataclasses import dataclass


class Printer(Protocol):
    def print(self, magazine: str) -> None:
        ...

    def copy(self, magazine: str, copies: int) -> None:
        ...


@dataclass
class LazerPrinter:
    name: str
    version: int

    def print(self, magazine: str) -> None:
        print(f"{self.name} (v{self.version}) is printing: '{magazine}'")

    def copy(self, magazine: str, copies: int) -> None:
        print(
            f"{self.name} (v{self.version}) is printing {copies} copies of: '{magazine}'"
        )


@dataclass
class InkJetPrinter:
    name: str
    version: int

    def print(self, magazine: str) -> None:
        print(f"{self.name} (v{self.version}) is printing: '{magazine}'")

    def copy(self, magazine: str, copies: int) -> None:
        print(
            f"{self.name} (v{self.version}) is printing {copies} copies of: '{magazine}'"
        )


def print_magazine(printer: Printer, magazine: str) -> None:
    printer.print(magazine)
    printer.copy(magazine, 5)


lp: LazerPrinter = LazerPrinter("Lazer Printer", 1)

lp_printer: Printer = LazerPrinter(
    "Lazer Printer", 2
)  # no errors because Lazerprinter implements print and copy

ijp: InkJetPrinter = InkJetPrinter("InkJet Printer", 1)


print_magazine(lp, "Go")
print_magazine(ijp, "Python")
