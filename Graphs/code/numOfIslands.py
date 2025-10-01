from typing import List


def numIslands(grid: List[List[str]]) -> int:
    """Returns the number of islands found in a matrix"""
    # Calculate the number of rows and cols
    ROWS, COLS = len(grid), len(grid[0])

    # Store the directions we can travel our matrix in an array (easier to loop)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Keep track of the number of islands we find
    islands = 0

    # Create a dfs helper function
    def dfs(r, c):
        # check if our r index is our of bounds or our c index is out of bounds or if our grid point is water
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
            return

        # Mark as visited (sink the island)
        grid[r][c] = "0"

        # Recursively call the neighbors of our current (r,c)
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Loop through our maxrix to find a grid[r][c] point equal to one and pass it to our dfs function
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                dfs(r, c)
                islands += 1

    return islands
