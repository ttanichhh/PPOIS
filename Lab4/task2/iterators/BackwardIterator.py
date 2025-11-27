from iterators.BaseBidirectionalIterator import BaseBidirectionalIterator
from typing import TypeVar, Generic

V = TypeVar("V")

class BackwardIterator(BaseBidirectionalIterator[V], Generic[V]):
    def __init__(self, collection: list[V], start_position: int | None = None) -> None:
        self._collection: list[V] = collection
        self._position: int = start_position if start_position is not None else len(collection)

    def __next__(self) -> V:
        self._position -= 1
        if self._position < 0:
            raise StopIteration
        return self._collection[self._position]

    def previous(self) -> V:
        self._position += 1
        if self._position >= len(self._collection):
            raise StopIteration
        return self._collection[self._position]