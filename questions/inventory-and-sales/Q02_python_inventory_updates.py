"""
QUESTION:
Model an inventory as a list of (product, quantity) pairs. Implement pure functions that add stock,
remove stock safely, update the list through a higher-order function, and determine the product with
the highest quantity using a reduction.

CONCEPT:
Higher-order functions, immutable list transformation, reduction, tuple processing.

DIFFICULTY:
Intermediate

APPROACH:
Each update returns a new inventory instead of mutating the input list. The inventory is rebuilt with
list comprehensions and recursive logic is avoided only where direct functional transformation is more
readable. `reduce` is used to compute the highest-stock product.

EXAMPLE RUN:
Added inventory: [('apple', 15), ('banana', 8), ('pear', 11)]
Reduced inventory: [('apple', 10), ('banana', 8), ('pear', 11)]
Highest stock: ('pear', 11)

NOTES:
The original solution mutated the list in place and did not reliably handle missing products. This
version keeps the same problem intent while making each step pure and explicit.
"""

from functools import reduce

Product = str
Quantity = int
Inventory = list[tuple[Product, Quantity]]


def add_stock(inventory: Inventory, item: tuple[Product, Quantity]) -> Inventory:
    product, quantity = item
    if quantity <= 0:
        raise ValueError("Quantity to add must be positive.")

    if any(name == product for name, _ in inventory):
        return [
            (name, available + quantity) if name == product else (name, available)
            for name, available in inventory
        ]

    return inventory + [(product, quantity)]


def remove_stock(inventory: Inventory, item: tuple[Product, Quantity]) -> Inventory:
    product, quantity = item
    if quantity <= 0:
        raise ValueError("Quantity to remove must be positive.")

    matching_entries = list(filter(lambda entry: entry[0] == product, inventory))
    if not matching_entries:
        raise ValueError("No products left with the requested name.")

    available = matching_entries[0][1]
    if available < quantity:
        raise ValueError("Insufficient stock for the requested removal.")

    return list(
        filter(
            lambda entry: entry[1] > 0,
            [
                (name, available_qty - quantity) if name == product else (name, available_qty)
                for name, available_qty in inventory
            ],
        )
    )


def update_stock(
    updater, inventory: Inventory, item: tuple[Product, Quantity]
) -> Inventory:
    return updater(inventory, item)


def highest_quantity(inventory: Inventory) -> tuple[Product, Quantity] | None:
    if not inventory:
        return None

    return reduce(
        lambda current, candidate: candidate if candidate[1] > current[1] else current,
        inventory[1:],
        inventory[0],
    )


if __name__ == "__main__":
    base_inventory = [("apple", 10), ("banana", 8), ("pear", 11)]
    expanded_inventory = update_stock(add_stock, base_inventory, ("apple", 5))
    reduced_inventory = update_stock(remove_stock, expanded_inventory, ("apple", 5))

    print("Added inventory:", expanded_inventory)
    print("Reduced inventory:", reduced_inventory)
    print("Highest stock:", highest_quantity(reduced_inventory))
