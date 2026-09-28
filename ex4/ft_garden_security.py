class Plant:
    def __init__(
        self,
        name: str,
        height: float | int = 0,
        age_days: int = 0
    ) -> None:
        self._name = name
        self._height: float | int = 0.0
        self._age_days: int = 0
        self.set_height(height)
        self.set_age(age_days)

    def show(self) -> None:
        print(
            f"{self._name}: {self._height}cm, "
            f"{self._age_days} days old"
        )

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_days += 1

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


def main() -> None:
    rose = Plant("rose", 10.0, 20)
    print("=== Garden Security System ===")
    print("Plant Created: ", end="")
    rose.show()
    print()
    rose.set_height(20)
    rose.set_age(30)
    print()
    rose.set_height(-20)
    rose.set_age(-20)
    print()
    print(f"Current state: Rose: {rose.get_height()}cm, "
          f"{rose.get_age()} days old")


if __name__ == "__main__":
    main()
