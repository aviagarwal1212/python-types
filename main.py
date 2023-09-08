class Fruit:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.name} (weight: {self.weight})"


orange: Fruit = Fruit("orange", 100)

# error because Fruit class has the Fruit type
# apple: int = Fruit("apple", 100)

# error because type annotation
# apple: Fruit = Fruit(100, 100)


def describe(fruit: Fruit):
    print(f"{fruit.name} weighs {fruit.weight}g")


describe(orange)


class Apple(Fruit):
    ...


fuji_apple: Apple = Apple("fuji apple", 200)
describe(fuji_apple)
print(fuji_apple)

# not an error
desi_apple: Fruit = Apple("desi apple", 150)
