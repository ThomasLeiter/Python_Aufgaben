def _swap(lst,i,j):
    """Swaps elements at i and j"""
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

def _insert_into(lst,hi,key):
    """
    Helper function for insertion_sort
    Inserts element at lst[hi] 
    into slice lst[:hi]
    """
    while hi > 0 and key(lst[hi]) < key(lst[hi-1]):
        _swap(lst,hi-1,hi)
        hi -= 1

def insertion_sort(lst:list,key=lambda x: x) -> list:
    """
    In place implementation of insertion sort algorithm.
    Runtime in O(n**2). There is no Space overhead.
    The sorting algorithm is stable i.e. preserves 
    relative indeces of equal elements.

    Parameters:
    -----------
    lst : list
        The list that is to be sorted.
    key: T -> C, optional
        A key function that returns a comparable 
        object of type C when applied to list element
        of type T
        e.g. lambda t: t[1] to do pairwise comparison 
        on the second element of tuple t

    Returns:
    --------
    list
        The sorted list
    """
    for i in range(len(lst)):
        _insert_into(lst,i,key)
    return lst

def _partition(lst,lo,hi,key,pivot):
    """
    In place partition algorithm using
    the Hoarse partitioning scheme. 
    (see wikipedia for further deatils)
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
    insertion_sort(small_lst,key)
    return small_lst[len(small_lst)//2]

def _quick_sort(lst,lo,hi,key):
    """Quicksort implementation using a key function"""
    if hi-lo <= 1:
        return
    # Find pivot element as median of head, tail and center
    pivot = _median([lst[lo],lst[(lo+hi-1)//2],lst[hi-1]],key)
    # Partition and obtain index of the pivot element
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
        of type T
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
    # Merge iteration
    while i < len(lo) and j < len(hi):
        if key(lo[i])<=key(hi[j]):
            lst.append(lo[i])
            i += 1
        else:
            lst.append(hi[j])
            j += 1
    # Append remaining tail to merged list.
    # One tail is always empty.
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
        of type T
        e.g. lambda t: t[1] to do pairwise comparison 
        on the second element of tuple t

    Returns:
    --------
    list
        A sorted copy of the list
    """
    if len(lst) <= 1:
        return lst
    lo = merge_sort(lst[:len(lst)//2],key)
    hi = merge_sort(lst[len(lst)//2:],key)
    return _merge(lo,hi,key)

def _repair_tail(lst,i,key):
    """
    Repair heapstructure from tail to head.
    Restore Invariant lst[i] <= lst[i//2]
    i.e. child <= parent
    """
    if i == 0:
        return
    # If Child is bigger than parent, swap and recurse
    if key(lst[i]) > key(lst[i//2]): 
        _swap(lst,i,i//2) 
        _repair_tail(lst,i//2,key)

def _heapify(lst,key):
    """
    Turn lst in place into
    a decending binary heap 
    with maximum at head.
    """
    for i in range(len(lst)-1,0,-1):
        _repair_tail(lst,i,key)

def _repair_root(lst,i,hi,key):
    """
    Repair heapstructure from head to hi.
    Restore Invariant: lst[i] >= max(lst[2*i+1],lst[2*i+2])
    i.e. parent >= child
    """
    if 2*i+1>=hi: # Node i has no children
        return
    if 2*i+2>=hi: # Only left child existent
        if key(lst[i])<key(lst[2*i+1]):
            _swap(lst,i,2*i)
        return
    # If left child is biggest, make root and go left
    if key(lst[2*i+1])>=key(lst[2*i+2]) and key(lst[i])<key(lst[2*i+1]):
        _swap(lst,i,2*i+1)
        _repair_root(lst,2*i+1,hi,key)
        return
    # If right child is biggest, make root and go right
    if key(lst[2*i+1])<key(lst[2*i+2]) and key(lst[i])<key(lst[2*i+2]):
        _swap(lst,i,2*i+2)
        _repair_root(lst,2*i+2,hi,key)
        return

def heap_sort(lst:list,key=lambda x: x) -> list:
    """
    Heapsorts lst using a key function
    Worst-Case Runtime O(n*log(n)) 
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
        of type T
        e.g. lambda t: t[1] to do pairwise comparison 
        on the second element of tuple t

    Returns:
    --------
    list
        The sorted list
    """
    _heapify(lst,key)                 # Build descending heap structure.
    for hi in range(len(lst)-1,0,-1):
        _swap(lst,0,hi)               # Swap maximum to end of list
        _repair_root(lst,0,hi,key) # Restore the heap condition
    return lst

if __name__ == "__main__":
    for f in [insertion_sort,merge_sort,quick_sort,heap_sort]:
        lst = [3,1,4,2,7,1,5]
        print(f"{f.__name__} {f(lst)}")