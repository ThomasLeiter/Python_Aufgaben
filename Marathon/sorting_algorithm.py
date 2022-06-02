def _swap(lst,i,j):
    """Swaps elements at i and j"""
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

def _insert_into(lst,lo,hi,selector):
    """
    Helper function for insertion_sort
    Inserts element at lst[hi] 
    into slice lst[lo:hi]
    """
    while hi > lo and selector(lst[hi]) < selector(lst[hi-1]):
        _swap(lst,hi-1,hi)
        hi -= 1

def _insertion_sort(lst,lo,hi,selector):
    """
    In place implementation of 
    insertion sort algorithm.
    """
    for i in range(lo+1,hi):
        _insert_into(lst,lo,i,selector)

def _partition(lst,lo,hi,selector,pivot):
    """
    In place partition algorithm using
    the Hoarse partitioning scheme.
    """
    i,j = lo-1,hi
    while True:
        while True: # Do while loop simulated
            i += 1
            if selector(lst[i])>=selector(pivot):
                break
        while True: # Do while loop simulated
            j -= 1
            if selector(lst[j])<=selector(pivot):
                break
        if i>=j:
            return j
        _swap(lst,i,j)

def _median(small_lst,selector):
    """
    Calculates the median of a small list
    using insertion_sort.
    """
    _insertion_sort(small_lst,0,len(small_lst),selector)
    return small_lst[len(small_lst)//2]

def _quick_sort(lst,lo,hi,selector):
    """Quicksort implementation using a selector function"""
    if hi-lo <= 1:
        return
    if hi-lo <= 7:
        _insertion_sort(lst,lo,hi,selector)
        return
    pivot = _median([lst[lo],lst[(lo+hi-1)//2],lst[hi-1]],selector)
    pivot_idx = _partition(lst,lo,hi,selector,pivot)
    _quick_sort(lst,lo,pivot_idx,selector)
    _quick_sort(lst,pivot_idx+1,hi,selector)

def quick_sort(lst=list,selector=lambda x: x) -> list:
    """
    Quicksorts lst using a selector function
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
    selector: T -> C, optional
        A selector function that returns a comparable 
        object of type C when applied to list element
        of type e
        e.g. lambda t: t[1] to do pairwise comparison 
        on the second element of tuple t

    Returns:
    --------
    list
        The sorted list
    """
    _quick_sort(lst,0,len(lst),selector)
    return lst

def _merge(lo,hi,selector):
    """Merges two lists lo,hi using a selector function"""
    lst = []
    i,j = 0,0
    while i < len(lo) and j < len(hi):
        if selector(lo[i])<=selector(hi[j]):
            lst.append(lo[i])
            i += 1
        else:
            lst.append(hi[j])
            j += 1
    return lst + lo[i:] + hi[j:]

def merge_sort(lst:list, selector=lambda x: x) -> list:
    """
    Mergesorts lst using a selector function
    Runtime O(n*log(n))
    Space Overhead O(n) since out of place
    The sorting algorithm is stable i.e. preserves 
    relative indeces of equal elements.

    Parameters:
    -----------
    lst : list
        The list that is to be sorted.
    selector: T -> C, optional
        A selector function that returns a comparable 
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
        merge_sort(lst[:len(lst)//2],selector),
        merge_sort(lst[len(lst)//2:],selector),
        selector)