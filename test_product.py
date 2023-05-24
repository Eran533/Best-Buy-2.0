import pytest
import store
import products

def test_create_product():
    name = "Product A"
    price = 10.99
    quantity = 5
    product = products.Product(name, price, quantity)
    assert product.name == name
    assert product.price == price
    assert product.quantity == quantity
    assert product.is_active()

def test_create_product_with_invalid_details():
    with pytest.raises(Exception) as excinfo:
        product1 = products.Product("", 10.99, 5)
    assert str(excinfo.value) == "Sorry, no empty name or numbers below zero"
    with pytest.raises(Exception) as excinfo:
        product2 = products.Product("Product B", -5.99, 3)
    assert str(excinfo.value) == "Sorry, no empty name or numbers below zero"

def test_product_reaches_zero_quantity():
    product_list = [
        products.Product("Product A", price=10.99, quantity=5),
        products.Product("Product B", price=15.99, quantity=0),
        products.Product("Product C", price=20.99, quantity=10)
    ]
    product_b = product_list[1]
    assert not product_b.is_active()

def test_purchase_modifies_quantity():
    product_list = [
        products.Product("Product A", price=10.99, quantity=5),
        products.Product("Product B", price=15.99, quantity=0),
        products.Product("Product C", price=20.99, quantity=10)
    ]
    test_store = store.Store(product_list)
    soping_list = [(product_list[2], 5)]
    test_store.order(soping_list)
    assert product_list[2].quantity == 5

def test_buying_larger_quantity():
    product_list = [
        products.Product("Product A", price=10.99, quantity=5),
        products.Product("Product B", price=15.99, quantity=0),
        products.Product("Product C", price=20.99, quantity=10)
    ]
    test_store = store.Store(product_list)
    soping_list = [(product_list[2], 15)]
    assert test_store.order(soping_list) == f"We do not have enough stock of this product"

pytest.main()