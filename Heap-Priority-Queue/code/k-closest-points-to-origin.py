import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """Returns k elements closest to the origin"""
    minheap = []
    res = []

    for x, y in points:
        dist = (x**2) + (y**2)
        minheap.append([dist, x, y])

    heapq.heapify(minheap)

    while k > 0:
        dist, x, y = heapq.heappop(minheap)
        res.append([x, y])
        k -= 1

    return res
