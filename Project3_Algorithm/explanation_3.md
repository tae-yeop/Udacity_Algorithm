First the input_list is sorted with merge sort algorithm. With sorted_list, We can pop the largest element one by one and assign the elements alternatingly to two lists(`first` and `second`) until the every elements are pulled off. The two lists are the representation of the first and second number.

```python
sorted_list = mergesort(input_list)
    while len(sorted_list)!=0:

        if len(sorted_list)>0:
            first.append(sorted_list.pop())
            
        if len(sorted_list)>0:
            second.append(sorted_list.pop())
```
Since This is alternatingly assigning the elements, It gaurantee that the number of digits cannot be differ by more than 1.
For example, if the sorted list is `[1,2,3,4,5,6,7]`, `first` list will be `[7,5,3,1]` and `second` list will be `[6,4,2]`.
Also placing the largest number into bigger digit can form maximum number. Therefore sum of the constructed two number are gauranteed to be maximum number.

After constructing each lists, we can convert the list into actual number by multiplying a power of 10 with each element.
```python
for i, power in enumerate(range(first_len-1, -1, -1)):
        first_total += first[i] * (10**power)
        
    for i, power in enumerate(range(second_len-1, -1, -1)):
        second_total += second[i] * (10**power)
```

The total time complexity will be `O(n log(n))`.
- First, the merge sort takes `O(n log(n))`.
- Second, the constructing two lists with single while-loop will take `O(n)`.
- Third, converting to two lists into actual numbers takes `O(n)`.
- Therefore `O(n log(n))` + `O(2n)` = `O(n log(n))`.

The total space complexity will be `O(n)`.
- merge sort takes `O(n)` for `left` and `right`.
- `sorted_list` will hold `O(n)`.
- `first` + `second` will hold `O(n)`.
- Therefore `O(n)` + `O(n)` + `O(n)`  = `O(n)`.