import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graph.MatrixManager import MatrixManager
from graph.AdjacencyManager import AdjacencyManager
from graph.GraphVertex import GraphVertex
from graph.GraphNode import GraphNode


def test_matrix_manager_basic():
    """Тест базовых операций MatrixManager"""
    matrix = MatrixManager()

    # Изначально матрица пустая
    assert matrix.current_size == 0

    # Расширяем матрицу
    matrix.expand_matrix(3)
    assert matrix.current_size == 3

    # Получаем доступный индекс
    index = matrix.get_available_index()
    assert index == 3  # Так как матрица размера 3, следующий индекс 3


def test_matrix_manager_connections():
    """Тест операций с соединениями в MatrixManager"""
    matrix = MatrixManager()
    matrix.expand_matrix(3)

    # Создаем тестовый узел
    vertex = GraphVertex("A", {}, 0)
    node = GraphNode(vertex, 0, 1)

    # Устанавливаем соединение
    matrix.set_connection(0, 1, node)
    assert matrix.get_connection(0, 1) == node
    assert matrix.get_connection(1, 0) == node  # Должно работать в обе стороны

    # Удаляем соединение
    matrix.remove_connection(0, 1)
    assert matrix.get_connection(0, 1) is None


def test_adjacency_manager_basic():
    """Тест базовых операций AdjacencyManager"""
    vertex1 = GraphVertex("A", {}, 0)
    vertex2 = GraphVertex("B", {}, 1)
    vertex3 = GraphVertex("C", {}, 2)

    node1 = GraphNode(vertex2, 0, 1)
    node2 = GraphNode(vertex3, 0, 2)

    # Добавляем соединения
    AdjacencyManager.add_connection(vertex1, node1)
    AdjacencyManager.add_connection(vertex1, node2)

    # Проверяем смежные вершины
    adjacent = AdjacencyManager.get_connected_vertices(vertex1)
    assert len(adjacent) == 2
    assert vertex2 in adjacent
    assert vertex3 in adjacent

    # Проверяем количество соединений
    count = AdjacencyManager.count_connections(vertex1)
    assert count == 2

    # Удаляем соединение
    AdjacencyManager.remove_connection(vertex1, node1)
    adjacent_after = AdjacencyManager.get_connected_vertices(vertex1)
    assert len(adjacent_after) == 1
    assert vertex3 in adjacent_after


def test_adjacency_manager_empty():
    """Тест AdjacencyManager с пустым списком"""
    vertex = GraphVertex("A", {}, 0)

    adjacent = AdjacencyManager.get_connected_vertices(vertex)
    assert len(adjacent) == 0

    count = AdjacencyManager.count_connections(vertex)
    assert count == 0