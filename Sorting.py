"""
Different Sorting Methods
Precondition: Items in the list must be comparable.
-Quick Sort (More efficient)
-Quick Sort2 (Naive)
-Merge Sort
-Shell Sort
-Insertion Sort
-Selection Sort
-Bubble Sort
"""
from random import randint, shuffle

def quick_sort(list1):
    # Easy way to call quick_sort
    quick_sort_index(list1, 0, len(list1) - 1)

def quick_sort_index(list1, left, right):
    """ (List, int, int) -> None
    """
    if left < right: 
        pivot_pos = partition(list1, left, right )
        #recursively call quick_sort on left and right
        quick_sort_index(list1, left, pivot_pos - 1)
        quick_sort_index(list1, pivot_pos + 1, right)

def partition(list1, left, right):
    # Left and Right are the start and end indixes of the subarray
    pivot = randint(left, right)
    list1[left], list1[pivot] = list1[pivot], list1[left]
    i = left + 1
    pivot = list1[left]# choose first element in subarray as pivot
     
    for j in range(left + 1, right + 1):
        if list1[j] < pivot:
            list1[j], list1[i] = list1[i], list1[j]
            i += 1
             
    pivot_position = i - 1
    list1[left], list1[pivot_position] = list1[pivot_position], list1[left]
    #new pivot position. Used to determine the next left and right side
    return pivot_position     

def quick_sort2(list1):
    """ (List) -> List
    
    Simple version of quicksort
    """
    if list1 == []: 
        return []
    else:
        pivot = list1[0]
        lesser = quick_sort([x for x in list1[1:] if x < pivot])
        greater = quick_sort([x for x in list1[1:] if x >= pivot])
        return lesser + [pivot] + greater
    
from heapq import merge
def merge_sort(list1):
    """ (List) -> List

    The basic idea is to split the collection into smaller groups by halving
    it until the groups only have one element or no elements.
    
    O(n*log n)
    
    
    >>> alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> merge_sort(alist)
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    if len(list1) <= 1:
        return list1

    middle = len(list1) // 2
    left = list1[:middle]
    right = list1[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

# MERGE METHOD TO USE IF YOU CHOOSE TO NOT IMPORT MERGE FROM HEAPQ
def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1


    if left:
        result.extend(left[left_index:])
    if right:
        result.extend(right[right_index:])
    return result

def shell_sort(list1):
    """ (List) -> None

    Shellsort is a sequence of interleaved insertion sorts based on an increment sequence.
    With an increment size of 1, the sort is a basic insertion sort, but by this time the data
    is guaranteed to be almost sorted, which is insertion sort's "best case".

    O(n log^2 n)
    
    Picking the Gap Note:
    Empirical studies have shown a geometric increment sequence
    with a ratio of about 2.2 work well in practice.
    
    >>> alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> shell_sort(alist)
    >>> alist
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    gap = len(list1) // 2
    while gap > 0:
        for index, value in enumerate(list1):
            while index >= gap and list1[index - gap] > value:
                list1[index] = list1[index - gap]
                index -= gap
            list1[index] = value
        if gap == 2:
            gap = 1
        else:
            gap = int( gap * 5.0 / 11)

    
def insertion_sort(list1):
    """ (List) -> None

    A sorting algorithm which moves elements one at a time into the correct position.

    O(n^2)

    >>> alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> insertion_sort(alist)
    >>> alist
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    for index in range(1, len(list1)): # Skip over the first item
        value = list1[index]
        j = index
        while j > 0 and list1[j - 1] > value:
            list1[j] = list1[j - 1] 
            j = j - 1
        list1[j] = value

def selection_sort(list1):
    """ (List) -> NoneType
    
    Find the smallest element in the list and exchange it with the
    element in the first position. Then find the second smallest element
    and exchange it with the element in the second position. Continue
    to do this until the entire list is sorted.

    O(n^2)
    
    >>> alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> selection_sort(alist)
    >>> alist
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    for index in range(len(list1) - 1):
        value = list1[index]
        # enumerate all (index, value) pairs from the non sorted part of list1
        # and take the pair with the smallest value
        min_subindex, min_value = \
                      min(enumerate(list1[index+1:]), key=lambda x: x[1])
        # Place the smallest value in the correct index
        if min_value < value:
            list1[index] = min_value
            list1[min_subindex + index + 1] = value
 
def bubble_sort(list1):
    """ (List) -> NoneType
    
    The bubble sort works by passing sequentially over a list, comparing each
    value to the one immediately after it. If the first value is greater than
    the second, their positions are switched. Over a number of passes, at most
    equal to the number of elements in the list, all of the values drift into
    their correct positions (large values "bubble" rapidly toward the end,
    pushing others down around them).
    
    >>> alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> bubble_sort(alist)
    >>> alist
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    """
    sorted = False
    length = len(list1) - 1
    
    while length > 0 and not sorted:
        sorted = True # Assume the list is sorted
        for element in range(length):
            if list1[element] > list1[element + 1]:
                sorted = False # Found two elements in wrong order
                # Swap the two elements
                list1[element], list1[element + 1] = \
                                list1[element + 1], list1[element]
        length = length - 1
