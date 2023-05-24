import products
class Store:
    def __init__(self, products=[]):
        self.products_list = products

    def add_product(self, product):
        self.products_list.append(product)

    def remove_product(self, product):
        self.products_list.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products_list:
            total += product.quantity
        return total

    def get_all_products(self):
        lst_products = []
        for product in self.products_list:
            if product.active:
                lst_products.append(product)
        return lst_products

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if isinstance(product, products.NonStockedProduct):
                total_price += product.buy(quantity)
            elif isinstance(product, products.LimitedProduct):
                if quantity > 1:
                    return f"Error! Only 1 is allowed from this product : {product.name}!"
                else:
                    total_price += product.buy(quantity)
                    product.quantity -= quantity
            elif product in self.products_list and product.quantity >= quantity:
                total_price += product.buy(quantity)
                product.quantity -= quantity
            else:
                return "We do not have enough stock of this product"
        return f"Order cost: {total_price} dollars."
