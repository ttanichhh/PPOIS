"""операции со списками смежности (добавить/удалить узел, обойти соседей)."""

from typing import Generic, TypeVar, Optional
from graph.GraphVertex import GraphVertex
from graph.GraphNode import GraphNode

T = TypeVar("T")
P = TypeVar("P")


class AdjacencyManager(Generic[T, P]):
    """Управление списками смежности для вершин"""

    def add_connection(self, vertex: GraphVertex[T, P], node: GraphNode[T, P]):
        if vertex.first_connection:
            vertex.first_connection.prev_node = node
            node.next_node = vertex.first_connection
        vertex.first_connection = node

    def remove_connection(self, vertex: GraphVertex[T, P], node: GraphNode[T, P]):
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            vertex.first_connection = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node

    def get_connected_vertices(self, vertex: GraphVertex[T, P]) -> list[GraphVertex[T, P]]:
        result = []
        current = vertex.first_connection
        while current:
            result.append(current.connected_vertex)
            current = current.next_node
        return result

    def count_connections(self, vertex: GraphVertex[T, P]) -> int:
        count = 0
        current = vertex.first_connection
        while current:
            count += 1
            current = current.next_node
        return count
