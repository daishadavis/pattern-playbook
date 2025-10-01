from typing import List

def climbing_stairs(n):
    """Returns the combination of steps you can climb"""
    memo = {}
    
    def dfs(i):
        if i <= 1:
            return 1
        
        if i in memo:
            return memo[i]
        
        memo[i] = dfs(i - 1) + dfs(i - 2)
        return memo[i]
    
    return dfs(n)

print(climbing_stairs(3))
    