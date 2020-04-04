`LRU_Chace` object will be initilized with `capacity`, So it has `self.capacity` attribute. `self.cache` is a dict and it stores the key and value. `self.sequence` kees track of the seqeunce when the keys are used. `self.cache_count` is for the current number of elements stored in the `self.chace`.

```python
class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = dict()
        self.sequence = []
        self.capacity = capacity
        self.cache_count = 0

```

`set` function takes `key` and `value`. If the key is already in the `self.cache`, then we have collision situation and we overwrite the old value with new passed value. Since collision can be considered as `use operation`, we need to modify the key sequence.

The last element in the `self.sequence` list are used as most recently used element and the first one would be least recently used one.

We remove the `key` from the `self.sequence` and move to the last poisition. Because the remove function finds the position of the `key`, so it needs a iteration. So time complexity will be `O(n)`.

```python
if self.cache.get(key) != None: 
    self.cache[key] = value
    self.sequence.remove(key)
    self.sequence.append(key)
    return 

```
If cache is not full, we can add new key-value to the cache. `set` operation is also `user operation`, we need to append the `key` to the `self.sequence`.

```python
if self.cache_count < self.capacity: 
    self.cache_count += 1
    self.cache[key] = value
    self.sequence.append(key)
```

If cache is in full capacity, we need to pop the least recentyl used data. we pop the first element in `self.seqeunce` which is the key of the least recently used one. Then we can delete the data with this key in the `self.cache`.  Then we can assign new data and add the new key to the `self.sequence`.

```python
else:
    pop_key = self.sequence.pop(0)
    self.cache.pop(pop_key)
    self.cache[key] = value
    self.sequence.append(key)
```

`get` function check the data with the key is in the `self.cache`. If it isn't there, we return -1. If data exists, then we get the value of the key. Again this is `use operation`, we can consider this as most recently using this data. So we remove the key and append it as the last element of the `self.sequence`.

```python
def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent. 
        """
        if self.cache.get(key) == None:
            return -1
        else:
            value = self.cache[key]
            self.sequence.remove(key)
            self.sequence.append(key)
            return value
```

Since any local variables in functions are not added based on the input parameter, space complexity will be `O(1)`.