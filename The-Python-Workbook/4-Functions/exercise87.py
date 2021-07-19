""" An online retailer provides express shipping for many of its items at a rate of $10.95 for the first item in an order, and $2.95 for each subsequent item in the same order. Write a function that takes the number of items in the order as its only parameter. Return the shipping charge for the order as the function’s result. Include a main program that reads the number of items purchased from the user and displays the shipping charge.
 """

FIRST = 10.95
SUBSEQUENT = 2.95


def item(number_item):

    number_item_sub = number_item - 1
    subsequent_ship = number_item_sub * SUBSEQUENT
    shipping = FIRST + subsequent_ship
    return shipping


def main():

    number_item = int(input("Insert numbert item: "))
    print('The total amount of the shipment is : ' + '%.2f ' %
          item(number_item), '$')


if __name__ == "__main__":
    main()
