This problem is to find the minimum and maximum number in an array explicitly. Since It only needs to keep track of the min and max value whenever we inspect the element in the array, We can perform the task by using a single traversal.

Iterating the array, we can check the element is larger than `max` and smaller than `min`. The initial value for `max` is very low number(negative infinity in theory) so that if the element is bigger than this, then we can always keep track of bigger number by the comparison. The `min` case follows the similar logic but vice versa.

Instead of actual number, we can use `math` pacakge for assigning intial min and max
```python
import math

min = math.inf
max = -math.inf
```
Since It has only single loop traverse, the time complexity is `O(n)`. Since it doesn't use additional data structure based on the input size, space complexity will be `O(1)`.