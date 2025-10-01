def dfs_recursive(graph):
    """DFS recursion a adjancey list"""
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)

        return ans
    
    seen = {START_NODE}
    return dfs(START_NODE)


def dfs_interactive(graph):
    