from heapq import heappop, heappush, heappushpop

class Reversed:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if self.value[0] < other.value[0]:
            return True
        else:
            return False

def k_lists(arrs):
    lists = arrs
    for i in range(len(lists)):
        lists[i] = [(x, i, 0) for x in lists[i] if x>=0]

    max_heap = []
    len_heap = 0
    result = []
    for lst in lists:
        len_heap += 1
        heappush(max_heap,Reversed(lst[0]))
    
    while len_heap > 0:
        max_elem = heappop(max_heap)
        len_heap -= 1
        value = max_elem.value[0]
        lst_num = max_elem.value[1]
        pos_in_lst = max_elem.value[2]
        result.append(value)
        if len(lists[lst_num]) - 1 > pos_in_lst:
            heappush(max_heap, Reversed((lists[lst_num][pos_in_lst+1][0], lists[lst_num][pos_in_lst+1][1], pos_in_lst+1)))
            len_heap += 1

    return result

def start():
    inp = int(input())
    arrs = []
    for i in range(inp):
        eles = input().split(' ')
        arrs.append([int(x) for x in eles])

    res = k_lists(arrs)
    nice_res = [str(x) for x in res]
    nicer_res = " ".join(nice_res)
    print(nicer_res)

if __name__ == '__main__':
    start()
