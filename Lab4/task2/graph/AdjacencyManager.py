from typing import Generic, TypeVar, Optional
from graph.GraphVertex import GraphVertex
from graph.GraphNode import GraphNode

T = TypeVar("T")
P = TypeVar("P")


class AdjacencyManager(Generic[T, P]):
    """Управление списками смежности для вершин"""

    @staticmethod
    def add_connection(vertex: GraphVertex[T, P], node: GraphNode[T, P]):
        """Добавляет узел в начало списка смежности вершины"""
        if vertex.first_connection:
            vertex.first_connection.prev_node = node
            node.next_node = vertex.first_connection
        vertex.first_connection = node

    @staticmethod
    def remove_connection(vertex: GraphVertex[T, P], node: GraphNode[T, P]):
        """Удаляет узел из списка смежности вершины"""
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            vertex.first_connection = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node

    @staticmethod
    def get_connected_vertices(vertex: GraphVertex[T, P]) -> list[GraphVertex[T, P]]:
        """Возвращает список смежных вершин"""
        result = []
        current = vertex.first_connection
        while current:
            result.append(current.connected_vertex)
            current = current.next_node
        return result

    @staticmethod
    def count_connections(vertex: GraphVertex[T, P]) -> int:
        """Подсчитывает количество смежных вершин"""
        count = 0
        current = vertex.first_connection
        while current:
            count += 1
            current = current.next_node
        return count