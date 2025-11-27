from typing import Generic, TypeVar, List, Tuple, Optional
import copy
from GraphExceptions import (
    VertexNotFoundError,
    EdgeNotFoundError,
    DuplicateVertexError,
    DuplicateEdgeError,
    ImmutableObjectException
)
from iterators.ForwardIterator import ForwardIterator
from iterators.BackwardIterator import BackwardIterator
from iterators.ImmutableForwardIterator import ImmutableForwardIterator
from iterators.ImmutableBackwardIterator import ImmutableBackwardIterator
from ImmutableWrapper import ImmutableWrapper
from graph.GraphVertex import GraphVertex
from graph.GraphConnection import GraphConnection
from graph.GraphNode import GraphNode
from graph.AdjacencyManager import AdjacencyManager
from graph.MatrixManager import MatrixManager

T = TypeVar("T")
P = TypeVar("P")


class UndirectedGraph(Generic[T, P]):
    """
    Неориентированный граф с модифицированной структурой Вирта
    Комбинация матрицы смежности и двусвязных списков смежности
    """

    def __init__(self):
        self._vertex_list: List[Optional[GraphVertex[T, P]]] = []
        self._vertex_lookup: dict[T, int] = {}
        self._connection_list: List[GraphConnection[T, P]] = []
        self._matrix_handler = MatrixManager[T, P]()
        self._adjacency_handler = AdjacencyManager[T, P]()

    def _create_immutable(self, obj):
        """Создает неизменяемую обертку для объекта"""
        immutable_types = (int, float, str, bytes, tuple, frozenset, bool)
        return obj if isinstance(obj, immutable_types) else ImmutableWrapper(obj)

    def _locate_vertex_index(self, value: T) -> int:
        """Находит индекс вершины по значению"""
        if value not in self._vertex_lookup:
            raise VertexNotFoundError(f"Вершина '{value}' отсутствует в графе")
        return self._vertex_lookup[value]

    def _get_vertex_by_index(self, index: int) -> GraphVertex[T, P]:
        """Получает вершину по индексу"""
        if index < 0 or index >= len(self._vertex_list) or self._vertex_list[index] is None:
            raise VertexNotFoundError(f"Вершина с индексом {index} не найдена")
        return self._vertex_list[index]

    def vertex_exists(self, value: T) -> bool:
        """Проверяет существование вершины"""
        return value in self._vertex_lookup

    def connection_exists(self, value1: T, value2: T) -> bool:
        """Проверяет существование связи между вершинами"""
        if not self.vertex_exists(value1) or not self.vertex_exists(value2):
            return False
        idx1 = self._locate_vertex_index(value1)
        idx2 = self._locate_vertex_index(value2)
        return self._matrix_handler.get_connection(idx1, idx2) is not None

    def is_graph_empty(self) -> bool:
        """Проверяет пустоту графа"""
        return len([v for v in self._vertex_list if v is not None]) == 0

    def get_vertex_count(self) -> int:
        """Возвращает количество вершин"""
        return len([v for v in self._vertex_list if v is not None])

    def get_connection_count(self) -> int:
        """Возвращает количество связей"""
        return len(self._connection_list)

    def clear_graph(self) -> None:
        """Очищает граф"""
        self._vertex_list.clear()
        self._vertex_lookup.clear()
        self._connection_list.clear()
        self._matrix_handler = MatrixManager[T, P]()

    def calculate_vertex_degree(self, value: T) -> int:
        """Вычисляет степень вершины"""
        vertex = self._get_vertex_by_index(self._locate_vertex_index(value))
        return self._adjacency_handler.count_connections(vertex)

    def calculate_connection_degree(self, value1: T, value2: T) -> int:
        """Вычисляет степень связи (в неориентированном графе всегда 2)"""
        if not self.connection_exists(value1, value2):
            raise EdgeNotFoundError("Связь между вершинами не найдена")
        return 2

    def get_adjacent_vertices(self, value: T) -> List[GraphVertex[T, P]]:
        """Возвращает список смежных вершин"""
        vertex = self._get_vertex_by_index(self._locate_vertex_index(value))
        return self._adjacency_handler.get_connected_vertices(vertex)

    def get_incident_connections(self, value: T) -> List[GraphConnection[T, P]]:
        """Возвращает список инцидентных связей"""
        vertex = self._get_vertex_by_index(self._locate_vertex_index(value))
        result = []
        current = vertex.first_connection
        while current:
            # Находим соответствующую связь
            for conn in self._connection_list:
                if (conn.source_node == current or conn.target_node == current):
                    result.append(conn)
                    break
            current = current.next_node
        return result

    def get_all_connections(self) -> List[Tuple[T, T]]:
        """Возвращает список всех связей"""
        return [(conn.source_vertex.value, conn.target_vertex.value) for conn in self._connection_list]

    def insert_vertex(self, value: T, properties: P) -> GraphVertex[T, P]:
        """Добавляет новую вершину"""
        if self.vertex_exists(value):
            raise DuplicateVertexError(f"Вершина '{value}' уже существует")

        index = self._matrix_handler.get_available_index()

        if index == len(self._vertex_list):
            self._vertex_list.append(None)
            self._matrix_handler.expand_matrix(len(self._vertex_list))

        vertex = GraphVertex(value, properties, index)
        self._vertex_list[index] = vertex
        self._vertex_lookup[value] = index
        return vertex

    def create_connection(self, value1: T, value2: T, attributes=None) -> GraphConnection[T, P]:
        """Создает связь между вершинами"""
        if not self.vertex_exists(value1) or not self.vertex_exists(value2):
            raise VertexNotFoundError("Одна или обе вершины не существуют")

        if self.connection_exists(value1, value2):
            raise DuplicateEdgeError(f"Связь между '{value1}' и '{value2}' уже существует")

        idx1 = self._locate_vertex_index(value1)
        idx2 = self._locate_vertex_index(value2)
        vertex1 = self._vertex_list[idx1]
        vertex2 = self._vertex_list[idx2]

        # Создаем узлы для обеих вершин
        node1 = GraphNode(vertex2, idx1, idx2)
        node2 = GraphNode(vertex1, idx1, idx2)

        # Добавляем в списки смежности
        self._adjacency_handler.add_connection(vertex1, node1)
        self._adjacency_handler.add_connection(vertex2, node2)

        # Сохраняем в матрице
        self._matrix_handler.set_connection(idx1, idx2, node1)

        # Создаем связь
        connection = GraphConnection(vertex1, vertex2, node1, node2, attributes)
        self._connection_list.append(connection)

        return connection

    def remove_connection(self, value1: T, value2: T):
        """Удаляет связь между вершинами"""
        if not self.connection_exists(value1, value2):
            raise EdgeNotFoundError(f"Связи между '{value1}' и '{value2}' не существует")

        idx1 = self._locate_vertex_index(value1)
        idx2 = self._locate_vertex_index(value2)
        vertex1 = self._vertex_list[idx1]
        vertex2 = self._vertex_list[idx2]

        # Находим связь для удаления
        connection_to_remove = None
        for conn in self._connection_list:
            if (conn.source_vertex == vertex1 and conn.target_vertex == vertex2) or \
                    (conn.source_vertex == vertex2 and conn.target_vertex == vertex1):
                connection_to_remove = conn
                break

        if connection_to_remove:
            # Удаляем из списков смежности
            self._adjacency_handler.remove_connection(vertex1, connection_to_remove.source_node)
            self._adjacency_handler.remove_connection(vertex2, connection_to_remove.target_node)

            # Удаляем из матрицы
            self._matrix_handler.remove_connection(idx1, idx2)

            # Удаляем из списка связей
            self._connection_list.remove(connection_to_remove)

    def delete_vertex(self, value: T):
        """Удаляет вершину"""
        if not self.vertex_exists(value):
            raise VertexNotFoundError(f"Вершина '{value}' не существует")

        idx = self._locate_vertex_index(value)
        vertex = self._vertex_list[idx]

        # Собираем все инцидентные связи для удаления
        connections_to_remove = []
        current = vertex.first_connection
        while current:
            for conn in self._connection_list:
                if (conn.source_node == current or conn.target_node == current) and conn not in connections_to_remove:
                    connections_to_remove.append(conn)
                    break
            current = current.next_node

        # Удаляем все инцидентные связи
        for conn in connections_to_remove:
            other_vertex = conn.source_vertex if conn.source_vertex != vertex else conn.target_vertex
            self.remove_connection(vertex.value, other_vertex.value)

        # Удаляем вершину
        self._vertex_list[idx] = None
        del self._vertex_lookup[value]
        self._matrix_handler.release_index(idx)

    # Методы итераторов
    def vertex_iterator(self):
        """Итератор по вершинам"""
        active_vertices = [v for v in self._vertex_list if v is not None]
        return ForwardIterator(active_vertices)

    def reverse_vertex_iterator(self):
        """Обратный итератор по вершинам"""
        active_vertices = [v for v in self._vertex_list if v is not None]
        return BackwardIterator(active_vertices)

    def immutable_vertex_iterator(self):
        """Неизменяемый итератор по вершинам"""
        active_vertices = [v for v in self._vertex_list if v is not None]
        return ImmutableForwardIterator([self._create_immutable(v) for v in active_vertices])

    def connection_iterator(self):
        """Итератор по связям"""
        return ForwardIterator(self._connection_list[:])

    def reverse_connection_iterator(self):
        """Обратный итератор по связям"""
        return BackwardIterator(self._connection_list[:])

    def immutable_connection_iterator(self):
        """Неизменяемый итератор по связям"""
        return ImmutableForwardIterator([self._create_immutable(c) for c in self._connection_list])

    def incident_connection_iterator(self, value: T):
        """Итератор по инцидентным связям"""
        return ForwardIterator(self.get_incident_connections(value))

    def adjacent_vertex_iterator(self, value: T):
        """Итератор по смежным вершинам"""
        return ForwardIterator(self.get_adjacent_vertices(value))

    def immutable_reverse_vertex_iterator(self, start_position: int | None = None):
        """Неизменяемый обратный итератор по вершинам"""
        active_vertices = [v for v in self._vertex_list if v is not None]
        items = [self._create_immutable(v) for v in active_vertices]
        return ImmutableBackwardIterator(items, start_position)

    def immutable_reverse_connection_iterator(self, start_position: int | None = None):
        """Неизменяемый обратный итератор по связям"""
        items = [self._create_immutable(c) for c in self._connection_list]
        return ImmutableBackwardIterator(items, start_position)

    def immutable_reverse_adjacent_vertex_iterator(self, value: T, start_position: int | None = None):
        """Неизменяемый обратный итератор по смежным вершинам"""
        vertices = self.get_adjacent_vertices(value)
        items = [self._create_immutable(v) for v in vertices]
        return ImmutableBackwardIterator(items, start_position)

    def immutable_reverse_incident_connection_iterator(self, value: T, start_position: int | None = None):
        """Неизменяемый обратный итератор по инцидентным связям"""
        connections = self.get_incident_connections(value)
        items = [self._create_immutable(c) for c in connections]
        return ImmutableBackwardIterator(items, start_position)

    def delete_vertex_via_iterator(self, iterator):
        """Удаляет вершину через итератор"""
        vertex = iterator._collection[iterator.position]
        if isinstance(vertex, ImmutableWrapper):
            vertex = vertex._content
        self.delete_vertex(vertex.value)

    def delete_connection_via_iterator(self, iterator):
        """Удаляет связь через итератор"""
        connection = iterator._collection[iterator.position]
        if isinstance(connection, ImmutableWrapper):
            connection = connection._content
        self.remove_connection(connection.source_vertex.value, connection.target_vertex.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UndirectedGraph):
            return False
        return (set(self._vertex_lookup.keys()) == set(other._vertex_lookup.keys()) and
                set(self.get_all_connections()) == set(other.get_all_connections()))

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, UndirectedGraph):
            return False
        return self.get_connection_count() < other.get_connection_count()

    def __deepcopy__(self, memo):
        new_graph = UndirectedGraph[T, P]()

        # Копируем вершины
        for vertex in self._vertex_list:
            if vertex is not None:
                new_graph.insert_vertex(copy.deepcopy(vertex.value), copy.deepcopy(vertex.properties))

        # Копируем связи
        for connection in self._connection_list:
            new_graph.create_connection(
                copy.deepcopy(connection.source_vertex.value),
                copy.deepcopy(connection.target_vertex.value),
                copy.deepcopy(connection.attributes)
            )

        return new_graph

    def __str__(self):
        vertices = ", ".join(str(v.value) for v in self._vertex_list if v is not None)
        connections = ", ".join(f"({c[0]},{c[1]})" for c in self.get_all_connections())
        return f"UndirectedGraph(vertices=[{vertices}], connections=[{connections}])"

    def __repr__(self):
        return f"UndirectedGraph(vertices={self.get_vertex_count()}, connections={self.get_connection_count()})"

    def delete_vertex_via_iterator(self, iterator):
        """Удаляет вершину через итератор"""
        if hasattr(iterator, '_collection') and hasattr(iterator, 'position'):
            vertex = iterator._collection[iterator.position]
            if isinstance(vertex, ImmutableWrapper):
                vertex = vertex._content
            self.delete_vertex(vertex.value)
        else:
            raise VertexNotFoundError("Некорректный итератор")

    def delete_connection_via_iterator(self, iterator):
        """Удаляет связь через итератор"""
        if hasattr(iterator, '_collection') and hasattr(iterator, 'position'):
            connection = iterator._collection[iterator.position]
            if isinstance(connection, ImmutableWrapper):
                connection = connection._content
            self.remove_connection(connection.source_vertex.value, connection.target_vertex.value)
        else:
            raise EdgeNotFoundError("Некорректный итератор")