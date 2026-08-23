class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    rose = Plant("rose", 19, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    start_height = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        rose.show()
    growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {growth}cm")
