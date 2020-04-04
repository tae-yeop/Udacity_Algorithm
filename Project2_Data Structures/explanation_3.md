To compress the data into encoded data, We need a huffman tree for the data. We can implement the huffman tree with binary tree that each node must have left and right child except the leaf node.

The leaf nodes will have the character data and these are the only node whose children are empty.
Therefore node need to have `self.char` attribute to store the character data.

Also to construct the tree, we need to merge two nodes into one intermediate node. This node will have `self.count` attribute to indicate the total frequency of children's character data.

```python
class Node():
    def __init__(self, char, count=0):
    self.char = char
    self.count = count
    self.left_child = None
    self.right_child = None

```
`huffman_encoding` function takes the data and return the huffman tree and encoded data. This function proceed as follows.

```python
def huffman_encoding(data):
    """
    Args:
        data : string
    Returns
        encoded_data : string
        tree : list of Nodes
    """
    counter = get_frequencies(data)
    nodeslist = makeNode(counter)
    tree = huffman_tree(nodeslist)
    
    encoded_data = ""
    for char in data:
        
        code = tree_traverse(char, tree)
        encoded_data += code
    return encoded_data, tree
```

First, it calculate the frequencies of each character and then pass it to `makeNode` function.
dictionary is used for this function and it stores the character as key and frequency as value. Since it iterates through entire sentecnt, it will takes `O(n)` where n is the number of each character in `data` string.

```python
def get_frequencies(sentence):
    """
    Take a string and determine the relevant frequencies of the characters.

    Args:
        sentence : (string)
    Returns:
        counter : (dict)
    """
    counter = dict()
    for ch in sentence:
        if counter.setdefault(ch, 0) >= 0:
            counter[ch] += 1
    
    return counter
```
`makeNode` function will takes this counter data and convert it into list of `Node` object. It also takes `O(m)` where m is the number of keys in the `counter`.

```python
def makeNode(counter):
    """
    Construct the list of Nodes with counter dictionary

    Args:
        counter (dict)
    Returns:
        nodelist (list) : list of Nodes
    """
    nodelist = list()

    for k, v in counter.items():
        nodelist.append(Node(k, v))
    return nodelist
```

With this list, `huffman_tree` function construct the tree. It will pop 2 `Node` objects whose count(frequency) is the smallest in the list. And then these nodes are merged into the intermediate node. The intermediate node will have these two nodes as children. Then the intermediate node will put into the list. While repeating this process, if the list has only one `Node` object, that is when we have the root node of the tree.

```python
def huffman_tree(nodelist):
    """
    Construct huffman tree.
    """
    while True:
   
        if len(nodelist)==1:
            return nodelist[0]

        _, idx_for_min = min((node.count, idx) for (idx, node) in enumerate(nodelist))
        node_1 = nodelist.pop(idx_for_min)

        _, idx_for_min = min((node.count, idx) for (idx, node) in enumerate(nodelist))
        node_2 = nodelist.pop(idx_for_min)

        new_node = merge(node_1, node_2)
        # print(new_node)
        nodelist.append(new_node)
        
    return nodelist[0]
```

Even though we pop 2 nodes, since we put the intermeidate node everytime, the input size for the algrotihm reduces only 1. Therefore The time complexcity will be `O(m+ (m-1) + (m-2) + ... + 1)` = `O(m^2)`. 

After constructing this tree, we can encode the origianl data into encoded data. It iterates through the original data and exectue `tree_traverse` function.

```python
encoded_data = ""
    for char in data:
        code = tree_traverse(char, tree)
        encoded_data += code
```

`tree_travese` function is basically DFS algoritm and traverse the huffam tree while writting the code. If we move down to left child, we add `0` to the code and if we move down to the right child, we add `1`.

DFS algorithm takes `O(m)` when it is the worst case, and we invoke this traverse for every character in original sentence, So the time complexity for encoding is `O(nm)`. 

Because all of additioanl data structure are just list or dictionary of size of `n` or `m`, the space complexity will be linear(`O(n + m)`).

Lastly, `huffman_decoding` function will reconstruct the original data with the tree. The `encoded_data` is basically kind of instruction telling where to go to the leaf node. If the `code` is `0`, then we move to the left child and if it is `1`, then we move to the right child untill we hit the leaf node.
```python
def huffman_decoding(encoded_data,tree):
    
    pointer = tree
    word = ""
    for code in encoded_data:
        
        if code == '0':
            pointer = pointer.left_child
        else: # code == 1
            pointer = pointer.right_child
        
        # If hit the leaf node
        if pointer.left_child == None and pointer.right_child == None:
            word += pointer.char
            pointer = tree
            continue

    return word
```
In worst case, we will move to the longest path which is the height of the tree and we repeat this traverse for every single code, The time complexity will be `O(l*log(m))` where l is the length of encoded data and m is ther number of unique characters.



