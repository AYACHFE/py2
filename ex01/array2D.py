

def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list and return a sliced set of rows."""
    if not isinstance(family, list) or not family:
        return []
    if not all(isinstance(row, list) for row in family):
        return []
    if not all(len(row) == len(family[0]) for row in family):
        return []
    if not isinstance(start, int) or not isinstance(end, int):
        return []

    shape = (len(family), len(family[0]))
    print(f"My shape is : {shape}")

    sliced = family[start:end]
    print(f"My new shape is : {(len(sliced), len(family[0]))}")
    return sliced
