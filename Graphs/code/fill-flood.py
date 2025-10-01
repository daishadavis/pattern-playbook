from typing import List
from collections import deque


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """Returns an image once a flood fill has been performed"""
    # Calculate the rows and cols in our image
    ROWS, COLS = len(image), len(image[0])

    # Store the directions we can travel our image
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # store the original color
    original_color = image[sr][sc]

    # is he starting position is the same color as the color passed return the image
    if image[sr][sc] == color:
        return image

    # Helper bfs function
    def bfs(r, c):
        # Initalize our queue
        queue = deque()
        # Add the first position to our queue
        queue.append((r, c))
        # change the color of the position
        image[r][c] = color

        # while our queue is not empty
        while queue:
            # Pop the first position from our queue
            row, col = queue.popleft()
            # Loop through our directions array
            for dr, dc in directions:
                # calculate its neighbors
                nr, nc = dr + row, dc + col
                # if nr is out of bounds or nc i sout of bounds or position is not the same color
                if (
                    nr < 0
                    or nc < 0
                    or nr >= ROWS
                    or nc >= COLS
                    or image[nr][nc] != original_color
                ):
                    continue

                # change the color of our position
                image[nr][nc] = color
                # push it to the queue
                queue.append((nr, nc))

    # pass our starting position to bfs
    bfs(sr, sc)
    return image
