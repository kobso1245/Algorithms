class PhoneBook:

    def __init__(self):
        self.numbers = dict()

    def insert(self, name, number):
        self.numbers[name] = number

    def remove(self, name):
        del self.numbers[name]

    def lookup(self, name):
        if name in self.numbers:
            return self.numbers[name]
        else:
            return 'NOT FOUND'

    def list(self):
        names = sorted(self.numbers.keys())
        for name in names:
            print("{} {}".format(name, self.numbers[name]))


def start():
    book = PhoneBook()
    rows_num = int(input())
    for i in range(rows_num):
        row = input().split(' ')
        if row[0] == 'insert':
            book.insert(row[2], row[1])
        elif row[0] == 'lookup':
            print(book.lookup(row[1]))
        elif row[0] == 'list':
            book.list()
        else:
            book.remove(row[1])
start()
