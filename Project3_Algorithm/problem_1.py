
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    if number == None:
        print('invalid number')
        return None
    if number < 0:
        print('Negative number does not have a square root')
        return None
    search_space = list(range(number+1))

    first_idx = 0
    last_idx = len(search_space)-1
    # count = 0
    # limit = 20

    while first_idx <= last_idx:
        # count += 1
        # if count>=limit:
        #     return 0
        # mid_idx = max((first_idx + last_idx)//2 -1 , first_idx)
        mid_idx = (first_idx + last_idx)//2
        print(f""" mid_idx : {mid_idx}, num : {search_space[mid_idx]}""")
        
        # next_element = mid_idx+1 if mid_idx + 1 < last_idx else 
        if (search_space[mid_idx] ** 2) <= number < ((search_space[mid_idx]+1) ** 2):
            return search_space[mid_idx]

        elif number < (search_space[mid_idx] **2 ):
            last_idx = mid_idx
        else:
            first_idx = mid_idx+1


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
print ("Pass" if  (None == sqrt(None)) else "Fail")