from items.item import Item

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def __str__(self):
        return f'{self.name}\n {self.description}\n this weapon can inflict {self.damage} damage points'

    def on_take(self):
        print(f'You have picked up the {self.name}.')

    def on_drop(self):
        print(f'You have dropped the {self.name}.')

    