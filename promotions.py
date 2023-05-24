from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_promotion(self, quantity, price):
        pass

class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity):
        price = price / quantity
        price_lst = []
        for i in range(1, quantity+1):
            if i % 2 == 0:
                price_lst.append(price * 0.5)
            else:
                price_lst.append(price)
        return sum(price_lst)

class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity):
        price = price / quantity
        price_lst = []
        for i in range(1, quantity+1):
            if i % 3 == 0:
                price_lst.append(0)
            else:
                price_lst.append(price)
        return sum(price_lst)

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        return price - (price * self.percent / 100)


