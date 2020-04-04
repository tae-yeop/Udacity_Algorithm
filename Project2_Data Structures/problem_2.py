import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    file_name = []
    current_list = os.listdir(path)
    # print(f'list : {current_list}')
    if len(current_list)==0:
        pass
    else:
        
        for name in current_list:
            # print(f'checking file and dirs : {name}')
            p = path+"\\"+name
            if os.path.isfile(p):
                # print(f'file :{name}')
                if name.endswith(suffix):
                    file_name.append(name)
                else:
                    continue
            elif os.path.isdir(p):
                # print(f'dir :{name}')
                file_name.extend(find_files(suffix, path+"\\"+name))
    # print('back')
    return file_name


# Test case 1
print(find_files(".c", os.getcwd()+"\\"+"testdir")) # ['a.c', 'b.c', 'a.c', 't1.c']

# Test case 2
print(find_files(".h", os.getcwd()+"\\"+"testdir")) # ['a.h', 'b.h', 'a.h', 't1.h']

# Test case 3
print(find_files("", os.getcwd()+"\\"+"testdir")) # ['a.c', 'a.h', '.gitkeep', 'b.c', 'b.h', '.gitkeep', 'a.c', 'a.h', 't1.c', 't1.h']

# Test case 4
print(find_files(".udacity", os.getcwd()+"\\"+"testdir")) # []