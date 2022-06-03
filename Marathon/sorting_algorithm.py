def _swap(lst,i,j):
    """Swaps elements at i and j"""
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

def _insert_into(lst,lo,hi,key):
    """
    Helper function for insertion_sort
    Inserts element at lst[hi] 
    into slice lst[lo:hi]
    """
    while hi > lo and key(lst[hi]) < key(lst[hi-1]):
        _swap(lst,hi-1,hi)
        hi -= 1

def _insertion_sort(lst,lo,hi,key):
    """
    In place implementation of 
    insertion sort algorithm.
    """
    for i in range(lo+1,hi):
        _insert_into(lst,lo,i,key)

def _partition(lst,lo,hi,key,pivot):
    """
    In place partition algorithm using
    the Hoarse partitioning scheme.
    """
    i,j = lo-1,hi
    while True:
        while True: # Do while loop simulated
            i += 1
            if key(lst[i])>=key(pivot):
                break
        while True: # Do while loop simulated
            j -= 1
            if key(lst[j])<=key(pivot):
                break
        if i>=j:
            return j
        _swap(lst,i,j)

def _median(small_lst,key):
    """
    Calculates the median of a small list
    using insertion_sort.
    """
    _insertion_sort(small_lst,0,len(small_lst),key)
    return small_lst[len(small_lst)//2]

def _quick_sort(lst,lo,hi,key):
    """Quicksort implementation using a key function"""
    if hi-lo <= 1:
        return
    if hi-lo <= 7:
        _insertion_sort(lst,lo,hi,key)
        return
    pivot = _median([lst[lo],lst[(lo+hi-1)//2],lst[hi-1]],key)
    pivot_idx = _partition(lst,lo,hi,key,pivot)
    _quick_sort(lst,lo,pivot_idx,key)
    _quick_sort(lst,pivot_idx+1,hi,key)

def quick_sort(lst=list,key=lambda x: x) -> list:
    """
    Quicksorts lst using a key function
    Accumulated Runtime O(n*log(n))
    Worst-Case Runtime O(n**2) for specially 
    constructed data. Could be avoided by 
    using median_of_medians pivot selection.
    Space Overhead O(log(n)) since in place
    The sorting algorithm is unstable i.e. does
    NOT preserve relative indeces of equal elements.

    Parameters:
    -----------
    lst : list
        The list that is to be sorted.
    key: T -> C, optional
        A key function that returns a comparable 
        object of type C when applied to list element
        of type e
        e.g. lambda t: t[1] to do pairwise comparison 
        on the second element of tuple t

    Returns:
    --------
    list
        The sorted list
    """
    _quick_sort(lst,0,len(lst),key)
    return lst

def _merge(lo,hi,key):
    """Merges two lists lo,hi using a key function"""
    lst = []
    i,j = 0,0
    while i < len(lo) and j < len(hi):
        if key(lo[i])<=key(hi[j]):
            lst.append(lo[i])
            i += 1
        else:
            lst.append(hi[j])
            j += 1
    return lst + lo[i:] + hi[j:]

def merge_sort(lst:list, key=lambda x: x) -> list:
    """
    Mergesorts lst using a key function
    Runtime O(n*log(n))
    Space Overhead O(n) since out of place
    The sorting algorithm is stable i.e. preserves 
    relative indeces of equal elements.

    Parameters:
    -----------
    lst : list
        The list that is to be sorted.
    key: T -> C, optional
        A key function that returns a comparable 
        object of type C when applied to list element
        of type e
        e.g. lambda t: t[1] to do pairwise comparison 
        on the second element of tuple t

    Returns:
    --------
    list
        A sorted copy of the list
    """
    if len(lst) <= 1:
        return lst
    return _merge(
        merge_sort(lst[:len(lst)//2],key),
        merge_sort(lst[len(lst)//2:],key),
        key)