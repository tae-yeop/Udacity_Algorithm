def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = 9999
    max = -9999
    for i in ints:
        if i > max:
            max = i
        if i < min:
            min = i
            
    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


l = [i for i in range(-10, 10)]  # a list containing -10 - 9
random.shuffle(l)
print ("Pass" if ((-10, 9) == get_min_max(l)) else "Fail")

l = [0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")