from typing import Iterable


def list_elements(elements: Iterable[str]) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=": ")


people: list[str] = ["Mario", "Luigi", "Peach"]
list_elements(people)

# error
# list_elements(10)

numbers: list[int] = [1, 2, 3]
# error
list_elements(numbers)
