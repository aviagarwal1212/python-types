# for python under 3.10
from typing import Optional

person: Optional[str] = "Luigi"
person = None

# also valid >= py3.10
person: str | None = "Luigi"
person = None


def greet(name: str | None = None):
    if name is None:
        print("No one is here")
    else:
        print(name)


greet(person)
greet(None)
greet()
# error
# greet(10)
