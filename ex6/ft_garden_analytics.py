class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float | int,
        age_days: int
    ) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        self._stats = Plant.Statistics()

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: "
            f"{self._height}cm, "
            f"{self._age_days} days old"
        )
        self._stats.add_show()

    def grow(self, grow_height: float = 8.0) -> None:
        self._height += grow_height
        self._stats.add_grow()

    def age(self, aging_days: int = 1) -> None:
        self._age_days += aging_days
        self._stats.add_age()

    @staticmethod
    def check_year_old(age_days: int) -> None:
        print(
            f"Is {age_days} days more than a year? -> "
            f"{age_days > 365}"
        )

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_statistics(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float | int,
        age_days: int,
        color: str = "red",
        bloomed: bool = False
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = bloomed

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

        if self._bloomed:
            print(
                f"{self._name.capitalize()} "
                f"is blooming beautifully!"
            )
        else:
            print(
                f"{self._name.capitalize()} "
                f"has not bloomed yet"
            )


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float | int,
        age_days: int,
        trunk_diameter: float | int = 5.0
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter
        self._tree_stats = Tree.TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.add_shade()

        print(
            f"Tree {self._name.capitalize()} now produces "
            f"a shade of {self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: "
            f"{self._trunk_diameter}cm"
        )


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float | int,
        age_days: int,
        color: str = "yellow",
        bloomed: bool = False,
        seeds: int = 0
    ) -> None:
        super().__init__(
            name,
            height,
            age_days,
            color,
            bloomed
        )
        self._seeds = seeds

    def grow_and_bloom(
        self,
        grow_height: float,
        aging_days: int,
        seeds: int
    ) -> None:
        self.grow(grow_height)
        self.age(aging_days)
        self.bloom()
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(
        f"[statistics for "
        f"{plant._name.capitalize()}]"
    )
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.check_year_old(30)
    Plant.check_year_old(400)

    print("=== Flower")
    rose = Flower("rose", 15.0, 10)
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed(
        "sunflower",
        80.0,
        45
    )
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow_and_bloom(
        30.0,
        20,
        42
    )

    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
