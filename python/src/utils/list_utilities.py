from typing import TypeVar


T = TypeVar("T")


def flatten(list: list[list[T]]) -> list[T]:
    return [element for sublist in list for element in sublist]
