from typing import List


def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    """A function that returns the combinations of the target"""
    res = []

    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return

        if i >= len(nums) or total > target:
            return

        curr.append(nums[i])
        dfs(i, curr, total + nums[i])
        curr.pop()
        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res
