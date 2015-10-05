from operator import itemgetter


def lookup_names(phone_book, numbers):
    names = []
    phone_book.sort(key=itemgetter(1))
    for number in numbers:
        name = find_number(phone_book, number)
        names.append(name)

    return names


def find_number(phone_book, number):
    left = 0
    right = len(phone_book) - 1
    curr = left + (right - left) // 2

    while left <= right:
        if phone_book[curr][1] == number:
            return phone_book[curr][0]
        if phone_book[curr][1] > number:
            right = curr - 1

        if phone_book[curr][1] < number:
            left = curr + 1

        curr = left + (right - left) // 2
    return "Not found!"


def main():
    first_line = input().split(' ')
    names = int(first_line[0])
    queries = int(first_line[1])
    phone_book = []

    for i in range(names):
        name = input().split(' ')
        phone_book.append((name[1], int(name[0])))

    result = []
    numbers = []
    for i in range(queries):
        number = int(input())
        numbers.append(number)
    result = lookup_names(phone_book, numbers)
    for res in result:
        print(res)

if __name__ == '__main__':
    main()
