"""
Different sorting methods implemented
-Sequential Search
"""

def sequential_search(lst, search_item):
    """ (List, Object) -> int

    Linearly searches through the list and returns the index of the first item
    found matching search_item. Returns -1 if the items is not in lst.
    O(n)

    >>> sequential_search([1, 2, 32, 8, 17], 3)
    -1
    >>> sequential_search([1, 2, 32, 8, 17], 32)
    2
    """
    index = -1

    # Start at the beginning of lst. Update index and stop searching
    # if search_item is found.
    for i in range(len(lst)):
        if lst[i] == search_item:
            index = i
            break
            
    return index

def binary_search(lst, search_item):
    """ (List, Object, int, int) -> int

    Precondition: List must be ordered.

    Searches through the list and returns the index of the first item
    found matching search_item. Returns -1 if the items is not in lst.
    O(log n)
    """
    lo = 0
    hi = len(lst) 
        
    while lo < hi:
        mid = (lo + hi) // 2
        mid_val = lst[mid]
        print(mid_val)
        if mid_val < search_item:
            lo = mid + 1
        elif mid_val > search_item:
            hi = mid
        else:
            return mid
        
    return -1
