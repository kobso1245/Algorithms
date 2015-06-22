1. The `birthday_ranges.py` module has `birthday_count(birthdays, ranges)`
   function, which is used to tell exactly how many people have birthdays
   in a specific range
 
   ```python
   from birthday_ranges import birthdays_count
   bir_cnt = birthdays_count([5,6,10,10,12,15],[(1,6),(7,12)])
   print(bir_cnt) #[2, 3]
   ``` 
2. The `birthday_ranges_with_counting` module has `bir_range(birthdays, ranges)`
   function, which does the same as the above function BUT does it a lil bit faster 
