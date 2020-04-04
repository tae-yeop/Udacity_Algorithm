If we halve the rotated sorted array, we can always get at least one sorted array.
For example, If we halve `[6, 7, 8, 1, 2, 3, 4]` into `[6,7,8,1]` and `[2,3,4]`. In this case `[2,3,4]` is sorted array. Moreover since the `[6,7,8,1]` is also rotated sorted array, we can get the sorted part of the array by halving it. (`[6,7]` and `[8,1]` ; `[6,7]` is sorted array)

If we apply binary search, we were able to compare the mid point of the array to the target number and then halve the array. Therefore, even if the list is not sorted, we gaurantee that we always get the sorted array by using binary search. 

`search function` is doing binary search. first check the mid point is the target value. If the mid point is indeed the target value, we can return it.

```python
def search(input_list, number, first_search_index, last_search_index):

    first_index = first_search_index
    last_index = last_search_index
        
    mid_index = (first_index+last_index) // 2
    
    if input_list[mid_index] == number:
        return mid_index
```
If the mid point is not target value, then check whether the left side of the array is sorted or not and the target number is in the left side. If we find that the value is in the left side, we would limit the search space by setting `last index` to `mid_index-1`. 

```python
if check(input_list[first_index: mid_index], number):
    return search(input_list, number, first_index, mid_index-1)
```

If the value is not in the left side, then we check the right side. In the similar way, we can cut down the search space by setting the `first index` to `mid_index+1`.
```python
elif check(input_list[mid_index+1 : last_index+1], number):
    return search(input_list, number, mid_index+1, last_index)
```
For example, let's say we are going to check the number `2` is in the `[6, 7, 8, 1, 2, 3, 4]`. The mid point value is `1` (`1`!=`2`), so we need to check the `[6,7,8]` and `[2,3,4]` are sorted and the target value is in that list. 


`check function` get the one part of the list as `input_list` and target number. First check `input_list` is sorted or not. If it is indeed sorted array, then the first element is smaller than the last one. If we get the sorted part, then we can check the target value in that array by following two comparison. 
```python
def check(input_list, number):
    if len(input_list) == 0:
        return False

    if input_list[0] <= input_list[-1]:
        if number >= input_list[0] and number <= input_list[-1]:
            return True
        else:
            return False
```

The `input_list` might not be sorted, which means that it is partially sorted since the original list is rotated sorted array. More precisely, It has increasing part and decreasing part. For example, `[6,7,1,2]` has `[6,7]`(increasing part) and `[1,2]`(decreasing aprt). So in this case, we need to compare the value in the following way for taking the both possible cases. 
```python
else: 
    if number >= input_list[0] or number <= input_list[-1]:
        return True
    else:
        return False
```

Since binary search has `O(log(n))` time complexcity, this algorithm also takes `O(log(n))`. But the size of our alogrithm's local variables are not dependent on the input size, So the space complexity will be `O(1)`.
