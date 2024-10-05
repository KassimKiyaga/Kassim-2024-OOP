class ShoppingCart:
    total_carts = 0  # Class variable to track the total number of shopping carts created

    def __init__(self):
        
        #Initializes a new shopping cart with an empty list of items.
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        
#Adds a product to the cart if the quantity is available.
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Not enough stock for {product.product_name}.")

    def remove_from_cart(self, product):
    
#Removes a product from the cart.
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"Removed {product.product_name} from the cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
    
#Displays all items in the cart.
        if not self.items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for product, quantity in self.items:
                print(f"{product.product_name} - Quantity: {quantity}")

    def calculate_total(self):
        
#Calculates and returns the total price of items in the cart.
    
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

