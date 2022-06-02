# Swaps elements at i and j
def _swap(lst,i,j):
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

# Helper function for insertion_sort
# Inserts element at lst[hi] 
# into slice lst[lo:hi]
def _insert_into(lst,lo,hi,selector):
    while hi > lo and selector(lst[hi]) < selector(lst[hi-1]):
        _swap(lst,hi-1,hi)
        hi -= 1

# In place implementation of 
# insertion sort algorithm.
def _insertion_sort(lst,lo,hi,selector):
    for i in range(lo+1,hi):
        _insert_into(lst,lo,i,selector)

# In place partition algorithm using
# the Hoarse partitioning scheme
def _partition(lst,lo,hi,selector,pivot):
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

# Calculates the median of a small list
# or tuple using insertion_sort.
def _median(small_lst,selector):
    _insertion_sort(small_lst,0,len(small_lst),selector)
    return small_lst[len(small_lst)//2]

# Quicksort implementation using a selector function
def _quick_sort(lst,lo,hi,selector):
    if hi-lo <= 1:
        return
    if hi-lo <= 7:
        _insertion_sort(lst,lo,hi,selector)
        return
    pivot = _median([lst[lo],lst[(lo+hi-1)//2],lst[hi-1]],selector)
    pivot_idx = _partition(lst,lo,hi,selector,pivot)
    _quick_sort(lst,lo,pivot_idx,selector)
    _quick_sort(lst,pivot_idx+1,hi,selector)

############################################
# Quicksorts lst using the selector function
# Accumulated Runtime O(n*log(n))
# Worst-Case Runtime O(n**2) for specially 
# constructed data. Could be avoided by 
# using median_of_medians pivot selection.
# Space Overhead O(log(n)) since in place
# The sorting algorithm is unstable i.e. does
# NOT preserve relative indeces of equal elements.
def quick_sort(lst,selector=lambda x: x):
    _quick_sort(lst,0,len(lst),selector)
    return lst

####################################################
# Merges two lists lo,hi using the selector function
def _merge(lo,hi,selector):
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

############################################
# Mergesorts lst using the selector function
# Runtime O(n*log(n))
# Space Overhead O(n) since out of place
# The sorting algorithm is stable i.e. preserves 
# relative indeces of equal elements.
def merge_sort(lst, selector=lambda x: x):
    if len(lst) <= 1:
        return lst
    return _merge(
        merge_sort(lst[:len(lst)//2],selector),
        merge_sort(lst[len(lst)//2:],selector),
        selector)