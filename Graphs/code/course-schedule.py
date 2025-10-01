from typing import List
from collections import defaultdict

def canFinish(numCourses: int, prerequisites: List[List[int]]):
    """Returns true is we cna finish our courses returns false if not"""
    preMap = defaultdict(list)
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
        
    visit = set()
    def dfs(crs):
        if crs in visit:
            return False
        if preMap[crs] == []:
            return True
        
        visit.add(crs)
        for pre in preMap[crs]:
            if not dfs(crs):
                return False
        visit.remove(crs)
        preMap[crs] = []
        return True
    
    for c in range(numCourses):
        if not dfs(c):
            return False
    return True