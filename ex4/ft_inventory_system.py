#!/usr/bin/env python3


import sys


def parse_inventory_args(args: list[str]) -> dict[str, int]:

    inventory: dict[str, int] = {}

    for arg in args:
        try:

            parts = arg.split(':')

            if len(parts) != 2:
                print(f"Warning: Invalid format '{arg}'"
                      ", expected 'item:quantity'")
                continue

            item_name = parts[0]
            quantity = int(parts[1])

            inventory[item_name] = quantity

        except ValueError as e:
            print(f"Warning: Invalid quantity in '{arg}': {e}")
            continue

    return inventory


def analyze_inventory(inventory: dict[str, int]) -> None:

    print("=== Inventory System Analysis ===")

    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")

    unique_types = len(inventory)
    print(f"Unique item types: {unique_types}")

    print()
    print("=== Current Inventory ===")

    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)

    for item, quantity in sorted_items:

        percentage = (quantity / total_items) * 100

        unit_text = "unit" if quantity == 1 else "units"

        print(f"{item}: {quantity} {unit_text} ({percentage:.1f}%)")

    print()
    print("=== Inventory Statistics ===")

    most_abundant = max(inventory.items(), key=lambda x: x[1])
    print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")

    least_abundant = min(inventory.items(), key=lambda x: x[1])
    print(f"Least abundant: {least_abundant[0]} ({least_abundant[1]} unit)")

    print()
    print("=== Item Categories ===")

    categories: dict[str, dict[str, int]] = {
        "Abundant": {},    # Items with quantity >= 5
        "Moderate": {},    # Items with quantity 3-4
        "Scarce": {}       # Items with quantity 1-2
    }

    for item, quantity in inventory.items():
        if quantity >= 5:
            categories["Abundant"][item] = quantity
        elif quantity >= 3:
            categories["Moderate"][item] = quantity
        else:
            categories["Scarce"][item] = quantity

    for category, items in categories.items():
        if items:
            print(f"{category}: {items}")

    print()
    print("=== Management Suggestions ===")

    restock_needed = [item for item, qty in inventory.items() if qty == 1]

    if restock_needed:
        print(f"Restock needed: {restock_needed}")
    else:
        print("All items well-stocked!")

    print()
    print("=== Dictionary Properties Demo ===")

    print(f"Dictionary keys: {list(inventory.keys())}")

    print(f"Dictionary values: {list(inventory.values())}")

    sword_qty = inventory.get("sword", 0)
    print(f"Sample lookup - 'sword' in inventory: {sword_qty > 0}")


def main() -> None:
    """
    Main function that processes inventory from command-line arguments.
    """

    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py "
              "item:quantity item:quantity ...")
        print("Example: python3 ft_inventory_system.py"
              "sword:1 potion:5 shield:2")
        return

    inventory = parse_inventory_args(sys.argv[1:])

    if not inventory:
        print("No valid inventory items to analyze!")
        return

    analyze_inventory(inventory)


if __name__ == "__main__":
    main()
