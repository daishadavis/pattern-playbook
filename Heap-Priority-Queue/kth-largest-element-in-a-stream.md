# Problem: Kth Largest Element in a Stream

**Pattern / Category: Min-Heap/ Priority Queue**

**Why this Pattern?:**
- We want to keep track of the top k elements at all times.
- A min-heap of size k makes this efficient:
    - insert a new number -> O(log k)
    - Remove the smallesthen size > k -> O(log k)
- Root of our heap = kth largest -> O(1)

**Mini-Template (Core logic):
```
class KthLargest:
    input: k (integer), nums (list of integers)
    data: minHeap (min-heap)
    
    constructor(k, nums):
        store k
        initialize minHeap = empty
        for each num in nums:
            add(num) // reuse add logic

    function add(val):
        push val into minHeap
        if size of minHeap > k:
            pop the smallest element from minHeap
        return minHeap root // root is the smallest number
```

**Complexity:**
 - Time: O(m * log k) -> k the kth largest number and m number of calls to add() or the number of new elements in the stream
 - Space: O(k) -> heap only stores k elements no matter how big the stream gets