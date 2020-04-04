Before implementing actual Router, RouteTrie and RouteTrieNode are needed to be implemented. 
RouteTrieNode has `children` and a `handler` instead of `is_word`. The insert method takes the partial segment of url and uses it as key to children.

```python
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None
    def insert(self, segment):
        # Insert the node as before
        self.children[segment] = RouteTrieNode()
```

Next, RouteTrie is initialized with root node. The root node is RouteTrieNode object and will insert root segment(`/`) with root_handler.
```python
def __init__(self, seg, handler):
        self.root = RouteTrieNode()
        self.root.insert(seg)
        self.root.handler = handler

```
The insert method for RouteTrie takes the list of url segments and handler.
Simple single for-loop is used for this method. If the segment is not in the children, then insert the segment. 
After moving down to the leaf node, we can finally assign the handler for this segments.

Since It has single traverse with dictionary retreiving, It will take `O(n)`. If we add a complety new path to the Trie, then we need space of `O(n)`.
```python
def insert(self, segments, handler):

    current_node = self.root

    for seg in segments:
        if seg not in current_node.children:
            current_node.insert(seg)
        current_node = current_node.children[seg]
    
    current_node.handler = handler

```

`find` method is used for look up function and this returns the assigened handler. Similar to insert method, It has single traverse with dictionary retreiving, It will take `O(n)`. This function doesn't use segement-size dependent variables, So the space complexity will be `O(1)`.
```python
def find(self, segments):
                   
        current_node = self.root

        for seg in segments:
            if seg not in current_node.children:
                return None
            current_node = current_node.children[seg]

        return current_node.handler
```

Router class will be initialized with two parameters(`root_handler`, `not_found_handler`).
The constructor creates a RouteTrie instance with `/` segment and `root_handler`. The router will keep `not_found_handler` with its attribute so that the router is able to return `not_found_handler` when it fails at lookup method.

 ```python
 class Router:
    def __init__(self, root_handler, not_found_handler):


        self.routeTrie = RouteTrie("/", root_handler)
        self.not_found_handler = not_found_handler
```

`split_path` method is needed for breaking down the url path into partial segments. It splits with `.split('/')` and get the list.
The first and last delimiter string is replaced with `''`. For example, `"/home/about/"` will become `['', 'home', 'about', ''].`
In order to handler `router.lookup("/")` case, the first element of the list are assigned to `"/"`.
Moreover the replaced last element in the list is truncated to handler the trailing slashes.
```python
def split_path(self, path):
    segments = path.split('/')
    segments[0] = "/"
    if segments[-1] == "":
        segments = segments[:-1]
    return segments
```

Using this `split_path` method, we can implement `add_handler` and `lookup` method. Both methods are simply delegated to the `RouteTrie` objects's `insert` and `find` methods.