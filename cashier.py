#  Print list of available groceries to select from
print()
print("List of items currently in stock: ")
print()
print("Biscuits, Chicken, Eggs, Fish, Coke, Bread, Apples, Onions, Green Chile:")
print()
#  Supermarket Cashier program
#  Function for products While loop
def enter_products():
    buying_data = {}
    enter_details: bool = True
    while enter_details:
        details = input('Press A to add product and Q to quit: ')
        if details == 'A':
            product = input('Enter product: ')
            try:
                quantity = int(input('Enter quantity: '))
                buying_data.update({product: quantity})
            except ValueError as e:
                print("quantity must be in integer")
        elif details == 'Q':
            enter_details = False
        else:
            print('Please select a correct option')
    return buying_data


#  Subtotal - Get Price function
def get_price(product, quantity):
    price_data = {
        'Biscuits': 3,
        'Chicken': 5,
        'Eggs': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apples': 3,
        'Onions': 3,
        'Green Chile': 5
    }
    subtotal = price_data[product] * quantity
    print(product + ':$' + 
          str(price_data[product]) + 'x' + str(quantity) + 
          '=' + str(subtotal))
    return subtotal


#  Discount  where we check to see if the consumer has a membership and gets a discount for it
#  We will also add a condition that a discount will be given only if the billing amount is greater than $25
#  Membership levels: Gold = 20% off, Silver = 10% off, Bronze = 5% off
#  get_discount function
def get_discount(bill_amount, membership):
    discount = 0
    if bill_amount >= 25:
        if membership == 'Gold':
            bill_amount = bill_amount * 0.80
            discount = 20
        elif membership == 'Silver':
            bill_amount = bill_amount * 0.90
            discount = 10
        elif membership == 'Bronze':
            bill_amount = bill_amount * 0.95
            discount = 5
        print(str(discount) + "% off for " + membership +
              " " + "membership on total amount: $" + str(bill_amount))
    else:
        print("No discount on amount less than $25")
    return bill_amount


# Final Bill - This is the final step where we will make the calls to these functions we created and make the bill
# for the products the consumer has purchased
def make_bill(buying_data, membership):
    bill_amount = 0
    for key, value in buying_data.items():
        bill_amount += get_price(key, value)
    bill_amount = get_discount(bill_amount, membership)
    print("The discounted amount is $" + str(bill_amount))


#  Final piece to make the code run
buying_data = enter_products()
membership = input("Enter customer membership: ")
make_bill(buying_data, membership)
