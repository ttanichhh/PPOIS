"""как устроена и расширяется матрица смежности, где именно лежит ссылка на GraphNode"""

from typing import Generic, TypeVar, List, Optional
from graph.GraphNode import GraphNode

T = TypeVar("T")
P = TypeVar("P")


class MatrixManager(Generic[T, P]):
    """Управление матрицей смежности"""

    def __init__(self):
        self._matrix: List[List[Optional[GraphNode[T, P]]]] = []
        self._available_indices: List[int] = []

    def expand_matrix(self, new_size: int):
        """Расширяет матрицу до нового размера"""
        current_size = len(self._matrix)
        if new_size <= current_size:
            return

        # Добавляем новые столбцы к существующим строкам
        for i in range(current_size):
            self._matrix[i].extend([None] * (new_size - current_size))

        # Добавляем новые строки
        for i in range(current_size, new_size):
            self._matrix.append([None] * new_size)

    def set_connection(self, row: int, col: int, node: GraphNode[T, P]):
        """Устанавливает связь в матрице"""
        i, j = min(row, col), max(row, col)
        self._matrix[i][j] = node

    def get_connection(self, row: int, col: int) -> Optional[GraphNode[T, P]]:
        """Получает связь из матрицы"""
        i, j = min(row, col), max(row, col)
        if i < len(self._matrix) and j < len(self._matrix[i]):
            return self._matrix[i][j]
        return None

    def remove_connection(self, row: int, col: int):
        """Удаляет связь из матрицы"""
        i, j = min(row, col), max(row, col)
        if i < len(self._matrix) and j < len(self._matrix[i]):
            self._matrix[i][j] = None

    def get_available_index(self) -> int:
        """Возвращает доступный индекс для новой вершины"""
        if self._available_indices:
            return self._available_indices.pop()
        return len(self._matrix)

    def release_index(self, index: int):
        """Освобождает индекс для повторного использования"""
        self._available_indices.append(index)

    @property
    def current_size(self) -> int:
        return len(self._matrix)