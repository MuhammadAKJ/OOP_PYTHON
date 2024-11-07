from item import Item

class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )


"""
item1 = Item("Keyboard", 234, 5)
phone1 = Phone('Xiaomi', 500, 10, 4)
print(Phone.all)
"""