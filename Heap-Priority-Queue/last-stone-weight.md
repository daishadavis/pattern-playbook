# Problem: Last Stone Weight

**Pattern / Category: Max-Heap/ Priority Queue**

**Why this Pattern?:**
- Every turn we must find the two heaviest stones

**Mini-Template (Core logic):
```
Convert all stones to negative // to simulate max-heap using min-heap
create a heap from stones

while heap has more than 1 element:
    first = remove the top element //largest stone
    second = remove the top element // 2nd largest

    if first not equal to second:
        push (first - second) back to the heap

if heap is empty:
    return 0
else:
    return absolute value of remaining element

```

**Complexity:**
 - Time: 0(n log n)
 - Space: 0(n)