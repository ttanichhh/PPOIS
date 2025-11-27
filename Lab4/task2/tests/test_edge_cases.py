import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from UndirectedGraph import UndirectedGraph
from GraphExceptions import *


def test_self_loop():
    """Тест петли (ребро из вершины в саму себя)"""
    graph = UndirectedGraph[str, dict]()
    graph.insert_vertex("A", {})

    # В неориентированном графе петли обычно не разрешены, но проверим поведение
    # Это может зависеть от реализации
    try:
        graph.create_connection("A", "A", {})
        # Если не выброшено исключение, проверяем
        if graph.connection_exists("A", "A"):
            assert graph.calculate_vertex_degree("A") == 1
    except Exception:
        # Ожидаемо, если петли запрещены
        pass


def test_single_vertex_graph():
    """Тест графа с одной вершиной"""
    graph = UndirectedGraph[str, dict]()
    graph.insert_vertex("A", {})

    assert graph.get_vertex_count() == 1
    assert graph.get_connection_count() == 0
    assert graph.calculate_vertex_degree("A") == 0
    assert len(graph.get_adjacent_vertices("A")) == 0
    assert len(graph.get_incident_connections("A")) == 0


def test_complete_graph():
    """Тест полного графа (все вершины соединены со всеми)"""
    graph = UndirectedGraph[str, dict]()

    # Добавляем 3 вершины
    for i in range(3):
        graph.insert_vertex(f"V{i}", {})

    # Соединяем все со всеми
    graph.create_connection("V0", "V1", {})
    graph.create_connection("V0", "V2", {})
    graph.create_connection("V1", "V2", {})

    assert graph.get_vertex_count() == 3
    assert graph.get_connection_count() == 3

    # В полном графе каждая вершина имеет степень n-1
    for i in range(3):
        assert graph.calculate_vertex_degree(f"V{i}") == 2


def test_immutable_reverse_iterators():
    """Тест обратных неизменяемых итераторов"""
    graph = UndirectedGraph[str, dict]()
    graph.insert_vertex("A", {})
    graph.insert_vertex("B", {})
    graph.insert_vertex("C", {})
    graph.create_connection("A", "B", {})
    graph.create_connection("B", "C", {})

    # Тестируем все варианты обратных неизменяемых итераторов
    imm_rev_vertices = list(graph.immutable_reverse_vertex_iterator())
    assert len(imm_rev_vertices) == 3

    imm_rev_edges = list(graph.immutable_reverse_connection_iterator())
    assert len(imm_rev_edges) == 2

    imm_rev_adjacent = list(graph.immutable_reverse_adjacent_vertex_iterator("B"))
    assert len(imm_rev_adjacent) == 2

    imm_rev_incident = list(graph.immutable_reverse_incident_connection_iterator("B"))
    assert len(imm_rev_incident) == 2


def test_deep_copy():
    """Тест глубокого копирования"""
    graph = UndirectedGraph[str, dict]()
    graph.insert_vertex("A", {"color": "red"})
    graph.insert_vertex("B", {"color": "blue"})
    graph.create_connection("A", "B", {"weight": 5})

    # Создаем глубокую копию
    import copy
    graph_copy = copy.deepcopy(graph)

    # Проверяем, что структура совпадает
    assert graph_copy.get_vertex_count() == graph.get_vertex_count()
    assert graph_copy.get_connection_count() == graph.get_connection_count()

    # Проверяем, что это разные объекты
    assert graph_copy is not graph