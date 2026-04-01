class Inventory:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f" Added {item} to {self.owner}'s inventory.")

    def __str__(self):
        item_list = ", ".join(self.items)
        return f"{self.owner}'s Inventory: [{item_list}]"

    def __len__(self):
        return len(self.items)          # ← your one-liner!

    def __add__(self, other):
        combined_inventory = Inventory(f"{self.owner} & {other.owner}")
        combined_inventory.items = self.items + other.items
        return combined_inventory


# --- Testing the Magic ---

arthur_inv = Inventory("Arthur")
arthur_inv.add_item("Sword")
arthur_inv.add_item("Shield")

gandalf_inv = Inventory("Gandalf")
gandalf_inv.add_item("Staff")
gandalf_inv.add_item("Health Potion")

print("-" * 20)

print(arthur_inv)    # calls __str__ automatically
print(gandalf_inv)

print(f"Arthur has {len(arthur_inv)} items.")   # calls __len__
print(f"Gandalf has {len(gandalf_inv)} items.")

party_inv = arthur_inv + gandalf_inv            # calls __add__
print(party_inv)
