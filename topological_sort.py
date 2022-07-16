from typing import List
from collections import defaultdict, deque


def topological_sort(vertices: int, edges: List[List[int]]) -> List[int]:
    """ Returns the topologically sorted nodes 

            Parameters:
                    vertices: The number of vertices in the input graph
                    edges: Edge pairs of the form [[e1, e2], [e2, e3], ...]

            Returns:
                    A list containing the topologically sorted nodes
    """
    sorted_order = []

    # Step 1: Initialize the graph
    in_degree = {i:0 for i in range(vertices)}
    graph = defaultdict(list)

    # Step 2: Build the graph
    for (parent, child) in edges:
        graph[parent].append(child)
        in_degree[child] += 1

    # Step 3: Find all sources
    sources = deque([key for key in in_degree if in_degree[key] == 0])

    # Step 4: Run BFS to topologically sort the nodes
    while sources:
        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    
    # Step 5: Check for cycles (if there is a cycle, those nodes don't get processed
    # since they're in_degree is always > 1, hence sorted_order will be smaller than vertices)
    if len(sorted_order) != vertices:
        return []
    
    return sorted_order

    
if __name__ == "__main__":
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))








