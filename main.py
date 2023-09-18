from typing import Literal

Mode = Literal["r", "w", "a"]


def read_file(file: str, mode: Mode) -> None:
    print(f"Reading {file} in {mode} mode")


read_file("stocks.csv", "r")
read_file("stocks.csv", "rw")  # error


def read_another_file(file: str, mode: Literal["r", "w", "a"]) -> None:
    ...


read_another_file("stocks.csv", "rw")  # error
