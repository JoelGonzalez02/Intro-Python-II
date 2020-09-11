# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items
        

    def __str__(self):
        return f'"Name: "\t{self.name}\n "Current Room: " \t{self.location}\n \n "Inventory:"\t{" , ".join(str(item) for item in self.items) if len(self.items) > 0 else "Inventory Empty"}\n'
    
    def print_inventory(self):
        print(f'{" ".join(str(item) for item in self.items), " ".join(str(weapon) for weapon in self.weapons) if len(self.items) and len(self.weapons) > 0 else "Inventory Empty"}')

    def get(self, item):
        self.items.append(item)
        return
    
    def drop(self, item):
        self.items.remove(item)
        return