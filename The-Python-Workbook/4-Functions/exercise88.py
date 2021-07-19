""" Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.
Hint: The median value is the middle of the three values when they are sorted into ascending order. It can be found using if statements, or with a little bit of mathematical creativity.
 """


def median(a, b, c):

    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c

    return median


def main():

    a = int(input("Insert first number item: "))
    b = int(input("Insert second number item: "))
    c = int(input("Insert third number item: "))

    print('The median number is', median(a, b, c))


if __name__ == "__main__":
    main()
