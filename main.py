from typing import Callable
from datetime import datetime


def get_time() -> str:
    return f"{datetime.now():%H:%M:%S}"


def repeat(func: Callable, amount: int) -> None:
    for i in range(amount):
        print(i + 1)
        print(func())


repeat(get_time, 3)
# repeat("bla", 5) # error


def print_it(text: str, printer: Callable[[str], None]) -> None:
    printer(text)


def loud_print(text: str) -> None:
    print(text.upper())


def print_number(number: int) -> None:
    print(number)


def louder(text: str) -> str:
    return text.upper()


print_it("hello", loud_print)
print_it("hello", print_number)  # error
print_it("hello", louder)  # error
