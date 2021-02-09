def copy(arr):
    return [n for n in arr]

def select_sort(arr):
    if len(arr) == 1: return arr
    item = min(arr)
    send = copy(arr)
    send.remove(item)
    return [item] + select_sort(send)


def select_perm(arr):
    if len(arr) == 1: yield arr
    else:
        for n in arr:
            send = copy(arr)
            send.remove(n)
            for i in select_perm(send):
                yield [n] + i
