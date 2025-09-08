from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Returning all subsets"""
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


