""" The Twelve Days of Christmas is a repetitive song that describes an increasingly long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on the first day. A new gift is added to the collection on each additional day, and then the complete collection is sent. The first three verses of the song are shown below.

Write a program that displays the complete lyrics for The Twelve Days of Christ- mas. Your program should include a function that displays one verse of the song. It will take the verse number as its only parameter. Then your program should call this function 12 times with integers that increase from 1 to 12.
Each item that is sent to the recipient in the song should only appear in your program once, with the possible exception of the partridge. It may appear twice if that helps you handle the difference between “A partridge in a pear tree” in the first verse and “And a partridge in a pear tree” in the subsequent verses. Import your solution to Exercise 89 to help you complete this exercise.

 """
from exercise89 import ordinal


def displayVerse(number):
    print("On the", ordinal(number), "day of Christmas")
    print("my true love sent to me:")
    if number >= 12:
        print("Twelve drummers drumming,")
    if number >= 11:
        print("Eleven pipers piping,")
    if number >= 10:
        print("Ten lords a-leaping,")
    if number >= 9:
        print("Nine ladies dancing,")
    if number >= 8:
        print("Eight maids a-milking,")
    if number >= 7:
        print("Seven swans a-swimming,")
    if number >= 6:
        print("Six geese a-laying,")
    if number >= 5:
        print("Five golden rings,")
    if number >= 4:
        print("Four calling birds,")
    if number >= 3:
        print("Three French hens,")
    if number >= 2:
        print("Two turtle doves,")
    if number == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()
# Display all 12 verses of the song


def main():
    for verse in range(1, 13):
        displayVerse(verse)


main()
