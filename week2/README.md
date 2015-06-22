1. The `birthday_ranges.py` module has `birthday_count(birthdays, ranges)`
   function, which is used to tell exactly how many people have birthdays
   in a specific range.
   It returns list of the birthdays count in each range.
 
   ```python
   from birthday_ranges import birthdays_count
   bir_cnt = birthdays_count([5,6,10,10,12,15],[(1,6),(7,12)])
   print(bir_cnt) #[2, 3]
   ``` 
2. The `birthday_ranges_with_counting.py` module has `bir_range(birthdays, ranges)`
   function, which does the same as the above function BUT does it a lil bit faster

3. The `heap_sort.py` module provides `insert_elem(heap, elem)`, `create_heap(array)`,
   `remove_top(max_heap)` and `heap_sort(array)` functions.
    Implements max_heap.
    It works with tuples and with non-indexable data structures.
    ```python
    from heap_sort import heap_sort
    arr = heap_sort([1,3,2,4,5,6,8,0,12,10])
    print(arr) #[0,1,2,3,4,5,6,8,10,12]
    ``` 
    ```python
    from heap_sort import insert_elem
    max_heap = [11,10,8,5,6,2,7,1,4,3]
    insert_elem(max_heap, 13) #[13,11,8,5,10,2,7,1,4,3,6]
    ```
4.  The `klists.py` module provides `k_lists(list_of_lists)` function, which is used if we want     to merge already sorted k number of lists into one sorted lists. This function sorts
    them in ascending order(and needs ascending order lists to run correctly).
    It returns the merged and ordered list.
    The function needs the `insert_elem` and `remove_top` functions from the `heap_sort`
    module.

    ```python
    from heap_sort import insert_elem, remove_top
    from klists import k_lists
    arr = k_lists[(1,3,5,7,9), (2,4,6,8)] #[1,2,3,4,5,6,7,8,9]
    ``` 

5. The `kmin.py` module provides `k_min(array, k)` function, which returns the k-th min 
   element in an array.
   It needs the `remove_top` and `insert_elem` functions from `heap_sort` module in order to 
   run.

   ```python
   from heap_sort import remove_top, insert_elem
   from kmin import k_min
   elem = k_min([1,2,5,3,4,6], 6)
   print(elem) #6
   ```
6. The `phonebook.py` module provides `find_number(phone_book, number)` function that returns
   list of names, associated with this numbers

   ```python
   from operator import itemgetter
   phones = [("Gosho", 1234564),("Pesho",3569080),("Dani",125648),("Koko", 4860780),("Ivo",
   87030543),("Coco", 78678030)]
   numbs = [4860780,123456,1234564,87030543,125648,3569080,78678030]
   print(lookup_names(phones, numbs)) #["Koko", "Not found!", "Gosho","Ivo", "Not found!","Not found!", "Coco"]
   ```

