In this problem, We can use simple for-loop and some comparisions that is to check whether the element is 0, 1 or 2. And then we can assign the element into the each list (`zero_array`, `one_array`, `two_array`). 
```python
for value in input_list:
    if value == 0:
        zero_array.append(0)
    elif value == 1:
        one_array.append(1)
    elif value == 2: 
        two_array.append(2)
    else:
        print('The input list has element that is not 0, 1, 2.')
        continue
```
Since the order of the integer always follows as `0, 1, 2` , we can simply concatenate the 3 lists.
```python
return zero_array+one_array+two_array
```

Since the algorithm takes only single traverses with for-loop, the time complexity is `O(n)`. The size of `zero_array`, `one_array`, `two_array` will be dependent on the `input_size`. So space complexity will be `O(n)`.
