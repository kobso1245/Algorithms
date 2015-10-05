def count_em_all(lists, cnt):
    arr = {}
    elems = set()

    for i in range(cnt):
        for elem in lists[i]:
            if elem in arr:
                if arr[elem][1] != i:
                    arr[elem] = (arr[elem][0] + 1, i)

                if i == cnt - 1 and arr[elem][0] == cnt:
                    elems.add(elem)
            else:
                arr[elem] = (1, i)

    return elems


def test():
    print(count_em_all([[2, 5, 5, 10, 3, 1], [
          7, 13, 3, 9, 2, 55, 5, 47, 10], [42, 2, 3], [5, 5]], 4))
test()
