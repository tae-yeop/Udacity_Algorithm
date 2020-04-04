To implement auto-completion, TireNode need to have suffixes function. The suffixies function is implemented in a recursive way with an inner function.

First It check whether its children has each character in the suffix string and move down to the chilren which has the last character of the suffix string. 

```python
def suffixes(self, suffix = ''):
    current_children = self.children
        for char in suffix:
            if char in current_children:
                current_children = current_children[char].children

```
From this children, we can collect the word with recursion and save it into `words` list.
If the we hit the leaf node, then append completed word into the word_list.
```python
if len(children)==0:
    word_list.append(word)
```
If the children is not the leaf node, then we can concatentate the word from the children. We can move down to the its children node with recursion and do the same process. We'll return to the branching point where we call the recursion function after constructing full one word. Then the new word being constructed will starts with another child in the children. Therefore we need to re-initialize word with `""`. 

```python
for child in children:
    word+=child
    recursion(children[child].children, word_list, word)
    word = ""
```
For example, let's say we're finding suffixes of `'ant'` when we have a trie of `["ant", "anthology", "antagonist", "antonym"]`.
't' node has 3 children (`o`, `a`). We concatenate the `'a'` to `word` to construct `"antagonist"`. After adding the word `"antagonist"` into `word_list`, we starts with `'o'` node. 

Since the algorithm takes DFS approach, It will take `O(log n)`.
It could depends on how many its each has children and how many words. Let's say the trie has `x` children for every nodes and total elements of `y`.

The DFS algorithm takes `log_x (y)`. Since `log_x (y) = log_2 (y) / log_2 (x)`, the big order still will be `O(log n)`.