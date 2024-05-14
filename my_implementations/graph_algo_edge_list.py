import heapq
from typing import List, Dict, Set, Tuple

# Depth First Search (DFS) Algorithm
def dfs(graph: List[Tuple[int, int]], start: int) -> List[int]:
    """
    DFS algorithm to traverse a graph starting from a given node.

    Assumption: The graph is represented using an edge list.
    Type Annotation:
        graph: List[Tuple[int, int]] - Edge list representation of the graph.
        start: int - Starting node for DFS traversal.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use a stack (or recursion) to keep track of nodes to visit.
    """
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return traversal_order

# Breadth First Search (BFS) Algorithm
def bfs(graph: List[Tuple[int, int]], start: int) -> List[int]:
    """
    BFS algorithm to traverse a graph starting from a given node.

    Assumption: The graph is represented using an edge list.
    Type Annotation:
        graph: List[Tuple[int, int]] - Edge list representation of the graph.
        start: int - Starting node for BFS traversal.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use a queue to keep track of nodes to visit.
    """
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()
    traversal_order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(neighbor for neighbor in adj_list[node] if neighbor not in visited)

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
def topological_sort(graph: List[Tuple[int, int]]) -> List[int]:
    """
    Topological sort algorithm to find the linear ordering of vertices in a directed acyclic graph (DAG).

    Assumption: The graph is a directed acyclic graph (DAG).
    Type Annotation:
        graph: List[Tuple[int, int]] - Edge list representation of the graph.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use DFS and stack to order the vertices.
    """
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in adj_list:
        if node not in visited:
            dfs(node)

    return stack[::-1]

# Dijkstra's Algorithm
def dijkstra(graph: List[Tuple[int, int, int]], start: int) -> Dict[int, int]:
    """
    Dijkstra's algorithm to find the shortest paths from a single source node to all other nodes in a graph.

    Assumption: The graph is weighted and does not contain negative edge weights.
    Type Annotation:
        graph: List[Tuple[int, int, int]] - Weighted edge list representation of the graph.
        start: int - Starting node for Dijkstra's algorithm.
    Time Complexity: O((V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use priority queue (heapq) to efficiently select the next vertex with the smallest distance.
    """
    adj_list = defaultdict(list)
    for u, v, weight in graph:
        adj_list[u].append((v, weight))

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in adj_list[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))

    return distances

# Prim's Algorithm
def prim(graph: List[Tuple[int, int, int]]) -> Dict[int, int]:
    """
    Prim's algorithm to find the minimum spanning tree (MST) of a connected, undirected graph.

    Assumption: The graph is connected and undirected.
    Type Annotation:
        graph: List[Tuple[int, int, int]] - Weighted edge list representation of the graph.
    Time Complexity: O((V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use priority queue (heapq) to efficiently select the next edge with the smallest weight.
    """
    adj_list = defaultdict(list)
    for u, v, weight in graph:
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))

    mst = {}
    visited = set()
    start_node = 0
    pq = [(0, start_node)]

    while pq:
        weight, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            if node != start_node:
                mst[node] = weight
            for neighbor, edge_weight in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor))

    return mst

# Kruskal's Algorithm
def kruskal(graph: List[Tuple[int, int, int]]) -> Dict[int, int]:
    """
    Kruskal's algorithm to find the minimum spanning tree (MST) of a connected, undirected graph.

    Assumption: The graph is connected and undirected.
    Type Annotation:
        graph: List[Tuple[int, int, int]] - Weighted edge list representation of the graph.
    Time Complexity: O(E * log(E)) where E is the number of edges.
    Space Complexity: O(E) where E is the number of edges.
    Trick: Use Union-Find data structure to efficiently detect cycles while selecting edges.
    """
    mst = {}
    edges = sorted(graph, key=lambda x: x[2])
    uf = UnionFind(len(edges))

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            mst[(u, v)] = weight
            uf.union(u, v)

    return mst

# Bellman-Ford Algorithm
def bellman_ford(graph: List[Tuple[int, int, int]], start: int) -> Dict[int, int]:
    """
    Bellman-Ford algorithm to find the shortest paths from a single source node to all other nodes in a graph.

    Assumption: The graph may contain negative edge weights but should not contain negative cycles.
    Type Annotation:
        graph: List[Tuple[int, int, int]] - Weighted edge list representation of the graph.
        start: int - Starting node for Bellman-Ford algorithm.
    Time Complexity: O(V * E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Relax edges repeatedly to find the shortest paths.
    """
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    return distances

# Floyd-Warshall Algorithm
def floyd_warshall(graph: List[Tuple[int, int, int]]) -> Dict[Tuple[int, int], int]:
    """
    Floyd-Warshall algorithm to find all pair shortest paths in a weighted graph.

    Assumption: The graph may contain negative edge weights but should not contain negative cycles.
    Type Annotation:
        graph: List[Tuple[int, int, int]] - Weighted edge list representation of the graph.
    Time Complexity: O(V^3) where V is the number of vertices.
    Space Complexity: O(V^2) where V is the number of vertices.
    Trick: Dynamic Programming approach to solve all pair shortest paths.
    """
    distances = defaultdict(lambda: float('inf'))

    for u, v, weight in graph:
        distances[(u, v)] = weight

    for k in range(len(distances)):
        for i in range(len(distances)):
            for j in range(len(distances)):
                distances[(i, j)] = min(distances[(i, j)], distances[(i, k)] + distances[(k, j)])

    return distances

# Cycle Detection in Undirected Graph (Using Union Find)
def has_cycle(graph: List[Tuple[int, int]]) -> bool:
    """
    Cycle detection algorithm to detect cycles in an undirected graph.

    Assumption: The graph is undirected.
    Type Annotation:
        graph: List[Tuple[int, int]] - Edge list representation of the graph.
    Time Complexity: O(E * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use Union-Find data structure to detect cycles.
    """
    uf = UnionFind(len(graph))
    for u, v in graph:
        if uf.find(u) == uf.find(v):
            return True
        uf.union(u, v)
    return False

# Cut Vertex (Articulation Point) Detection
def find_cut_vertices(graph: List[Tuple[int, int]]) -> Set[int]:
    """
    Cut vertex (articulation point) detection algorithm to find the vertices whose removal would increase the number of connected components.

    Assumption: The graph is undirected.
    Type Annotation:
        graph: List[Tuple[int, int]] - Edge list representation of the graph.
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

        for neighbor in adj_list[node]:
            if neighbor != parent:
                if neighbor not in visited:
                    children += 1
                    dfs(neighbor, node, visited, disc, low, result)
                    low[node] = min(low[node], low[neighbor])

                    if parent is None and children > 1:
                        result.add(node)
                    elif parent is not None and low[neighbor] >= disc[node]:
                        result.add(node)
                else:
                    low[node] = min(low[node], disc[neighbor])

    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()
    disc = {}
    low = {}
    result = set()
    time = [0]

    for node in adj_list:
        if node not in visited:
            dfs(node, None, visited, disc, low, result)

    return result

# Example usage:

# Constructing a graph
graph_edge_list = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)
]

# DFS example usage
print("DFS traversal:", dfs(graph_edge_list, 0))

# BFS example usage
print("BFS traversal:", bfs(graph_edge_list, 0))

# Topological Sort example usage
print("Topological Sort:", topological_sort(graph_edge_list))

# Dijkstra's Algorithm example usage
weighted_graph_edge_list = [
    (0, 1, 4), (0, 2, 3), (1, 3, 2), (2, 1, 1), (2, 3, 5)
]
print("Dijkstra's shortest paths:", dijkstra(weighted_graph_edge_list, 0))

# Prim's Algorithm example usage
print("Prim's Minimum Spanning Tree:", prim(weighted_graph_edge_list))

# Kruskal's Algorithm example usage
print("Kruskal's Minimum Spanning Tree:", kruskal(weighted_graph_edge_list))

# Bellman-Ford Algorithm example usage
weighted_graph_edge_list_negative = [
    (0, 1, 4), (0, 2, 3), (1, 3, -2), (2, 1, 1), (2, 3, 5)
]
print("Bellman-Ford shortest paths:", bellman_ford(weighted_graph_edge_list_negative, 0))

# Floyd-Warshall Algorithm example usage
weighted_graph_edge_list_all_pairs = [
    (0, 1, 4), (0, 2, 3), (1, 3, 2), (2, 1, 1), (2, 3, 5)
]
print("Floyd-Warshall all pair shortest paths:", floyd_warshall(weighted_graph_edge_list_all_pairs))

# Cycle Detection example usage
print("Graph has cycle:", has_cycle(graph_edge_list))

# Cut Vertex Detection example usage
print("Cut vertices:", find_cut_vertices(graph_edge_list))
