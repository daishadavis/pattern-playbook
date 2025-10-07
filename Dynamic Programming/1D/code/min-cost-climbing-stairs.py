from typing import List

def minCostClimbStairs(costs:List[int]) -> int:
    cache = {}
    
    def dfs(i):
        if i >= len(costs):
            return 0

        if i in cache:
            return cache[i]
        
        cache[i] = costs[i] + min(dfs(i+1), dfs(i+2))
        return cache[i]

    return min(dfs(0), dfs(1))