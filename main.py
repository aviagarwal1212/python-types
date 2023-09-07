coordinate: tuple[int, int] = (20, 30)
coordinate_2: tuple[int, int, int, int] = (10, 20, 30, 40)
coordinate_3: tuple[int, ...] = (10, 20, 30, 40)
coordinate_4: tuple[int | str, ...] = (10, 20, "30", "40")


def test():
    print()
