## Block class

The Block object contains its data, hash and timestamp, previous block's hash and pointer. The constructor for block object will initialize these attributes. 

```python
def __init__(self, timestamp="", data="", previous_hash=0):
    if timestamp == "":
        self.timestamp = self.get_utc_time()
    else:
        self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
    self.prev_block = None

```

`calc_hash` method will calculate the hash code based on its data and the time stamp when it is generated. 

```python
def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = (self.data + self.timestamp).encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()
```

## BlockChain

The blockchain will prefer to retreive previous node unlike standarad linked list where it has a refrence to next node instead of previous one. Therefore BlockChain object has `self.tail` to store most recent added node.

`add` method will check the `self.tail` is `None`. If It is `None`, that means the BlockChain is empty and we can assing the block as first one. If this is not the case, then we get the previous recent added block and assign the reference variable `prev_block`.

With this reference variable, we can assign current block's previous hash code and its previous block with this reference variable.

```python
def add(self, block):
    if self.tail is None:
        self.tail = block
        return
    prev_block = self.tail
    block.previous_hash = prev_block.hash
    block.prev_block = prev_block
    self.tail = block
```
Since It directly assign its `previous_hash` and `previous_block` with the `self.tale`, the time and space complexity will be both `O(1)`.