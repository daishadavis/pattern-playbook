# Problem: Course Schedule

**Pattern / Category:Graphs**

**Notes:**
- The problem is represented as a directed graph where each course is a node and prerequisites are directed edges
- The question is essentially: Can we complete all courses -> This reduces to check if the graph has a cycle
- If the graph contains a cycle it's impossible to finish all courses, If it's acyclic(DAG), then all course can be completed.
- This maps directly to Topological sorting(using BFS with indegree counting or DFS with cycle detection)

**Mini-Template (Core logic):
```
Build an adjacency list from prerequisites
Create a set to each track of nodes we have already processed
Create help dfs function and pass it a course:
    if course in visit:
        return False
    if preMap[crs] == []:
        return True 

```

**Complexity:**
 - Time: O(V + E) where V = number of courses, E = number of prerequisites
 - Space: 0(V + E)
