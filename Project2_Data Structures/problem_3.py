import sys

class Node():
    def __init__(self, char, count=0):
        self.char = char
        self.count = count
        self.left_child = None
        self.right_child = None
        
    def set_left_child(self, left_child):
        self.left_child = left_child
        
    def set_right_child(self, right_child):
        self.right_child = right_child
        
    def __repr__(self):
        left_char = None if self.left_child is None else self.left_child.char
        right_char = None if self.right_child is None else self.right_child.char
        return f'[character : {self.char}, count : {self.count}, left : {left_char}, right:{right_char}]'
    

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

def merge(left_child, right_child):
    """
    Merge two nodes and link to the new parent node.

    """
    new_node = Node(char=None, count = left_child.count + right_child.count)
    new_node.set_left_child(left_child)
    new_node.set_right_child(right_child)
    
    return new_node

def huffman_tree(nodelist):
    """
    Construct huffman tree.
    """
    # print(nodelist)
    
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
        # encoded_data += "/"
    return encoded_data, tree

def tree_traverse(char, node):
    """
    Traverse the huffman tree and convert the character into the huffman code.
    """
    code = ""
    visit_oder = [node.char]
    stack = [node]
    while node:
        # print(node)
        if node.char == char:
            # print(code)
            return code
        if node.left_child is not None and node.left_child not in visit_oder:
            stack.append(node.left_child)
            node = node.left_child
            visit_oder.append(node)
            code += "0"
        elif node.right_child is not None and node.right_child not in visit_oder:
            stack.append(node.right_child)
            node = node.right_child
            visit_oder.append(node)
            code += "1"
        else:
            stack.pop()
            code = code[:-1]
            if len(stack) > 0:
                node = stack[-1]
            else:
                node = None


def huffman_decoding(encoded_data,tree):
    
    pointer = tree
    word = ""
    for code in encoded_data:
        # print(f'code:{code} pointer: {pointer}')
        
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
            

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
