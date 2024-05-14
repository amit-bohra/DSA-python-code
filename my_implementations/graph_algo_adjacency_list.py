from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple

# Depth First Search (DFS) Algorithm
def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    DFS algorithm to traverse a graph starting from a given node.

    Assumption: The graph is represented using an adjacency list.
    Type Annotation:
        graph: Dict[int, List[int]] - Adjacency list representation of the graph.
        start: int - Starting node for DFS traversal.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use a stack (or recursion) to keep track of nodes to visit.
    """
    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return traversal_order

# Breadth First Search (BFS) Algorithm
def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    BFS algorithm to traverse a graph starting from a given node.

    Assumption: The graph is represented using an adjacency list.
    Type Annotation:
        graph: Dict[int, List[int]] - Adjacency list representation of the graph.
        start: int - Starting node for BFS traversal.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use a queue to keep track of nodes to visit.
    """
    visited = set()
    traversal_order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return traversal_order

# Union Find Algorithm (Disjoint Set Union)
class UnionFind:
    """
    Union Find data structure for implementing Union-Find algorithm.

    Assumption: Union Find data structure is used for disjoint-set data structure.
    Time Complexity:
        - Initialization: O(N) where N is the number of elements.
        - Union: O(log N)
        - Find: O(log N)
    Space Complexity: O(N) where N is the number of elements.
    Trick: Path compression and union by rank are used for optimal performance.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Topological Sort Algorithm
def topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    """
    Topological sort algorithm to find the linear ordering of vertices in a directed acyclic graph (DAG).

    Assumption: The graph is a directed acyclic graph (DAG).
    Type Annotation:
        graph: Dict[int, List[int]] - Adjacency list representation of the graph.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use DFS and stack to order the vertices.
    """
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

# Dijkstra's Algorithm
def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Dijkstra's algorithm to find the shortest paths from a single source node to all other nodes in a graph.

    Assumption: The graph is weighted and does not contain negative edge weights.
    Type Annotation:
        graph: Dict[int, List[Tuple[int, int]]] - Weighted adjacency list representation of the graph.
        start: int - Starting node for Dijkstra's algorithm.
    Time Complexity: O((V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use priority queue (heapq) to efficiently select the next vertex with the smallest distance.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        distance, node = heapq.heappop(pq)
        if distance > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            if distance + weight < distances[neighbor]:
                distances[neighbor] = distance + weight
                heapq.heappush(pq, (distance + weight, neighbor))

    return distances

# Prim's Algorithm
def prim(graph: Dict[int, List[Tuple[int, int]]]) -> Dict[int, int]:
    """
    Prim's algorithm to find the minimum spanning tree (MST) of a connected, undirected graph.

    Assumption: The graph is connected and undirected.
    Type Annotation:
        graph: Dict[int, List[Tuple[int, int]]] - Weighted adjacency list representation of the graph.
    Time Complexity: O((V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Trick: Use priority queue (heapq) to efficiently select the next edge with the smallest weight.
    """
    mst = {}
    visited = set()
    start_node = next(iter(graph))
    pq = [(0, start_node)]

    while pq:
        weight, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            if node != start_node:
                mst[node] = weight
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor))

    return mst

# Kruskal's Algorithm
def kruskal(graph: Dict[int, List[Tuple[int, int]]]) -> Dict[int, int]:
    """
    Kruskal's algorithm to find the minimum spanning tree (MST) of a connected, undirected graph.

    Assumption: The graph is connected and undirected.
    Type Annotation:
        graph: Dict[int, List[Tuple[int, int]]] - Weighted adjacency list representation of the graph.
    Time Complexity: O(E * log(E)) where E is the number of edges.
    Space Complexity: O(E) where E is the number of edges.
    Trick: Use Union-Find data structure to efficiently detect cycles while selecting edges.
    """
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, rank, x, y):
        root_x = find(parent, x)
        root_y = find(parent, y)

        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    mst = {}
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors]
    edges.sort()
    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst[(u, v)] = weight
            union(parent, rank, u, v)

    return mst

# Bellman-Ford Algorithm
def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Bellman-Ford algorithm to find the shortest paths from a single source node to all other nodes in a graph.

    Assumption: The graph may contain negative edge weights but should not contain negative cycles.
    Type Annotation:
        graph: Dict[int, List[Tuple[int, int]]] - Weighted adjacency list representation of the graph.
        start: int - Starting node for Bellman-Ford algorithm.
    Time Complexity: O(V * E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Relax edges repeatedly to find the shortest paths.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

# Floyd-Warshall Algorithm
def floyd_warshall(graph: Dict[int, Dict[int, int]]) -> Dict[int, Dict[int, int]]:
    """
    Floyd-Warshall algorithm to find all pair shortest paths in a weighted graph.

    Assumption: The graph may contain negative edge weights but should not contain negative cycles.
    Type Annotation:
        graph: Dict[int, Dict[int, int]] - Weighted adjacency list representation of the graph.
    Time Complexity: O(V^3) where V is the number of vertices.
    Space Complexity: O(V^2) where V is the number of vertices.
    Trick: Dynamic Programming approach to solve all pair shortest paths.
    """
    n = len(graph)
    distances = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        distances[i][i] = 0
        for neighbor, weight in graph[i].items():
            distances[i][neighbor] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

# Cycle Detection in Undirected Graph (Using DFS)
def has_cycle(graph: Dict[int, List[int]]) -> bool:
    """
    Cycle detection algorithm to detect cycles in an undirected graph.

    Assumption: The graph is undirected.
    Type Annotation:
        graph: Dict[int, List[int]] - Adjacency list representation of the graph.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use DFS to detect back edges while traversing the graph.
    """
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# Cut Vertex (Articulation Point) Detection
def find_cut_vertices(graph: Dict[int, List[int]]) -> Set[int]:
    """
    Cut vertex (articulation point) detection algorithm to find the vertices whose removal would increase the number of connected components.

    Assumption: The graph is undirected.
    Type Annotation:
        graph: Dict[int, List[int]] - Adjacency list representation of the graph.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use DFS to detect articulation points.
    """
    def dfs(node, parent, visited, disc, low, result):
        children = 0
        visited.add(node)
        disc[node] = time[0]
        low[node] = time[0]
        time[0] += 1

        for neighbor in graph[node]:
            if neighbor not in visited:
                children += 1
                dfs(neighbor, node, visited, disc, low, result)
                low[node] = min(low[node], low[neighbor])

                if parent is None and children > 1:
                    result.add(node)
                elif parent is not None and low[neighbor] >= disc[node]:
                    result.add(node)
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    visited = set()
    disc = {}
    low = {}
    result = set()
    time = [0]

    for node in graph:
        if node not in visited:
            dfs(node, None, visited, disc, low, result)

    return result

# Example usage:

# Constructing a graph
graph_adj_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4],
    4: [3]
}

# DFS example usage
print("DFS traversal:", dfs(graph_adj_list, 0))

# BFS example usage
print("BFS traversal:", bfs(graph_adj_list, 0))

# Topological Sort example usage
print("Topological Sort:", topological_sort(graph_adj_list))

# Dijkstra's Algorithm example usage
weighted_graph = {
    0: [(1, 4), (2, 3)],
    1: [(3, 2)],
    2: [(1, 1), (3, 5)],
    3: []
}
print("Dijkstra's shortest paths:", dijkstra(weighted_graph, 0))

# Prim's Algorithm example usage
print("Prim's Minimum Spanning Tree:", prim(weighted_graph))

# Kruskal's Algorithm example usage
print("Kruskal's Minimum Spanning Tree:", kruskal(weighted_graph))

# Bellman-Ford Algorithm example usage
weighted_graph_negative = {
    0: [(1, 4), (2, 3)],
    1: [(3, -2)],
    2: [(1, 1), (3, 5)],
    3: []
}
print("Bellman-Ford shortest paths:", bellman_ford(weighted_graph_negative, 0))

# Floyd-Warshall Algorithm example usage
weighted_graph_all_pairs = {
    0: {1: 4, 2: 3},
    1: {3: 2},
    2: {1: 1, 3: 5},
    3: {}
}
print("Floyd-Warshall all pair shortest paths:", floyd_warshall(weighted_graph_all_pairs))

# Cycle Detection example usage
print("Graph has cycle:", has_cycle(graph_adj_list))

# Cut Vertex Detection example usage
print("Cut vertices:", find_cut_vertices(graph_adj_list))
