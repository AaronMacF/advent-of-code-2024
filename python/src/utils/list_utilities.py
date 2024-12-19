def flatten(list: list[list]) -> list:
    return [element for sublist in list for element in sublist]
