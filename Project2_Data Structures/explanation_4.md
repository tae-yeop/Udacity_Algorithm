The `is_user_in_group` function will takes an user and group and check whether the user is in the group.
The `group` agument is kind of root trie node in the trie data structure. We can get all of its sub groups of the group with `.get_groups()` and all of current group's user list with `.get_users()`.

```python
group_list = group.get_groups()
user_list = group.get_users()
```

First It will check the argument `user` in the current `user_list`. If it is not in thre `user_list` then check for its sub groups. 

We can call the `is_user_in_group` function in a recursion fashion with passing the `group` agument with its `sub_group`.
```python
if user in user_list:
    return True
else:
    for sub_group in group_list:
        return is_user_in_group(user, sub_group)
return False
```

Since this algorithm is like DFS serach in tree data structure, the time complexity will be `O(n)` for the worst case where we need to check out all of the `user_list` in every `group_list`. We use `group_list` and `user_list` local variables to solve this problem. Since `user_list` is just string, it takes `O(1)` space complextiy, but `group_list` depends on the how many total user `group` have. So it takes `O(n)` space complextiy.