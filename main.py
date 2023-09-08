def add_numbers(a: int, b: int) -> int:
    return a + b


# error
# add_numbers(10, 20.0)


def return_nothing(a: int) -> None:
    # error
    # return a
    print(a)


def return_nothing_also(a: int):
    # no error
    return a


def fetch_user(user_id: int) -> str | None:  # returning an optional
    users: dict[int, str] = {0: "Mario", 1: "Luigi"}
    return users.get(user_id)


fetch_user(1)
fetch_user(99)
