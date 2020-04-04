class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = dict()
        self.sequence = []
        self.capacity = capacity
        self.cache_count = 0
        
    def __repr__(self):
        return f'cache : {self.cache}, key_sequence :{self.sequence}'

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
        
    
    def set(self, key, value):
        """
        Set the value if the key is not present in the cache. 
        If the cache is at capacity remove the oldest item. 
        """
        if key == None:
            print('Not valid key')
            return 
        # key collision : overwrite with new value.
        if self.cache.get(key) != None: 
            self.cache[key] = value
            self.sequence.remove(key)
            self.sequence.append(key)
            return 
        
        # Not full capacity : Add the new key-value
        if self.cache_count < self.capacity: 
            self.cache_count += 1
            self.cache[key] = value
            self.sequence.append(key)
        # full capcity : pop the least recently used data.
        else:
            pop_key = self.sequence.pop(0)
            self.cache.pop(pop_key)
            self.cache[key] = value
            self.sequence.append(key)



# Test Case 1 
print('Test case 2')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))      

# Test Case 2
print('Test case 2')
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(2, 100)

print(our_cache.get(2)) # returns 100

our_cache.set(4, 4)
# returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(our_cache.get(1)) 


# Test Case 3
print('Test case 3')
our_cache = LRU_Cache(3)

our_cache.set(None, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
# returns -1 because the cache reached it's capacity and 2 was the least recently used entry
print(our_cache.get(2)) 
