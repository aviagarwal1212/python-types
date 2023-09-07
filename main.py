my_dict: dict = {"a": 10}
typed_dict: dict[str, int] = {"a": 10}
test_dict: dict[int, str] = {1: "first", 2: "second"}


def print_it(some_dict: dict[int, str]):
    for value in some_dict.values():
        print(value.title())


print_it(test_dict)

# error
# print_it(typed_dict)
