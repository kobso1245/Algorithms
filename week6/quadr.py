def checker(first, second, third, fourth):
    arr = {}
    cnt = 0
    for elem in first:
        for elem2 in second:
            curr = elem + elem2
            if curr in arr:
                arr[curr] += 1
            else:
                arr[curr] = 1

    for elem3 in third:
        for elem4 in fourth:
            curr = elem3 + elem4
            if -curr in arr:
                cnt += arr[-curr]

    return cnt



def test():
    cnt = input()
    inp = input().split(' ')
    first = [int(x) for x in inp]
    inp = input().split(' ')
    second = [int(x) for x in inp]
    inp = input().split(' ')
    third = [int(x) for x in inp]
    inp = input().split(' ')
    fourth = [int(x) for x in inp]

    print(checker(first, second, third, fourth))


test()

