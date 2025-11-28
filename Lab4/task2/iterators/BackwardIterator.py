"""Этот класс даёт «обратный» итератор по списку: он ходит по элементам с конца к началу,
но при этом умеет двигаться и назад, и вперёд относительно текущей позиции.
"""

from iterators.BaseBidirectionalIterator import BaseBidirectionalIterator
from typing import TypeVar, Generic

V = TypeVar("V")

class BackwardIterator(BaseBidirectionalIterator[V], Generic[V]):
    def __init__(self, collection: list[V], start_position: int | None = None) -> None:
        self._collection: list[V] = collection # список, по которому будем ходить (например, список вершин или рёбер).
        self._position: int = start_position if start_position is not None else len(collection) # текущая позиция

    def __next__(self) -> V: # Движение назад (для цикла for)
        self._position -= 1
        if self._position < 0:
            raise StopIteration
        return self._collection[self._position]

    def previous(self) -> V: # Движение назад относительно текущей позиции – previous
        self._position += 1
        if self._position >= len(self._collection):
            raise StopIteration
        return self._collection[self._position]