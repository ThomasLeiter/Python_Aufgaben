from sorting_algorithm import merge_sort,quick_sort,heap_sort,insertion_sort

from random import shuffle
from time import time_ns

def test_performance(sorting_function,t_total=1.0e3):
    """
    Parameters:
    -----------
    sorting_function : list, [key] -> list
        A sorting function
    t_total : float, optional
        Available time in ms
    
    Returns:
    --------
    int
        The largest size sorted in t_total
    """
    a,b = 1,2
    t = 0
    while t < t_total:
        lst = list(range(b))
        shuffle(lst)
        t0 = time_ns()
        sorting_function(lst)
        t += (time_ns() - t0)/1.0e6
        a,b = b,a+b
    return a

def test_stable(sorting_function):
    """
    Tests whether the sorting function is stable i.e. 
    preserves relative position of equal elements.

    Parameters:
    -----------
    sorting_function : list, [key] -> list
        A sorting function
    
    Returns:
    --------
    True if stable, else False
    """
    N = 100
    lst = [n//10 for n in range(N)]
    shuffle(lst)
    lst = list(zip(lst,range(N)))
    lst = sorting_function(lst,key=lambda p: p[0])
    return all(lst[i] <= lst[i+1] for i in range(N-1))

if __name__ == '__main__':
    for sorting_function in (merge_sort,quick_sort,heap_sort,insertion_sort):
        print(f"Testing {sorting_function.__name__} ...")
        p = test_performance(sorting_function)
        print(f"Sorted a maximum of {p} elements within one second.")
        s = test_stable(sorting_function)
        print(f"Sorting was performed stable: {s}\n")
