from typing import Sequence


sample_set: set[int] = {1, 2, 3}
sample_list: list[int] = [1, 2, 3]


def get_first_element(sequence: Sequence[int]) -> int:
    return sequence[0] if sequence else -1


# print(get_first_element(sample_set))  # error
print(get_first_element(sample_list))
