from collections import defaultdict, deque
import heapq
from typing import List, Dict, Set

class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

# Depth First Search (DFS) Algorithm
def dfs(node: Node) -> List[int]:
    """
    DFS algorithm to traverse a graph starting from a given node.

    Assumption: The graph is represented using a linked list with single references to neighbors.
    Type Annotation:
        node: Node - Starting node for DFS traversal.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use a stack (or recursion) to keep track of nodes to visit.
    """
    visited = set()
    traversal_order = []
    stack = [node]

    while stack:
        current = stack.pop()
        if current.val not in visited:
            visited.add(current.val)
            traversal_order.append(current.val)
            for neighbor in reversed(current.neighbors):
                if neighbor.val not in visited:
                    stack.append(neighbor)

    return traversal_order

# Breadth First Search (BFS) Algorithm
def bfs(node: Node) -> List[int]:
    """
    BFS algorithm to traverse a graph starting from a given node.

    Assumption: The graph is represented using a linked list with single references to neighbors.
    Type Annotation:
        node: Node - Starting node for BFS traversal.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use a deque to keep track of nodes to visit.
    """
    visited = set()
    traversal_order = []
    queue = deque([node])

    while queue:
        current = queue.popleft()
        if current.val not in visited:
            visited.add(current.val)
            traversal_order.append(current.val)
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

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
def topological_sort(node: Node) -> List[int]:
    """
    Topological sort algorithm to find the linear ordering of vertices in a directed acyclic graph (DAG).

    Assumption: The graph is a directed acyclic graph (DAG).
    Type Annotation:
        node: Node - Starting node for topological sort.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use DFS and stack to order the vertices.
    """
    visited = set()
    stack = []

    def dfs(current):
        visited.add(current.val)
        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                dfs(neighbor)
        stack.append(current.val)

    dfs(node)
    return stack[::-1]

# Dijkstra's Algorithm
def dijkstra(graph: Dict[int, Node], start: int) -> Dict[int, int]:
    """
    Dijkstra's algorithm to find the shortest paths from a single source node to all other nodes in a graph.

    Assumption: The graph is weighted and does not contain negative edge weights.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
        start: int - Starting node for Dijkstra's algorithm.
    Time Complexity: O((V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use priority queue (heapq) to efficiently select the next vertex with the smallest distance.
    """
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, current = heapq.heappop(pq)
        if dist > distances[current]:
            continue
        for neighbor in current.neighbors:
            new_dist = dist + neighbor.weight
            if new_dist < distances[neighbor.val]:
                distances[neighbor.val] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

# Prim's Algorithm
def prim(graph: Dict[int, Node]) -> Dict[int, int]:
    """
    Prim's algorithm to find the minimum spanning tree (MST) of a connected, undirected graph.

    Assumption: The graph is connected and undirected.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
    Time Complexity: O((V + E) * log(V)) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use priority queue (heapq) to efficiently select the next edge with the smallest weight.
    """
    visited = set()
    mst = {}
    pq = [(0, None, graph[next(iter(graph))])]  # Start from any node

    while pq:
        weight, parent, current = heapq.heappop(pq)
        if current not in visited:
            visited.add(current)
            if parent:
                mst[current.val] = weight
            for neighbor in current.neighbors:
                heapq.heappush(pq, (neighbor.weight, current, neighbor))

    return mst

# Kruskal's Algorithm
def kruskal(graph: Dict[int, Node]) -> Dict[int, int]:
    """
    Kruskal's algorithm to find the minimum spanning tree (MST) of a connected, undirected graph.

    Assumption: The graph is connected and undirected.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
    Time Complexity: O(E * log(E)) where E is the number of edges.
    Space Complexity: O(E) where E is the number of edges.
    Trick: Use Union-Find data structure to efficiently detect cycles while selecting edges.
    """
    def find(node):
        if node.parent != node:
            node.parent = find(node.parent)
        return node.parent

    class Edge:
        def __init__(self, src, dest, weight):
            self.src = src
            self.dest = dest
            self.weight = weight

    edges = []
    for src, node in graph.items():
        for neighbor in node.neighbors:
            edges.append(Edge(src, neighbor.val, neighbor.weight))

    edges.sort(key=lambda edge: edge.weight)
    mst = {}
    uf = {}

    for src, node in graph.items():
        uf[src] = node

    for edge in edges:
        src_parent = find(uf[edge.src])
        dest_parent = find(uf[edge.dest])
        if src_parent != dest_parent:
            mst[edge.dest] = edge.weight
            src_parent.parent = dest_parent

    return mst

# Bellman-Ford Algorithm
def bellman_ford(graph: Dict[int, Node], start: int) -> Dict[int, int]:
    """
    Bellman-Ford algorithm to find the shortest paths from a single source node to all other nodes in a graph.

    Assumption: The graph may contain negative edge weights but should not contain negative cycles.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
        start: int - Starting node for Bellman-Ford algorithm.
    Time Complexity: O(V * E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Relax edges repeatedly to find the shortest paths.
    """
    vertices = list(graph.keys())
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for src in vertices:
            for neighbor in graph[src].neighbors:
                if distances[src] + neighbor.weight < distances[neighbor.val]:
                    distances[neighbor.val] = distances[src] + neighbor.weight

    return distances

# Floyd-Warshall Algorithm
def floyd_warshall(graph: Dict[int, Node]) -> Dict[Tuple[int, int], int]:
    """
    Floyd-Warshall algorithm to find all pair shortest paths in a weighted graph.

    Assumption: The graph may contain negative edge weights but should not contain negative cycles.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
    Time Complexity: O(V^3) where V is the number of vertices.
    Space Complexity: O(V^2) where V is the number of vertices.
    Trick: Dynamic Programming approach to solve all pair shortest paths.
    """
    vertices = list(graph.keys())
    n = len(vertices)
    distances = {(u, v): float('inf') for u in vertices for v in vertices}
    
    for u in vertices:
        for neighbor in graph[u].neighbors:
            distances[(u, neighbor.val)] = neighbor.weight
    
    for k in vertices:
        for i in vertices:
            for j in vertices:
                distances[(i, j)] = min(distances[(i, j)], distances[(i, k)] + distances[(k, j)])
    
    return distances

# Cycle Detection in Undirected Graph (Using Union Find)
def has_cycle(graph: Dict[int, Node]) -> bool:
    """
    Cycle detection algorithm to detect cycles in an undirected graph.

    Assumption: The graph is undirected.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) where V is the number of vertices.
    Trick: Use Union-Find data structure to detect cycles.
    """
    def find(node):
        if node.parent != node:
            node.parent = find(node.parent)
        return node.parent

    class Edge:
        def __init__(self, src, dest):
            self.src = src
            self.dest = dest

    edges = []
    for src, node in graph.items():
        for neighbor in node.neighbors:
            edges.append(Edge(src, neighbor.val))

    uf = {}

    for src, node in graph.items():
        uf[src] = node

    for edge in edges:
        src_parent = find(uf[edge.src])
        dest_parent = find(uf[edge.dest])
        if src_parent == dest_parent:
            return True
        uf[edge.src].parent = uf[edge.dest]

    return False

# Cut Vertex (Articulation Point) Detection
def find_cut_vertices(graph: Dict[int, Node]) -> Set[int]:
    """
    Cut vertex (articulation point) detection algorithm to find the vertices whose removal would increase the number of connected components.

    Assumption: The graph is undirected.
    Type Annotation:
        graph: Dict[int, Node] - Dictionary representing the graph with integer keys and Node values.
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

        for neighbor in node.neighbors:
            if neighbor.val != parent:
                if neighbor not in visited:
                    children += 1
                    dfs(neighbor, node, visited, disc, low, result)
                    low[node] = min(low[node], low[neighbor])
                    if parent is None and children > 1:
                        result.add(node.val)
                    elif parent is not None and low[neighbor] >= disc[node]:
                        result.add(node.val)
                else:
                    low[node] = min(low[node], disc[neighbor])

    visited = set()
    disc = {}
    low = {}
    result = set()
    time = [0]

    for node in graph.values():
        if node not in visited:
            dfs(node, None, visited, disc, low, result)

    return result

# Example usage:

# Constructing a graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3, node4]
node3.neighbors = [node1, node2]
node4.neighbors = [node2]

graph = {1: node1, 2: node2, 3: node3, 4: node4}

# DFS example usage
print("DFS traversal:", dfs(node1))

# BFS example usage
print("BFS traversal:", bfs(node1))

# Topological Sort example usage
print("Topological Sort:", topological_sort(node1))

# Dijkstra's Algorithm example usage
node1.neighbors[0].weight = 4
node1.neighbors[1].weight = 3
node2.neighbors[2].weight = 2
node2.neighbors[1].weight = 1
node3.neighbors[0].weight = 5
print("Dijkstra's shortest paths:", dijkstra(graph, 1))

# Prim's Algorithm example usage
print("Prim's Minimum Spanning Tree:", prim(graph))

# Kruskal's Algorithm example usage
print("Kruskal's Minimum Spanning Tree:", kruskal(graph))

# Bellman-Ford Algorithm example usage
node1.neighbors[0].weight = 4
node1.neighbors[1].weight = 3
node2.neighbors[2].weight = -2
node2.neighbors[1].weight = 1
node3.neighbors[0].weight = 5
print("Bellman-Ford shortest paths:", bellman_ford(graph, 1))

# Floyd-Warshall Algorithm example usage
print("Floyd-Warshall all pair shortest paths:", floyd_warshall(graph))

# Cycle Detection example usage
print("Graph has cycle:", has_cycle(graph))

# Cut Vertex Detection example usage
print("Cut vertices:", find_cut_vertices(graph))
