from typing import NewType, TypeAlias


UserId: TypeAlias = int


def get_user(userid: UserId) -> str | None:
    users: dict = {0: "Mario", 1: "Luigi", 2: "Peach"}
    return users.get(userid)


print(get_user(0))
print(get_user(False))
print(get_user(UserId(0)))


NewUserId = NewType("NewUserId", int)


def get_another_user(userid: NewUserId) -> str | None:
    ...


print(get_another_user(0))  # error
print(get_another_user(False))  # error
print(get_another_user(NewUserId(0)))
