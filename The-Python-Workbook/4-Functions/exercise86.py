""" In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled. Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare as its only result. Write a main program that demonstrates the function.
Hint: Taxi fares change over time. Use constants to represent the base fare and the variable portion of the fare so that the program can be updated easily when the rates increase.
 """

BASE = 4.00
PLUS = 0.25
TRAVELLED = 0.14

def distance(km):

    space = float(km // TRAVELLED)
    total = float(BASE + space * PLUS)
    return total

def main():

    km = float(input("Enter the distance traveled in km: "))
    print('The cost of the trip is:', distance(km))

if __name__ == "__main__":
    main()
