1. The `birthday_ranges.py` module has `birthday_count(birthdays, ranges)`
   function, which is used to tell exactly how many people have birthdays
   in a specific range
 
   ```python
   from birthday_ranges import birthdays_count
   bir_cnt = birthdays_count([5,6,10,10,12,15],[(1,6),(7,12)])
   print(bir_cnt) #[2, 3]
   ``` 
2. The `birthday_ranges_with_counting.py` module has `bir_range(birthdays, ranges)`
   function, which does the same as the above function BUT does it a lil bit faster

3. The `heap_sort.py` module provides `insert_elem(heap, elem)`, `create_heap(array)`,
   `remove_top(max_heap)` and `heap_sort(array)` functions.
    Implements max_heap
    It works with tuples and with non-indexable data structures
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
