def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def display_inventory(inventory):
    item_list = []
    for item, value in inventory.items():
        item_list.append(f"{item}: {value}")
    return "\n".join(item_list)

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
print(display_inventory(inv))