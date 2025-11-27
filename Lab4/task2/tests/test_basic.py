import pytest
import sys
import os

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from UndirectedGraph import UndirectedGraph
from GraphExceptions import *


class TestUndirectedGraph:

    @pytest.fixture
    def graph(self):
        """Фикстура для создания тестового графа"""
        return UndirectedGraph[str, dict]()

    def test_basic_import(self):
        """Базовый тест импорта"""
        graph = UndirectedGraph[str, dict]()
        assert graph is not None

    def test_vertex_creation(self, graph):
        """Тест создания вершины"""
        vertex = graph.insert_vertex("A", {"color": "red"})
        assert vertex.value == "A"
        assert vertex.properties["color"] == "red"
        assert graph.get_vertex_count() == 1
        assert graph.vertex_exists("A") == True

    def test_duplicate_vertex(self, graph):
        """Тест дублирования вершины"""
        graph.insert_vertex("A", {})
        with pytest.raises(DuplicateVertexError):
            graph.insert_vertex("A", {})

    def test_edge_creation(self, graph):
        """Тест создания ребра"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        edge = graph.create_connection("A", "B", {"weight": 5})

        assert graph.get_connection_count() == 1
        assert graph.connection_exists("A", "B") == True
        assert graph.connection_exists("B", "A") == True
        assert edge.attributes["weight"] == 5

    def test_duplicate_edge(self, graph):
        """Тест дублирования ребра"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.create_connection("A", "B", {})

        with pytest.raises(DuplicateEdgeError):
            graph.create_connection("A", "B", {})

    def test_edge_nonexistent_vertex(self, graph):
        """Тест создания ребра с несуществующей вершиной"""
        graph.insert_vertex("A", {})
        with pytest.raises(VertexNotFoundError):
            graph.create_connection("A", "B", {})

    def test_vertex_removal(self, graph):
        """Тест удаления вершины"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("B", "C", {})

        graph.delete_vertex("B")

        assert graph.get_vertex_count() == 2
        assert graph.vertex_exists("B") == False
        assert graph.get_connection_count() == 0

    def test_edge_removal(self, graph):
        """Тест удаления ребра"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.create_connection("A", "B", {})

        graph.remove_connection("A", "B")

        assert graph.get_connection_count() == 0
        assert graph.connection_exists("A", "B") == False

    def test_nonexistent_vertex_removal(self, graph):
        """Тест удаления несуществующей вершины"""
        with pytest.raises(VertexNotFoundError):
            graph.delete_vertex("X")

    def test_nonexistent_edge_removal(self, graph):
        """Тест удаления несуществующего ребра"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        with pytest.raises(EdgeNotFoundError):
            graph.remove_connection("A", "B")

    def test_vertex_degree(self, graph):
        """Тест вычисления степени вершины"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("A", "C", {})

        assert graph.calculate_vertex_degree("A") == 2
        assert graph.calculate_vertex_degree("B") == 1
        assert graph.calculate_vertex_degree("C") == 1

    def test_nonexistent_vertex_degree(self, graph):
        """Тест степени несуществующей вершины"""
        with pytest.raises(VertexNotFoundError):
            graph.calculate_vertex_degree("X")

    def test_edge_degree(self, graph):
        """Тест вычисления степени ребра"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.create_connection("A", "B", {})

        assert graph.calculate_connection_degree("A", "B") == 2

    def test_nonexistent_edge_degree(self, graph):
        """Тест степени несуществующего ребра"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        with pytest.raises(EdgeNotFoundError):
            graph.calculate_connection_degree("A", "B")

    def test_adjacent_vertices(self, graph):
        """Тест получения смежных вершин"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("A", "C", {})

        adjacent = graph.get_adjacent_vertices("A")
        adjacent_values = {v.value for v in adjacent}
        assert adjacent_values == {"B", "C"}

    def test_incident_edges(self, graph):
        """Тест получения инцидентных рёбер"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("A", "C", {})

        incident = graph.get_incident_connections("A")
        assert len(incident) == 2

    def test_empty_graph(self, graph):
        """Тест пустого графа"""
        assert graph.is_graph_empty() == True
        assert graph.get_vertex_count() == 0
        assert graph.get_connection_count() == 0

    def test_clear_graph(self, graph):
        """Тест очистки графа"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.create_connection("A", "B", {})

        graph.clear_graph()

        assert graph.is_graph_empty() == True
        assert graph.get_vertex_count() == 0
        assert graph.get_connection_count() == 0

    def test_vertex_iterator(self, graph):
        """Тест итератора вершин"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})

        vertices = list(graph.vertex_iterator())
        assert len(vertices) == 3
        vertex_values = {v.value for v in vertices}
        assert vertex_values == {"A", "B", "C"}

    def test_reverse_vertex_iterator(self, graph):
        """Тест обратного итератора вершин"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})

        vertices = list(graph.reverse_vertex_iterator())
        assert len(vertices) == 3
        vertex_values = {v.value for v in vertices}
        assert vertex_values == {"A", "B", "C"}

    def test_edge_iterator(self, graph):
        """Тест итератора рёбер"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("B", "C", {})

        edges = list(graph.connection_iterator())
        assert len(edges) == 2

    def test_adjacent_iterator(self, graph):
        """Тест итератора смежных вершин"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("A", "C", {})

        adjacent = list(graph.adjacent_vertex_iterator("A"))
        assert len(adjacent) == 2
        adjacent_values = {v.value for v in adjacent}
        assert adjacent_values == {"B", "C"}

    def test_incident_iterator(self, graph):
        """Тест итератора инцидентных рёбер"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("A", "C", {})

        incident = list(graph.incident_connection_iterator("A"))
        assert len(incident) == 2

    def test_immutable_iterators(self, graph):
        """Тест неизменяемых итераторов"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.create_connection("A", "B", {})

        imm_vertices = list(graph.immutable_vertex_iterator())
        assert len(imm_vertices) == 2

        imm_edges = list(graph.immutable_connection_iterator())
        assert len(imm_edges) == 1

    def test_iterator_removal(self, graph):
        """Тест удаления по итератору"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})

        # Удаление вершины по итератору
        vertex_iter = graph.vertex_iterator()
        first_vertex = next(vertex_iter)
        graph.delete_vertex_via_iterator(vertex_iter)

        assert graph.get_vertex_count() == 2
        assert graph.vertex_exists(first_vertex.value) == False

        # Удаление ребра по итератору
        edge_iter = graph.connection_iterator()
        if graph.get_connection_count() > 0:
            first_edge = next(edge_iter)
            graph.delete_connection_via_iterator(edge_iter)
            assert graph.get_connection_count() == 0

    def test_complex_operations(self, graph):
        """Тест комплексных операций"""
        # Создаём сложный граф
        for i in range(5):
            graph.insert_vertex(f"V{i}", {"index": i})

        # Создаём рёбра
        for i in range(4):
            graph.create_connection(f"V{i}", f"V{i + 1}", {"weight": i})

        # Проверяем структуру
        assert graph.get_vertex_count() == 5
        assert graph.get_connection_count() == 4

        # Удаляем вершину
        graph.delete_vertex("V2")
        assert graph.get_vertex_count() == 4
        assert graph.get_connection_count() == 2  # Удалились рёбра V1-V2 и V2-V3

    def test_string_representation(self, graph):
        """Тест строкового представления"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.create_connection("A", "B", {})

        str_repr = str(graph)
        assert "UndirectedGraph" in str_repr
        assert "A" in str_repr
        assert "B" in str_repr

        repr_str = repr(graph)
        assert "UndirectedGraph" in repr_str

    def test_all_connections(self, graph):
        """Тест получения всех соединений"""
        graph.insert_vertex("A", {})
        graph.insert_vertex("B", {})
        graph.insert_vertex("C", {})
        graph.create_connection("A", "B", {})
        graph.create_connection("B", "C", {})

        connections = graph.get_all_connections()
        assert len(connections) == 2
        assert ("A", "B") in connections
        assert ("B", "C") in connections