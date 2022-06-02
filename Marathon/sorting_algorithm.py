def _swap(lst,i,j):
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

def _insert_into(lst,lo,hi,selector):
    while hi > lo and selector(lst[hi]) < selector(lst[hi-1]):
        _swap(lst,lo,hi)
        hi -= 1

def _insertion_sort(lst,lo,hi,selector):
    for i in range(lo+1,hi):
        _insert_into(lst,lo,i,selector)

def _partition(lst,lo,hi,selector,pivot):
    i,j = lo-1,hi
    while True:
        while True:
            i += 1
            if selector(lst[i])>=selector(pivot):
                break
        while True:
            j -= 1
            if selector(lst[j])<=selector(pivot):
                break
        if i>=j:
            return j
        _swap(lst,i,j)

def _median(small_lst,selector):
    _insertion_sort(small_lst,0,len(small_lst),selector)
    return small_lst[len(small_lst)//2]

def _quick_sort(lst,lo,hi,selector):
    if hi-lo <= 1:
        return
    if hi-lo <= 7:
        _insertion_sort(lst,lo,hi,selector)
        return
    pivot = _median([lst[lo],lst[(lo+hi)//2],lst[hi]],selector)
    pivot_idx = _partition(lst,lo,hi,selector,pivot)
    _quick_sort(lst,lo,pivot_idx-1,selector)
    _quick_sort(lst,pivot_idx+1,hi,selector)

def sort(lst,selector=lambda x: x):
    _quick_sort(lst,0,len(lst),selector)