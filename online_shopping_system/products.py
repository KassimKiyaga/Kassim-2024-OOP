class Product:
    def __init__(self, product_name, price, quantity_in_stock):

#      Initializes a new product with a name, price, and quantity in stock.
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        
#        Displays the product details.
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")


