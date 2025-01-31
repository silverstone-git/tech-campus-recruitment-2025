# First approach

## Linear search:
    - readlines() would mean copying the entire file into RAM, which, is physically impossible, let alone inefficient
    - Very inefficient as an algorithm for large files
    - used a single with: block, so bad 


## Binary search, then, when found, expanded outwards
    - no readline(index) method, so, just pointer being incremented/decremented all over the place: an acceptable tradeoff
    - two with blocks: code quality / seperation of concerns <=> opening/reopening cost tradeoff
    - Very efficient for large files

## Binary search, then, when found, found reverse elements first, and then successive
    - same thing, but coalesced fetching used, so, the elements are next to each other in memory
    - , which is way more efficient than jumbling through the memory space
