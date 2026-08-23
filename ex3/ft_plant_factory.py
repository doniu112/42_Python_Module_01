class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, "
            f"{self.age_days} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")

    print("Created: ", end="")
    rose.show()

    print("Created: ", end="")
    oak.show()

    print("Created: ", end="")
    cactus.show()

    print("Created: ", end="")
    sunflower.show()

    print("Created: ", end="")
    fern.show()
