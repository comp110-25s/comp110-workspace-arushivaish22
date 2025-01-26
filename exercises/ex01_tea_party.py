"""A program to plan a giant tea party"""

__author__: str = "730579218"


def main_planner(guests: int) -> None:
    """Main tea party planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )


def tea_bags(people: int) -> int:
    """Returns the number of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Returns the number of treats needed"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the total cost of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
