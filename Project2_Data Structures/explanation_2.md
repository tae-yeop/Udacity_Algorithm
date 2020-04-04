We can solve this problem in a recurvise way. `find_files` recursion function takes the suffix and the path. First it gets the list containing the names of the files in the directory.
```python
current_list = os.listdir(path)
    if len(current_list)==0:
        pass
```
If the length of `current_list` is 0, that means there is nothing here in this path, So we can terminate the function here.

If it is not the case, we can inspect the name is ended with the `suffix` we are looking for. First we construct absolute path for that names for file and check it is truly a file. If the name ended with the `suffix` we record it into `file_name` lists.

```python
for name in current_list:
    p = path+"\\"+name
    if os.path.isfile(p):
        
        if name.endswith(suffix):
            file_name.append(name)
        else:
            continue

```

if the `name` is the name of directory instead of file, then we invoke `find_files` function where the `path` parameter is now `path+"\\"+name`. That is, we move down to the sub directory. If there are files we're looking for in the sub directory, `find_files` function will return the 

```python
elif os.path.isdir(p): 
    file_name.extend(find_files(suffix, path+"\\"+name))
```

We can think of the directory structure as a tree, so in worst case, we might move inspect all of the directory and files. Therefore the time complexity will be `O(n)`. Also we use `current_list` as local variables and it depends on how many files and sub-directory in the root directory, So space complexity will be `O(n)`.