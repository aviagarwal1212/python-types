from typing import Any
from sys import getsizeof


def get_size(user_input: Any) -> str:
    return f"{getsizeof(user_input)} bytes"


print(get_size([1, 2, 3]))
print(get_size("this is a string"))
print(get_size(True))
print(get_size(89))
print(get_size(None))
