def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    zero_array = list()
    one_array = list()
    two_array = list()
    
    for value in input_list:
        if value == 0:
            zero_array.append(0)
        elif value == 1:
            one_array.append(1)
        elif value == 2: 
            two_array.append(2)
        else:
            print('The input list has element that is not 0, 1, 2.')
            continue
            
    return zero_array+one_array+two_array

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2])
test_function([])