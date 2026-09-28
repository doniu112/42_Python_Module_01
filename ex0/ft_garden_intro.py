def ft_display(plant: str, height: float | int, age: int) -> None:
    welcome_message = "=== Welcome to My Garden ==="
    end_message = "=== End of Program ==="
    print(f"{welcome_message}\n"
          f"Plant: {plant.capitalize()}\n"
          f"Height: {height}cm\n"
          f"Age: {age} days\n"
          f"\n{end_message}")


def main() -> None:
    ft_display("rose", 25, 30)


if __name__ == "__main__":
    main()
