# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return f'"Name: "\t{self.name}\n "Current Room: " \t{self.location}\n \n "Inventory:"\t{" ".join(str(item) for item in self.inventory) if len(self.inventory) > 0 else "Inventory Empty"}'
    
    def print_inventory(self):
        print(f'{" ".join(str(item) for item in self.inventory), " ".join(str(weapon) for weapon in self.inventory) if len(self.inventory) > 0 else "Inventory Empty"}')

    def get(self, item):
        self.inventory.append(item)
        return
    
    def drop(self, item):
        self.inventory.remove(item)
        return