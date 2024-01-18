class ShoppingCart:

    def user_inputs(self):
        print("Welcome to our shopping cart")
        print("* * * * * * * * * * * * * * * ")

        for product in self.products:
            self.quantity[product] = self.valid_input(f"How many \"{product}\"s do you want? ", "Please enter a valid quantity.")
            print("")
            self.gift_wrap[product] = self.response(f"Do you need this \"{product}\" wrapped as a gift? type 'yes' or 'no' ")
            print("")

    def __init__(self):
        self.products = {
            "product_A": 20,
            "product_B": 40,
            "product_C": 50
        }
        self.quantity = {}
        self.gift_wrap = {}
        self.discount = {
            "FLAT10": 200,
            "BULK5": 10,
            "BULK10": 20,
            "TIERED50": {'total_quantity': 30, 'single_quantity': 15}
        }
        self.gift_wrap_fee = 1
        self.shipping_fee = 5
        self.units = 10
        self.user_inputs()

    def valid_input(self, message, error_message):
        while True:
            try:
                value = int(input(message))
                if value >= 0:
                    return value
                else:
                    print(error_message)
            except ValueError:
                print(error_message)

    def response(self, message):
        while True:
            user_input = input(message).lower()
            if user_input in ['yes', 'no']:
                return user_input == 'yes'
            else:
                print("Enter 'yes' or 'no'.")

    def discount_calculations(self):
        cart_total = sum(self.quantity[product] * self.products[product] for product in self.products)
        discounts = []

        if cart_total > self.discount['FLAT10']:
            discounts.append(('FLAT10', 10))

        for product, quantity in self.quantity.items():
            if quantity > 10:
                discount = 0.05 * self.products[product] * quantity
                discounts.append(('BULK5', discount))

        if sum(self.quantity.values()) > self.discount['BULK10']:
            discount = 0.1 * cart_total
            discounts.append(('BULK10', discount))

        if sum(self.quantity.values()) > self.discount['TIERED50']['total_quantity']:
            for product, quantity in self.quantity.items():
                if quantity > self.discount['TIERED50']['single_quantity']:
                    discount = 0.5 * self.products[product] * (quantity - self.discount['TIERED50']['single_quantity'])
                    discounts.append(('TIERED50', discount))

        if discounts:
            max_discount_rule, max_discount_amount = max(discounts, key=lambda x: x[1])
            return max_discount_rule, round(max_discount_amount, 2)
        else:
            return None, 0

    def calculate_total(self):
       
        subtotal = sum(self.quantity[product] * self.products[product] for product in self.products)
        
        discount_name, discount_amount = self.discount_calculations()
        gift_wrap_fee =sum(self.gift_wrap_fee * self.quantity [product] for product in self.products if
                            self.gift_wrap[product])
        
        shipping_fee =(sum(self.quantity.values()) - 1)  // self.units *self.shipping_fee + self.shipping_fee

        total =subtotal - discount_amount + gift_wrap_fee + shipping_fee
        
        
        return subtotal, discount_name, discount_amount, gift_wrap_fee, shipping_fee, total

    def display_receipt(self):
        print("\nReceipt:")
        print("*___________*")

        for product in self.products:
            print(f"{product}: Quantity - {self.quantity[product]}, Total - ${self.quantity[product] * self.products[product]}")
        subtotal, discount_name, discount_amount, gift_wrap_fee, shipping_fee, total = self.calculate_total()
       
        print(f"\nSubtotal: ${subtotal}")
        print(f"Discount Applied: {discount_name} - ${discount_amount}")
        print(f"Gift Wrap Fee: ${gift_wrap_fee}")
        print(f"Shipping Fee: ${shipping_fee}")
        print(f"\nTotal: ${total}")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.display_receipt()
