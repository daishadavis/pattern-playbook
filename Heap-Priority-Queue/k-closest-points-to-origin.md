# Problem: K Closest Points to Origin 

**Pattern / Category: Mix-Heap/ Priority Queue**

**Why this Pattern?:**
- Need to keep track of the points closest to the origin (smallest distance)

**Mini-Template (Core logic):
```
Initialize our min-heap array
Initialize result array

for each x,y in points:
    calculate the distance from the origin
    add out distance and x,y point to our min-heap array

convert our array to a min-heap

While k is greater than zero:
    remove the first point from our min-heap // closest point
    add it to our results array
    decrement k by 1 // sine we want k closest points

return result array

```

**Complexity:**
 - Time: O(k * log n)
 - Space: O(n)