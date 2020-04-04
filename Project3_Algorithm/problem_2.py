def check(input_list, number):
    """
    Check the target value is in the input_list
    Args:
        input_list
        number
    Returns:
        bool: True if the target number is in the list
    """

    if len(input_list) == 0:
        return False
    
    # print(input_list)

    # sorted
    if input_list[0] <= input_list[-1]:
        if number >= input_list[0] and number <= input_list[-1]:
            return True
        else:
            return False
    # unsorted
    else: 
        if number >= input_list[0] or number <= input_list[-1]:
            return True
        else:
            return False

def search(input_list, number, first_search_index, last_search_index):

    first_index = first_search_index
    last_index = last_search_index
        
    mid_index = (first_index+last_index) // 2
    
    if input_list[mid_index] == number:
        return mid_index
    
    if check(input_list[first_index: mid_index], number):
        return search(input_list, number, first_index, mid_index-1)
        
    elif check(input_list[mid_index+1 : last_index+1], number):
        return search(input_list, number, mid_index+1, last_index)

    return -1

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    first_index = 0
    last_index = len(input_list)-1
    
    return search(input_list, number, first_index, last_index)
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[7, 8, 1, 2, 3, 4, 5, 6], 7])
test_function([[1], 1])
test_function([[], 100])