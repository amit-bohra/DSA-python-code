from collections import deque
from typing import List, Optional


class Graph:
    def __init__(self) -> None:
        self.adj_matrix: List[List[int]] = []

    # Function to insert a new edge between two vertices
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert_edge(self, source: int, destination: int) -> None:
        """
        Inserts a new edge between two vertices in the graph.

        Trick: Set the corresponding cell in the adjacency matrix to represent the edge.

        Example Usage: Used to add a new edge between two vertices in the graph.
        """
        max_vertex = max(source, destination)
        if max_vertex >= len(self.adj_matrix):
            # Expand the adjacency matrix if necessary
            self.expand_adj_matrix(max_vertex + 1)
        self.adj_matrix[source][destination] = 1
        self.adj_matrix[destination][source] = 1  # For undirected graph

    # Function to expand the adjacency matrix to accommodate more vertices
    # Time Complexity: O(V^2), where V is the number of vertices
    # Space Complexity: O(V^2)
    def expand_adj_matrix(self, new_size: int) -> None:
        """
        Expands the adjacency matrix to accommodate more vertices.

        Trick: Create a new adjacency matrix with the new size and copy existing values.

        Example Usage: Used internally to resize the adjacency matrix when needed.
        """
        old_size = len(self.adj_matrix)
        new_adj_matrix = [[0] * new_size for _ in range(new_size)]
        for i in range(old_size):
            for j in range(old_size):
                new_adj_matrix[i][j] = self.adj_matrix[i][j]
        self.adj_matrix = new_adj_matrix

    # Function to delete an edge between two vertices
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def delete_edge(self, source: int, destination: int) -> None:
        """
        Deletes an edge between two vertices in the graph.

        Trick: Set the corresponding cell in the adjacency matrix to 0 to delete the edge.

        Example Usage: Used to remove an edge between two vertices in the graph.
        """
        if 0 <= source < len(self.adj_matrix) and 0 <= destination < len(self.adj_matrix):
            self.adj_matrix[source][destination] = 0
            self.adj_matrix[destination][source] = 0  # For undirected graph

    # Function for breadth-first search (BFS) traversal of the graph
    # Time Complexity: O(V^2), where V is the number of vertices
    # Space Complexity: O(V)
    def bfs(self, start_vertex: int) -> List[int]:
        """
        Performs breadth-first search (BFS) traversal of the graph starting from a given vertex.

        Trick: Use a queue to traverse the graph level by level, visiting all neighbors of each vertex before moving to the next level.

        Example Usage: Used to traverse the graph in breadth-first order starting from a specific vertex.
        """
        num_vertices = len(self.adj_matrix)
        visited: List[bool] = [False] * num_vertices
        result: List[int] = []
        queue: deque[int] = deque([start_vertex])

        while queue:
            vertex: int = queue.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                for neighbor in range(num_vertices):
                    if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)

        return result

    # Function for depth-first search (DFS) traversal of the graph
    # Time Complexity: O(V^2), where V is the number of vertices
    # Space Complexity: O(V)
    def dfs(self, start_vertex: int) -> List[int]:
        """
        Performs depth-first search (DFS) traversal of the graph starting from a given vertex.

        Trick: Use recursion to explore as far as possible along each branch before backtracking.

        Example Usage: Used to traverse the graph in depth-first order starting from a specific vertex.
        """
        num_vertices = len(self.adj_matrix)
        visited: List[bool] = [False] * num_vertices
        result: List[int] = []

        def dfs_util(vertex: int) -> None:
            visited[vertex] = True
            result.append(vertex)
            for neighbor in range(num_vertices):
                if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start_vertex)
        return result


# Example usage:
if __name__ == "__main__":
    # Create a new graph
    graph: Graph = Graph()

    # Insert edges into the graph
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 4)

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
