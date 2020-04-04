The binary search approach can be used to solve this problem. The sqrt function takes a number that are needed to find floored squared root. With this number, we can get the search space which consists of smaller numbers than this parameter.
```python
search_space = list(range(number+1))
```

The search space is sorted array inherently, So binary search algorithm can be easily applied to solve this problem.

In this problem, we want floored squared root. which means that In some cases, we can't get the exact integer number but instead got numbers with some deciaml places like `5.1961` for `27`.

The algorithm runs when the first index is less or equal than the last index. We need to include equality for the specil case such as `0 == sqrt(0)`. First, we calculate the mid index.
```python
while first_idx <= last_idx:
    mid_idx = (first_idx + last_idx)//2
    
```
With mid index value, we can check the the target number is equal or larger than the square of the element of middle index and less than the `(element+1)**2.`. With this inequality, we can handle the case where squeare of the elements in the search space is not exact integers. So when the true squared root has decimal points number, it will satisfy this inequaility, and we can ignore the decimal points part.
```python
if (search_space[mid_idx] ** 2) <= number < ((search_space[mid_idx]+1) ** 2):
    return search_space[mid_idx]
```
For example, If we try to find `sqrt(27)`, then the search space is [0,1,2.., 27] . The exact answer is `5.196` and Its sqaure(`27`) is in-between 25(=5^2) and 36(=6^2). Therefore during binary search, if the inequalities satistied then, we can gaurantee that the number are floored square root.

If the target number is less than the the square of the element at a step, It means that we need to limit our search space to [first index, mid index] 
```python
elif number < (search_space[mid_idx] **2 ):
        last_idx = mid_idx
```

Lastly, If the target number is larger than the square of the current element + 1 at a step, we discard the left half of the search space to limit the search space.
```python
else:
    first_idx = mid_idx+1
```

Since we are using binary search, the time coplexity is `O(log(n))`. we initialize the `search_space` in the beggining with the length of `number+1`. So the space complexity will be `O(number)`. 


