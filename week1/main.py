"""
Main controller of the application
"""

'''from welcome import show_welcome
from sales_register import register_sale
from calculations import calculate_sales
from summary_report import print_summary
from control import continue_register'''

def show_welcome():
    print('')
    print('')
    print('='*84) 
    print('-'*24,'WELCOME TO THE DAILY SALES SYSTEM ','-'*24)
    print('='*84)
    print('')
    print('')

def register_sale():

    product = validate_string("Enter product name: ")
    price = validate_float("Enter unit price: ")
    quantity = validate_integer("Enter quantity sold: ")

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity
    }

    return sale

def validate_string(message):

    valid = True
    result = ""

    while valid:

        value = input(message)

        if value.replace(" ", "").isalpha():
            result = value
            valid = False
        else:
            print("Invalid input. Only text values are allowed.")

    return result


def validate_float(message):

    valid = True
    result = 0.0

    while valid:

        value = input(message)

        try:
            result = float(value)
            valid = False
        except ValueError:
            print("Invalid input. Please enter a decimal number.")

    return result


def validate_integer(message):

    valid = True
    result = 0

    while valid:

        value = input(message)

        try:
            result = int(value)
            valid = False
        except ValueError:
            print("Invalid input. Please enter an integer number.")

    return result

def calculate_sales(sales_list):

    product_totals = {}
    total_income = 0

    for sale in sales_list:

        product = sale["product"]
        price = sale["price"]
        quantity = sale["quantity"]

        sale_total = price * quantity
        total_income += sale_total

        if product in product_totals:
            product_totals[product] += quantity
        else:
            product_totals[product] = quantity

    return product_totals, total_income

def print_summary(product_totals, total_income):

    print("\nSALES SUMMARY")
    print("-----------------------")

    for product in product_totals:

        print("Product:", product)
        print("Total quantity sold:", product_totals[product])
        

    print("Total income:", total_income)

def continue_register():

    control = True
    result = True

    while control:

        answer = input("Do you want to register another sale? (y/n): ").lower()

        if answer == "y":
            result = True
            control = False

        elif answer == "n":
            result = False
            control = False

        else:
            print("Invalid option. Please enter y or n.")

    return result

def main():

    show_welcome()

    sales_list = []

    continue_program = True

    while continue_program:

        sale = register_sale()

        sales_list.append(sale)

        continue_program = continue_register()

    product_totals, total_income = calculate_sales(sales_list)

    print_summary(product_totals, total_income)


if __name__ == "__main__":
    main()