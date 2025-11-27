from typing import TypeVar, Generic
from .BaseBidirectionalIterator import BaseBidirectionalIterator
from ImmutableWrapper import ImmutableWrapper

V = TypeVar("V")

class ImmutableForwardIterator(BaseBidirectionalIterator[V], Generic[V]):
    def __init__(self, collection: list[V], start: int = -1) -> None:
        self._position: int = start
        self._collection: list[V] = collection

    def __next__(self) -> ImmutableWrapper[V]:
        self._position += 1
        if self._position >= len(self._collection):
            raise StopIteration
        return ImmutableWrapper(self._collection[self._position])

    def previous(self) -> ImmutableWrapper[V]:
        self._position -= 1
        if self._position < 0:
            raise StopIteration
        return ImmutableWrapper(self._collection[self._position])