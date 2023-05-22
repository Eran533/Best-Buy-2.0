class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        if name == "" or price < 0 or quantity < 0:
            raise Exception("Sorry, no numbers below zero or empty name")

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        if self.quantity > 0:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        print(f"Name : {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        price = self.price * quantity
        if self.quantity - quantity < 0:
            raise Exception(f"I don't have enough stock, I have {self.quantity} of {self.name}")
        else:
            self.quantity -= quantity
        return price
