from collections import deque
from typing import List, Optional


class GraphNode:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.neighbors: List['GraphNode'] = []
        self.weights: List[int] = []


class Graph:
    def __init__(self) -> None:
        pass

    # Function to insert a new node with a given value
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert_node(self, val: int) -> GraphNode:
        """
        Inserts a new node with a given value into the graph.

        Trick: Create a new GraphNode instance with the provided value.

        Example Usage: Used to add a new node to the graph.
        """
        return GraphNode(val)

    # Function to delete a node with a given value
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(1)
    def delete_node(self, node: GraphNode) -> None:
        """
        Deletes a node from the graph.

        Trick: Remove the node and remove any edges connected to this node.

        Example Usage: Used to remove a node from the graph.
        """
        if node is None:
            return

        # Remove any edges connected to this node
        for neighbor in node.neighbors:
            neighbor.neighbors.remove(node)

    # Function to insert an edge between two nodes with given values
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert_edge(self, node1: GraphNode, node2: GraphNode, weight: int = 1) -> None:
        """
        Inserts an edge between two nodes into the graph.

        Trick: Add references to each other in their neighbor lists.

        Example Usage: Used to add an edge between two nodes in the graph.
        """
        node1.neighbors.append(node2)
        node1.weights.append(weight)

    # Function to delete an edge between two nodes with given values
    # Time Complexity: O(V), where V is the number of vertices
    # Space Complexity: O(1)
    def delete_edge(self, node1: GraphNode, node2: GraphNode) -> None:
        """
        Deletes an edge between two nodes from the graph.

        Trick: Remove references to each other from their neighbor lists.

        Example Usage: Used to remove an edge between two nodes in the graph.
        """
        index = node1.neighbors.index(node2)
        del node1.neighbors[index]
        del node1.weights[index]

    # Function for breadth-first search (BFS) traversal of the graph
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(V)
    def bfs(self, start_node: GraphNode) -> List[int]:
        """
        Performs breadth-first search (BFS) traversal of the graph starting from a given node.

        Trick: Use a queue to traverse the graph level by level, visiting all neighbors of each node before moving to the next level.

        Example Usage: Used to traverse the graph in breadth-first order starting from a specific node.
        """
        visited: List[int] = []
        queue: deque[GraphNode] = deque()

        queue.append(start_node)

        while queue:
            node: GraphNode = queue.popleft()
            if node.val not in visited:
                visited.append(node.val)
                for neighbor in node.neighbors:
                    queue.append(neighbor)

        return visited

    # Function for depth-first search (DFS) traversal of the graph
    # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space Complexity: O(V)
    def dfs(self, start_node: GraphNode) -> List[int]:
        """
        Performs depth-first search (DFS) traversal of the graph starting from a given node.

        Trick: Use recursion to explore as far as possible along each branch before backtracking.

        Example Usage: Used to traverse the graph in depth-first order starting from a specific node.
        """
        visited: List[int] = []

        def dfs_util(node: GraphNode) -> None:
            if node.val not in visited:
                visited.append(node.val)
                for neighbor in node.neighbors:
                    dfs_util(neighbor)

        dfs_util(start_node)

        return visited


# Example usage:
if __name__ == "__main__":
    # Create a new graph
    graph: Graph = Graph()

    # Insert nodes into the graph
    node1 = graph.insert_node(1)
    node2 = graph.insert_node(2)
    node3 = graph.insert_node(3)
    node4 = graph.insert_node(4)

    # Insert edges into the graph
    graph.insert_edge(node1, node2)
    graph.insert_edge(node1, node3)
    graph.insert_edge(node2, node4)

    # Perform breadth-first search (BFS) traversal
    print("BFS Traversal:")
    # Expected output: [1, 2, 3, 4]
    print(graph.bfs(node1))

    # Perform depth-first search (DFS) traversal
    print("\nDFS Traversal:")
    # Expected output: [1, 2, 4, 3]
    print(graph.dfs(node1))
