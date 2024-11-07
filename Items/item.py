import csv

class Item:
    #class atrributes
    pay_rate = 0.8
    all = []

    #constructor
    def __init__(self, name: str, price: float, quantity=0):
        #evaluate parameter passed
        assert price >= 0, "Price must be positive"
        assert quantity > 0, "Price must be positive"

        #instance attribute
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        return self.__price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # check if decimal is not zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    #object representation using a magic method repr
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.__price}, {self.quantity})'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >= 10:
            raise Exception("Name too long")
        else:
            self.__name = value


"""
print(Item.is_integer(3.6))
Item.instantiate_from_csv()
print(Item.all)
"""