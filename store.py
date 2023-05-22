class Store():
    def __init__(self, products_store = []):
        self.products_store = products_store

    def add_product(self, product):
        self.products_store.append(product)

    def remove_product(self, product):
        self.products_store.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products_store:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        active_prodcuts = []
        for product in self.products_store:
            if product.is_active():
                active_prodcuts.append(product)
        return active_prodcuts

    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products_store and product.quantity >= quantity:
                total_price += product.price * quantity
                product.quantity -= quantity
            else:
                print("We do not have enough stock of this product")
        return total_price
