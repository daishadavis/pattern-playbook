Problem Template:

# Problem: Min Cost Climbing Stairs 

**Pattern / Category:1-DP**

**Notes:**
- 

**Mini-Template (Core logic):
```
Initialize cache
helper dfs(i):
    if i less than or equal the length of cost:
        return 0
    
    if i in cache:
        return cache[i]
    
    cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
    return cache[i]

return min(dfs(0), dfs(1))

```

**Complexity:**
 - Time: O(n)
 - Space: O(n)