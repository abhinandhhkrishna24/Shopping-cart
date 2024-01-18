# Shopping Cart Program

Welcome to the Shopping Cart program! This program helps you calculate the cost of items in your shopping cart, including discounts, gift wrap fees, and shipping fees.

## Getting Started

Follow these steps to use the program:


### Installation

1. Clone the Repository:

    ```bash
    git clone https://github.com/abhinandhhkrishna24/Shopping-cart.git
    cd Shopping-cart
    ```

2. Run the Program:

    ```bash
    python shopping_cart.py
    ```

3. Enter Product Quantities:

    - For each product, enter the quantity when prompted.
    - Specify if the product needs to be wrapped as a gift by entering 'yes' or 'no'.

4. Review Order Details:

    - The program will display the details of your order, including product quantities, subtotals, and discounts.

5. View Receipt:

    - The program will generate a receipt showing the subtotal, discounts, gift wrap fees, shipping fees, and the total amount.

## Example

Welcome to our shopping cart
* * * * * * * * * * * * * * * 
How many "product_A"s do you want? 50
Do you need this "product_A" wrapped as a gift? type 'yes' or 'no' yes

How many "product_B"s do you want? 35
Do you need this "product_B" wrapped as a gift? type 'yes' or 'no' yes

How many "product_C"s do you want? 60
Do you need this "product_C" wrapped as a gift? type 'yes' or 'no' no

Receipt:
*___________*
product_A: Quantity - 50, Total - $1000
product_B: Quantity - 35, Total - $1400
product_C: Quantity - 60, Total - $3000

Subtotal: $5400
Discount Applied: TIERED50 - $1125.0
Gift Wrap Fee: $85
Shipping Fee: $75

Total: $4435.0
