import store
import products
import promotions
def start(store_obj):
    multiple_promotion = []
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
            i = 0
            for product in all_products:
                i += 1
                if product.promotion is not None:
                    if isinstance(product, products.NonStockedProduct):
                        print(f"{i}. {product.name}, Price: {product.price} $, Quantity: Unlimited, Promotion: {product.promotion.name}")
                    elif isinstance(product, products.LimitedProduct):
                        print(f"{i}. {product.name}, Price: {product.price} $, Limited to {product.maximum} per order!, Promotion: {product.promotion.name}")
                    else:
                        print(f"{i}. {product.show()}, Promotion: {product.promotion.name}")
                elif product.promotion is None and len(product.multiple_promotion) == 0:
                    if isinstance(product, products.NonStockedProduct):
                        print(f"{i}. {product.name}, Price: {product.price} $, Quantity: Unlimited, Promotion: None")
                    elif isinstance(product, products.LimitedProduct):
                        print(f"{i}. {product.name}, Price: {product.price} $, Limited to {product.maximum} per order!, Promotion: None")
                    else:
                        print(f"{i}. {product.show()}, Promotion: None")
                elif len(product.multiple_promotion) > 1 and isinstance(product, products.NonStockedProduct):
                    for promotion in product.multiple_promotion:
                        multiple_promotion.append(promotion.name)
                    print(f"{i}. {product.name}, Price: {product.price} $, Quantity: Unlimited, Promotion: {multiple_promotion}")
                elif isinstance(product, products.LimitedProduct) and len(product.multiple_promotion) > 1:
                    for promotion in product.multiple_promotion:
                        multiple_promotion.append(promotion.name)
                    print(f"{i}. {product.name}, Price: {product.price} $, Limited to {product.maximum} per order!, Promotion: {multiple_promotion}")
                elif len(product.multiple_promotion) > 1:
                    for promotion in product.multiple_promotion:
                        multiple_promotion.append(promotion.name)
                    print(f"{i}. {product.name}, Price: {product.price} $, Quantity: {product.quantity}, Promotion: {multiple_promotion}")

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
                print(store_obj.order(shopping_list))
            except IndexError as e:
                print(f"Wrong number choose between (1 - {len(store_obj.get_all_products())})")
        elif choice == "4":
            print("Thank you for using the store interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    product_list[0].set_promotion(second_half_price)
    product_list[1].multiple_promotions([third_one_free, thirty_percent])
    product_list[2].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()