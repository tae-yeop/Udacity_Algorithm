## 1. Union

First the union method takes two lists as argument and get the each head. `union` local variable is a set and it will be used to record the elements of two lists.

We can use two while-loop for each list and collect the element into the `union`. Since `union` is set, It can handle duplicates.

```python
while head_1:
    union.add(head_1.value)
    head_1 = head_1.next
while head_2:
    union.add(head_2.value)
    head_2 = head_2.next
```
After constructing `union`, we can convert it into list with single for-loop by appending each element.

```python
for i in union:
    union_ll.append(i)
```
Since this algorithm uses 3 traverse, time complexity will be `O(n) + O(m) + O(n+m)` where n is the number of elements in first set and m is the number of elements in second set. We can simplify the time efficiency as `O(n)` if n>m. We use additional `LinkedList` and `set` data structure, So It will be linear space complexity, `O(2*(n+m))`.


## 2. Intersection

Similar to the union method, It uses 3 traverses and extra data structure for recording elements. But this time, a dictionary is used instead of a set.

Durting first iteration, `value_dict` record the elements in the first while setting the value as 0. This means that if the a key has the value 0, then that key was in the first set.

```python
while head_1:
    value_dict.setdefault(head_1.value, 0)
    head_1 = head_1.next
```

Next, we iterats through the second set and check the element is already in the the dictionary, which means that it is in the first set in turn. 
If it turns out that the element is already in `value_dict`, we assign the value with `2`, which means that the element is in both sets.

```python
while head_2:
    if value_dict.setdefault(head_2.value, 1) == 0:
        value_dict[head_2.value] = 2
    head_2 = head_2.next
```
To avoid the key error where the key is not in the dictionary, we need to use `.setdefault(head_2.value, 1)`. So the key with value 1 will be the unique element of the second set.

After constructing the dictionary, we can convert it into a linked list.
```python
for k, v in value_dict.items():
    if v == 2:
        intersection_ll.append(k)
```
Since this algorithm uses 3 traverse, time complexity will be `O(n) + O(m) + O(n+m)` where n is the number of elements in first set and m is the number of elements in second set. We can simplify the time efficiency as `O(n)` if n>m. We use one more `Linked list` and `dictionary`, So It will be linear space complexity, `O(2*(n+m))`.