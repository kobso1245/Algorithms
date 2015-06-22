def bin_search(arr ,number):
    left = 0
    right = len(arr) - 1
    curr = left + (right - left)//2

    while left < right:
        if arr[curr + 1]**2 >= number and arr[curr - 1]**2 <= number:
            return arr[curr]

        if arr[curr]**2 < number:
            left = curr + 1

        if arr[curr]**2 > number:
            right = curr - 1

        curr = left + (right - left)//2


def generate_range(number):
    arr = [x for x in range(number)]

    return bin_search(arr, number)

def square_root(number):
    max_item = generate_range(number)
    left = max_item - 1
    right = max_item + 1
    arr = []
    curr = left
    while curr <= right:
        arr.append(curr)
        curr += 0.00001

    return bin_search(arr, number)

print(square_root(10000000))

