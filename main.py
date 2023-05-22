import store
import products

def start(store_obj):
    while True:
        print("---------- Store Menu ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            all_products = store_obj.get_all_products()
            print("Products in store:")
            for product in all_products:
                print(f"{product.name} - Price: ${product.price} - Quantity: {product.quantity}")

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            try:
                product_num = int(input("Enter the #num of the product: "))
                quantity = int(input("Enter the quantity: "))
                product = None
                for p in store_obj.get_all_products():
                    if p.name == store_obj.get_all_products()[product_num - 1].name:
                        product = p
                        break
                if product is None:
                    print("Product not found in store.")
                else:
                    shopping_list.append((product, quantity))
                    continue_shopping = input("Do you want to add more products to the shopping list? (yes/no): ")
                    while continue_shopping.lower() == "yes":
                        product_num = int(input("Enter the #num of the product: "))
                        quantity = int(input("Enter the quantity: "))
                        product = None
                        for p in store_obj.get_all_products():
                            if p.name == store_obj.get_all_products()[product_num - 1].name:
                                product = p
                                break
                        if product is None:
                            print("Product not found in store.")
                        else:
                            shopping_list.append((product, quantity))
                            continue_shopping = input("Do you want to add more products to the shopping list? (yes/no): ")
                total_price = store_obj.order(shopping_list)
                print(f"Order cost: {total_price} dollars.")
            except IndexError as e:
                print("Wrong number")

        elif choice == "4":
            print("Thank you for using the store interface. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
