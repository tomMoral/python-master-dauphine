def quicksort(ll):
    if len(ll) <= 1:
        return ll
    pivot = ll[0]
    less, greater = [], []
    for v in ll[1:]:
        if v <= pivot:
            less.append(v)
        else:
            greater.append(v)
    return quicksort(less) + [pivot] + quicksort(greater)

quicksort([-2, 3, 5, 1, 3])