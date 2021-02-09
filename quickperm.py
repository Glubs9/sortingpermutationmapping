def quick_sort(arr):
    if len(arr) <= 1: return arr
    bigger = quick_sort(list(filter(lambda n: n >= arr[0], arr[1:])))
    smaller = quick_sort(list(filter(lambda n: n < arr[0], arr[1:])))
    return smaller + [arr[0]] + bigger



#yields a tuple of included and not included
def combinations(arr):
    #this is the equivalent of the filter section of quick sort
    if len(arr) <= 1:
        yield ([arr[0]], [])
        yield ([], [arr[0]])
    else:
        rec = combinations(arr[1:])
        for (inc, ninc) in rec:
            yield ([arr[0]] + inc, ninc)
            yield (inc, [arr[0]] + ninc)

#could be thought of as equivalent to insert sort, like written inside out
def quick_perm(arr):
    if len(arr) <= 1: yield arr
    else:
        gen = combinations(arr[1:])
        for (inc, ninc) in gen:
            incp = quick_perm(inc)
            for n1 in incp:
                nincp = quick_perm(ninc) #i put this here just because it wasn't working and i was
                                            #mad and now it works???
                for n2 in nincp:
                    yield n1 + [arr[0]] + n2
