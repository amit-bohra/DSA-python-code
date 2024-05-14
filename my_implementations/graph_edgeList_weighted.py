from collections import deque
from typing import List, Tuple


class Graph:
    def __init__(self) -> None:
        self.edges: List[Tuple[int, int, int]] = []

    # Function to insert a new edge between two vertices with weight
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert_edge(self, source: int, destination: int, weight: int) -> None:
        """
        Inserts a new edge between two vertices in the graph.

        Trick: Add the edge tuple (source, destination, weight) to the list of edges.

        Example Usage: Used to add a new edge between two vertices in the graph.
        """
        self.edges.append((source, destination, weight))

    # Function to delete an edge between two vertices
    # Time Complexity: O(E), where E is the number of edges
    # Space Complexity: O(1)
    def delete_edge(self, source: int, destination: int) -> None:
        """
        Deletes an edge between two vertices in the graph.

        Trick: Remove the edge tuple (source, destination, weight) from the list of edges.

        Example Usage: Used to remove an edge between two vertices in the graph.
        """
        self.edges = [(s, d, w) for s, d, w in self.edges if (s, d) != (source, destination)]

    # Function for breadth-first search (BFS) traversal of the graph
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(V)
    def bfs(self, start_vertex: int) -> List[int]:
        """
        Performs breadth-first search (BFS) traversal of the graph starting from a given vertex.

        Trick: Use a queue to traverse the graph level by level, visiting all neighbors of each vertex before moving to the next level.

        Example Usage: Used to traverse the graph in breadth-first order starting from a specific vertex.
        """
        num_vertices = max(max(self.edges, key=lambda x: max(x[:-1]))[:-1]) + 1
        visited: List[bool] = [False] * num_vertices
        result: List[int] = []
        queue: deque[int] = deque([start_vertex])

        while queue:
            vertex: int = queue.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                for source, destination, _ in self.edges:
                    if source == vertex:
                        queue.append(destination)

        return result

    # Function for depth-first search (DFS) traversal of the graph
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(V)
    def dfs(self, start_vertex: int) -> List[int]:
        """
        Performs depth-first search (DFS) traversal of the graph starting from a given vertex.

        Trick: Use recursion to explore as far as possible along each branch before backtracking.

        Example Usage: Used to traverse the graph in depth-first order starting from a specific vertex.
        """
        num_vertices = max(max(self.edges, key=lambda x: max(x[:-1]))[:-1]) + 1
        visited: List[bool] = [False] * num_vertices
        result: List[int] = []

        def dfs_util(vertex: int) -> None:
            visited[vertex] = True
            result.append(vertex)
            for source, destination, _ in self.edges:
                if source == vertex and not visited[destination]:
                    dfs_util(destination)

        dfs_util(start_vertex)
        return result


# Example usage:
if __name__ == "__main__":
    # Create a new graph
    graph: Graph = Graph()

    # Insert edges into the graph with weights
    graph.insert_edge(0, 1, 1)
    graph.insert_edge(0, 2, 2)
    graph.insert_edge(1, 3, 3)
    graph.insert_edge(2, 4, 4)

    # Perform breadth-first search (BFS) traversal
    print("BFS Traversal:")
    # Expected output: [0, 1, 2, 3, 4]
    print(graph.bfs(0))

    # Perform depth-first search (DFS) traversal
    print("\nDFS Traversal:")
    # Expected output: [0, 1, 3, 2, 4]
    print(graph.dfs(0))

    # Delete edge (2, 4) from the graph
    graph.delete_edge(2, 4)

    # Perform breadth-first search (BFS) traversal after deletion
    print("\nBFS Traversal after deleting edge (2, 4):")
    # Expected output: [0, 1, 2, 3]
    print(graph.bfs(0))
