from collections import deque
from typing import List, Dict, Set, Optional


class Graph:
    def __init__(self) -> None:
        self.adj_list: Dict[int, List[int]] = {}

    # Function to insert a new vertex into the graph
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert_vertex(self, vertex: int) -> None:
        """
        Inserts a new vertex into the graph.

        Trick: Simply add the new vertex to the adjacency list with an empty list of neighbors.

        Example Usage: Used to add a new vertex to the graph.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    # Function to insert a new edge between two vertices
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert_edge(self, source: int, destination: int) -> None:
        """
        Inserts a new edge between two vertices in the graph.

        Trick: Add the destination vertex to the adjacency list of the source vertex to represent the edge.

        Example Usage: Used to add a new edge between two vertices in the graph.
        """
        if source in self.adj_list and destination in self.adj_list:
            self.adj_list[source].append(destination)

    # Function to delete a vertex from the graph
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(1)
    def delete_vertex(self, vertex: int) -> None:
        """
        Deletes a vertex from the graph along with all its incident edges.

        Trick: Remove the vertex from the adjacency list and iterate through the entire graph to remove any incident edges.

        Example Usage: Used to remove a vertex from the graph.
        """
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for vertices in self.adj_list.values():
                if vertex in vertices:
                    vertices.remove(vertex)

    # Function to delete an edge between two vertices
    # Time Complexity: O(V), where V is the number of vertices
    # Space Complexity: O(1)
    def delete_edge(self, source: int, destination: int) -> None:
        """
        Deletes an edge between two vertices in the graph.

        Trick: Remove the destination vertex from the adjacency list of the source vertex to delete the edge.

        Example Usage: Used to remove an edge between two vertices in the graph.
        """
        if source in self.adj_list and destination in self.adj_list:
            if destination in self.adj_list[source]:
                self.adj_list[source].remove(destination)

    # Function for breadth-first search (BFS) traversal of the graph
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(V)
    def bfs(self, start_vertex: int) -> List[int]:
        """
        Performs breadth-first search (BFS) traversal of the graph starting from a given vertex.

        Trick: Use a queue to traverse the graph level by level, visiting all neighbors of each vertex before moving to the next level.

        Example Usage: Used to traverse the graph in breadth-first order starting from a specific vertex.
        """
        visited: Set[int] = set()
        result: List[int] = []
        queue: deque[int] = deque([start_vertex])

        while queue:
            vertex: int = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

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
        visited: Set[int] = set()
        result: List[int] = []

        def dfs_util(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start_vertex)
        return result


# Example usage:
if __name__ == "__main__":
    # Create a new graph
    graph: Graph = Graph()

    # Insert vertices into the graph
    graph.insert_vertex(1)
    graph.insert_vertex(2)
    graph.insert_vertex(3)
    graph.insert_vertex(4)
    graph.insert_vertex(5)

    # Insert edges into the graph
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 4)
    graph.insert_edge(2, 5)

    # Perform breadth-first search (BFS) traversal
    print("BFS Traversal:")
    # Expected output: [1, 2, 3, 4, 5]
    print(graph.bfs(1))

    # Perform depth-first search (DFS) traversal
    print("\nDFS Traversal:")
    # Expected output: [1, 2, 4, 5, 3]
    print(graph.dfs(1))

    # Delete vertex 3 from the graph
    graph.delete_vertex(3)

    # Perform breadth-first search (BFS) traversal after deletion
    print("\nBFS Traversal after deleting vertex 3:")
    # Expected output: [1, 2, 4, 5]
    print(graph.bfs(1))
