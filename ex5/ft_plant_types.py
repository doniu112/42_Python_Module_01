class Plant:
    def __init__(
        self,
        name: str,
        height: float | int,
        age_days: int
    ) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {self._height}cm, "
            f"{self._age_days} days old"
        )

    def grow(self, grow_height: float = 0.8) -> None:
        self._height += grow_height

    def age(self, aging_days: int = 1) -> None:
        self._age_days += aging_days

    def set_height(self, new_height: float | int = 15) -> float | int:
        if new_height < 0:
            print(f"{self._name.capitalize()}: Error, "
                  f"height can't be negative\n"
                  f"Height update rejected")
            return self._height
        self._height = new_height
        print(f"Height updated: {self._height}cm")
        return self._height

    def set_age(self, new_age: int = 15) -> int:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative\n"
                  f"Age update rejected")
            return self._age_days
        self._age_days = new_age
        print(f"Age updated: {self._age_days} days old")
        return self._age_days

    def get_height(self) -> float | int:
        return round(self._height, 1)

    def get_age(self) -> int:
        return self._age_days


class Flower(Plant):
    def __init__(self,
                 flower_name: str,
                 flower_height: float | int,
                 flower_age_days: int,
                 color: str = 'red',
                 bloomed: bool = False) -> None:
        super().__init__(name=flower_name,
                         height=flower_height,
                         age_days=flower_age_days)
        self._color = color
        self.bloomed = bloomed

    def bloom(self) -> bool:
        if self.bloomed:
            return self.bloomed
        else:
            print(f"[asking the {self._name} to bloom]")
            self.bloomed = True
            return self.bloomed

    def show(self) -> None:
        Plant.show(self)
        print(f"Color: {self._color}")
        if self.bloomed:
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 tree_name: str,
                 tree_height: float | int,
                 tree_age_days: int,
                 trunk_diameter: float | int = 5,
                 shade: bool = False) -> None:
        super().__init__(
            name=tree_name,
            height=tree_height,
            age_days=tree_age_days
        )
        self._trunk_diameter = trunk_diameter
        self._shade = shade

    def produce_shade(self) -> bool:
        if self._shade:
            return self._shade
        else:
            print(f"[asking the {self._name} to produce shade]")
            self._shade = True
            print(f"Tree {self._name.capitalize()} now produces "
                  f"a shade of {self._height}cm long and "
                  f"{self._trunk_diameter}cm wide.")
            return self._shade

    def show(self) -> None:
        Plant.show(self)
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 vegetable_name: str,
                 vegetable_height: float | int,
                 vegetable_age_days: int,
                 harvest_season: str = "april",
                 nutritional_value: float | int = 0) -> None:
        super().__init__(
            name=vegetable_name,
            height=vegetable_height,
            age_days=vegetable_age_days
        )
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season

    def show(self) -> None:
        Plant.show(self)
        print(f"Harvest season: {self._harvest_season.capitalize()}")
        print(f"Nutritional value: {self._nutritional_value}")

    def vegetable_grow(self, days: int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        for day in range(days):
            Plant.age(self)
            Plant.grow(self, 1)
            self._nutritional_value += 1


def main():
    print("=== Garden Plant Types ===")

    print("=== Flower ===")
    rose = Flower("rose", 10, 15)
    rose.show()
    rose.bloom()
    rose.show()
    print("\n")

    print("=== Tree ===")
    oak = Tree("oak", 200.0, 15)
    oak.show()
    oak.produce_shade()
    print("\n")

    print("=== Vegetable ===")
    tomato = Vegetable("tomato", 10, 15)
    tomato.show()
    tomato.vegetable_grow(20)
    tomato.show()
    print("\n")


if __name__ == "__main__":
    main()
