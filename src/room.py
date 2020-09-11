# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[], weapons=[]):
        self.name = name
        self.description = description
        self.items = items
        self.weapons = weapons

    def remove_item(self, item):
        self.items.remove(item)
        return 
    
    def remove_weapon(self, weapon):
        self.weapons.remove(weapon)
        return

    def store_item(self, item):
        self.items.append(item)
        return
    
    def store_weapon(self, weapon):
        self.weapons.append(weapon)
        return 
    
    def __str__(self):
        return f'{self.name}\n\n{self.description}\n\n"Items in this room:"\t{self.items}\n "Weapons in this room:"\t{self.weapons}'