# sortingpermutationmapping
a theory of comparison sorting and permutation algorithm mapping (or isomorphism or equivalence idk i haven't been taught these terms but you get what i am saying)

# better explanation
The idea I have is that comparison sorting algorithms (insert sort, merge sort, ...) can be algorithmacially mapped to permutation finding algorithms (and potentially vice verse but I am struggling a bit with that one). 

# intuitive explanations 
The reason I think this is possible is because I think you can conceptualise comparison sorting algorithms as permutation finders that prune the permutations based on whether or not they are sorted. Another way of thinking about this is that when a comparison sorting algorithm compares two numbers, instead of deciding which path to take, you choose both! thereby switching all position on the list.

# the algorithm
the idea is, you are returning a generator that yields each option. At every decision point you yield both decisions. This introduces a problem in that recursive calls return a generator and you can't modify that generator. To get around this you have to iterator over any recursive calls made. I think this could be solved (or at least look nicer) by handling iterators as a monad for non-determinism, in a similar way that the list monad works (or at least in haskell), but I have not done this for the sake of readability.

# what are the other files?
I have included some examples of this transformation with the rest of the files. Hopefully this makes the idea more clear.

# TO-DO

1. I have no formal proof cause i have no clue how to, if you discover this and want to give it a shot I implore you to give it a go and fork / pull request your findings!            
2. I had some problems with implementing bubble sort in this fashion. This is cause bubble sort halts when it finds the list is sorted and I am not sure how to convert that to the idea presented in this github. Feel free to give it a shot! I'd love to see any attempts, even if they don't work!              
3. I would like to try this the other way around, converting permutation finding algorithms to sorting algorithms, but I am not sure it will work and I am finding it hard to find many candidates as permutation algorithsm are not coveredd in the same depth as sorting algorithms. As of right now I am trying to convert the only algorithm I can find, heap's algorithm, to a sorting algorithm but I haven't finished it yet.           
