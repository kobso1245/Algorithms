import random


def linear_search(sorted_array, elem_to_find):
    array_length = len(sorted_array)
    for curr_elem in range(array_length):
        if sorted_array[curr_elem] == elem_to_find:
            return curr_elem

    return -1


def binary_search(sorted_array, elem_to_find):
    left = 0
    right = len(sorted_array) - 1
    curr_elem = left + (right - left) // 2

    while(left <= right):
        if curr_elem > 0 and sorted_array[
                curr_elem] == elem_to_find and sorted_array[curr_elem - 1] < elem_to_find:
            return curr_elem
        if sorted_array[curr_elem] < elem_to_find:
            left = curr_elem + 1
        if sorted_array[curr_elem] >= elem_to_find:
            right = curr_elem - 1

        curr_elem = left + (right - left) // 2
    return -1


def sorted_array_generator():
    random_array_length = random.randrange(100, 50000)
    resulted_arr = []
    for i in range(random_array_length):
        resulted_arr.append(random.randrange(-50000, 50000))
    return sorted(resulted_arr)


def main_testing_function():
    random_elem = random.randrange(100, 50000)
    sorted_array = sorted_array_generator()
    if linear_search(
            sorted_array,
            random_elem) == binary_search(
            sorted_array,
            random_elem):
        return True
    return False


def tester():
    number_of_tests = random.randrange(500, 6000)
    for test in range(number_of_tests):
        if main_testing_function():
            print("Test {} passed!".format(test))

        else:
            print("Test {} failed!".format(test))
            return


tester()
##print(binary_search([1,2,3,5,7,8,12,12,40,60,75], 12))
