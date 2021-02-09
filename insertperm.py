#this file describes the insert sort algorithm and an example of how it can be converted to a
#permutation

#note: i am using a non tail recursive version for the simplicity of the conversion
def insert_sort(arr):
    if len(arr) <= 1: return arr
    sort = insert_sort(arr[1:]) #would have called it sorted but that is reserverd in python
    head = arr[0]
    n = 0
    #normally I have this in a separate function but this works better for this example
        #i also feel like i might be able to higher order function this but again, the example
    while n < len(sort) and head > sort[n]: n+=1 #this is the comparison points in insert sort
    sort.insert(n, head)
    return sort

#to stop destructive modification of arrays
    #this is only here because i couldn't be bothered to find functionally pure insert in python
        #(or write one myself)
def copy(arr):
    return [n for n in arr]

#hopefully you should be able to see the similarities
def insert_perm(arr):
    if len(arr) == 1: 
        yield arr
    else:

        perm = insert_perm(arr[1:])
        head = arr[0]

        for p in perm: #as it yields

            n = 0
            while n <= len(p): #note: no comparison here
                tmp = copy(p)
                tmp.insert(n,head)
                yield tmp
                n+=1
