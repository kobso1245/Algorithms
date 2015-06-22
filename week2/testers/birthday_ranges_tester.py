from ../birthday_ranges.py import birthdays_count
from random import randrange
from sys import maxsize

def test_random_ranges():
    for i in range(randrange(40,10000)):
        length_of_birthdays_array = randrange(0, 10000000)
        birthdays = []
        for i in range(length_of_birthdays_array):
            birthdays.append(randrange(0, 365))

        tuples = []
        length_of_tuples = randrange(0, 100000)
        for i in range(length_of_tuples):
            tuples.append((randrange(0, 365), randrange(0, 365)))


