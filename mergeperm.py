def merge(arr1, arr2):
    if len(arr1) == 0: return arr2
    elif len(arr2) == 0: return arr1
    elif arr1[0] > arr2[0]: return [arr1[0]] + merge(arr1[1:], arr2)
    else: return [arr2[0]] + merge(arr1, arr2[1:])

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid_pos = int(len(arr) / 2)
    h1 = merge_sort(arr[:mid_pos]) #this specific slice might not be the most efficient
    h2 = merge_sort(arr[mid_pos:])
    return merge(h1,h2)




def merge_yield(arr1, arr2):
    if len(arr1) == 0: yield arr2
    elif len(arr2) == 0: yield arr1
    else:
        for n in merge_yield(arr1[1:], arr2):
            yield [arr1[0]] + n
        for n in merge_yield(arr1, arr2[1:]):
            yield [arr2[0]] + n

def merge_perm(arr):
    if len(arr) <= 1: yield arr
    else:
        mid_pos = int(len(arr) / 2)
        h1 = merge_perm(arr[:mid_pos])
        for h1n in h1:
            h2 = merge_perm(arr[mid_pos:])
            for h2n in h2:
                for n in merge_yield(h1n, h2n):
                    yield n
