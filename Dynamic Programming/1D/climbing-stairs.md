# Problem: Climbing Stairs 

**Pattern / Category:1-D Dynamic Programming**

**Notes:**
- Using the Top-Down approach we can start from the original number and work our way down to the base cases 
- Start from the original number and work down to the base cases
- Top-down plus memo builds the tree and trims repeats with cache
- Bottom-up builds the array sequentially, no recursion, no repeats

**Mini-Template (Core logic):
```
Initialize memory cache

Initialize climb_helper function(i):
    if i <= 1:
        return 1

    if i in memory cache:
        return memorycache[i]
    
    memorycache[i] = climb_helper(i - 1) + climb_helper(i - 2)
    
    return memorycache[i]

return climb_helper(n)

```

**Complexity:**
 - Time: O(n)
 - Space: O(n)
