class PhoneBook:
    def __init__(self):
        self.book = {}

    def insert(self, number, name):
        self.book[name] = number

    def lookup(self, name):
        if name in self.book:
            return self.book[name]
        else:
            return 'NOT FOUND!'

    def remove(self, name):
        if name in self.book:
            del self.book[name]

    def list(self):
        sorted_names = sorted(self.book.keys())
        for name in sorted_names:
            print("{} {}".format(name, self.book[name]))

def main():
    book = PhoneBook()
    inp = int(input())

    for i in range(inp):
        row = input().split(' ')
        if row[0] == 'insert':
            book.insert(row[1], row[2])
        elif row[0] == 'list':
            book.list()
        elif row[0] == 'lookup':
            print(book.lookup(row[1]))
        elif row[0] == 'remove':
            book.remove(row[1])

main()

