def mergesort(items):
    
    if len(items)<=1:
        return items
    
    mid = len(items)//2

    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    first = list()
    second = list()

    sorted_list = mergesort(input_list)
    while len(sorted_list)!=0:

        if len(sorted_list)>0:
            first.append(sorted_list.pop())
            
        if len(sorted_list)>0:
            second.append(sorted_list.pop())
    
    first_len = len(first)
    first_total = 0
    
    second_len = len(second)
    second_total = 0

    for i, power in enumerate(range(first_len-1, -1, -1)):
        first_total += first[i] * (10**power)
        
    for i, power in enumerate(range(second_len-1, -1, -1)):
        second_total += second[i] * (10**power)
        
    return [first_total, second_total]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output, sum(output))
    print(f'sum(solution) = {sum(solution)}')
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9,4, 3,6], [94, 63]])
test_function([[1,2], [1, 2]])
