from typing import List, Tuple
from collections import defaultdict, deque

def build_order(projects: List[str], dependencies: List[Tuple[str]]) -> List[str]:
    sorted_order = []

    indegree = {p: 0 for p in projects}
    print(indegree)
    graph = defaultdict(list)

    for (parent, child) in dependencies:
        graph[parent].append(child)
        indegree[child] += 1
    
    sources = deque([key for key in indegree if indegree[key] == 0])
    
    while sources:
        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
        
    if len(sorted_order) != len(projects): return []  # Contains cycle

    return sorted_order


if __name__ == "__main__":
    print(build_order(
        projects=['a', 'b', 'c', 'd', 'e', 'f'],
        dependencies=[('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')] 
    ))