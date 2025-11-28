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
