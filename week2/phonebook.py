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
    curr = left + (right - left)//2

    while left <= right:
        if phone_book[curr][1] == number:
            return phone_book[curr][0]
        if phone_book[curr][1] > number:
            right = curr - 1

        if phone_book[curr][1] < number:
            left = curr + 1

        curr = left + (right - left)//2
    return "Not found!"


phones = [("Gosho", 1234564),("Pesho",3569080),("Dani",125648),("Koko", 4860780),("Ivo", 87030543),("Coco", 78678030)]
numbs = [4860780,123456,1234564,87030543,125648,3569080,78678030]
print(lookup_names(phones, numbs))
