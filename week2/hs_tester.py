from random import randrange
from heap_sort import heap_sort

def tester():
    fle = open("test_results", 'w')
    for i in range(20):
        testing_lst = [randrange(1, (100) - 1) for x in range(randrange(1, 200000))]
        res = heap_sort(testing_lst)
        other_res = sorted(testing_lst)
        if res != other_res:
            #fle.write(str(testing_lst))
            #fle.write('\n')
            print(testing_lst)


        fle.close()
tester()
