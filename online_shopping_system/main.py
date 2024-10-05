from products import Product
from shopping_cart import ShoppingCart

# Creating Product objects
product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 500, 10)
product3 = Product("Headphones", 100, 20)

# Creating ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding items to cart1
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product2, 2)
cart1.display_cart()
print(f"Total amount due: ${cart1.calculate_total()}")

# Adding and removing items in cart2
cart2.add_to_cart(product3, 5)
cart2.add_to_cart(product2, 1)
cart2.remove_from_cart(product3)
cart2.display_cart()
print(f"Total amount due: ${cart2.calculate_total()}")

# Displaying cart1 contents and total
print("\nCart 1:")
cart1.display_cart()
print(f"Total amount due: ${cart1.calculate_total()}")

# Displaying cart2 contents and total
print("\nCart 2:")
cart2.display_cart()
print(f"Total amount due: ${cart2.calculate_total()}")
