import promotions

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None
        self.multiple_promotion = []
        if len(self.name) == 0 or self.price < 0 or self.quantity < 0:
            raise Exception("Sorry, no empty name or numbers below zero")

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
        return f"{self.name}, Price : {self.price} $, Quantity : {self.quantity}"

    def buy(self, quantity) -> float:
        multiple_promotion_price = 0
        multiple_promotion_price_new = 0
        price = self.price * quantity
        if self.promotion is not None:
            return self.promotion.apply_promotion(price, quantity)
        elif len(self.multiple_promotion) > 1:
            promotion1 = self.multiple_promotion[0]
            promotion2 = self.multiple_promotion[1]
            multiple_promotion_price = promotion1.apply_promotion(price, quantity)
            multiple_promotion_price_new = promotion2.apply_promotion(multiple_promotion_price, quantity)
            return multiple_promotion_price_new
        else:
            return price

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def multiple_promotions(self, promotions=[]):
        for promotion in promotions:
            self.multiple_promotion.append(promotion)

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum
