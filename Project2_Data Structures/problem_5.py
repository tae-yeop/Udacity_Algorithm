import hashlib
import datetime  

class Block:
    def __init__(self, timestamp="", data="", previous_hash=0):
        if timestamp == "":
            self.timestamp = self.get_utc_time()
        else:
            self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev_block = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        # Get hash code based on the data and dates
        hash_str = (self.data + self.timestamp).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def get_utc_time(self):
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
            
    def __repr__(self):
        return f"Block info : data={self.data} , timestamp={self.timestamp}, prev_hash={self.previous_hash}"


class BlockChain:
    def __init__(self):
        self.tail = None
        
    def add(self, block):
        if self.tail is None:
            self.tail = block
            return
        prev_block = self.tail
        block.previous_hash = prev_block.hash
        block.prev_block = prev_block
        self.tail = block
        
    def __repr__(self):
        s = "Printing block chain\n________________\n"
        pointer = self.tail
        while pointer is not None:
            s += "\n".join([str(self.tail)])
            s += "\n___________________\n"
            pointer = pointer.prev_block
        return s



# Test cases 1 - Multiple Blocks

block1 = Block(data="data1")
block2 = Block(data="data2")
block3 = Block(data="data3")
block4 = Block(data="data4")

blockChain = BlockChain()

blockChain.add(block1)
blockChain.add(block2)
blockChain.add(block3)
blockChain.add(block4)
print(blockChain)

# Test cases 2 -Single block
block1 = Block(data="data1")
blockChain = BlockChain()
blockChain.add(block1)
print(blockChain)

# Test cases 3 - Null test
block1 = None
block2 = Block(data="data2")
blockChain = BlockChain()
blockChain.add(block1)
blockChain.add(block2)
print(blockChain)
