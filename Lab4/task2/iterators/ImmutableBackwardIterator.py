"""Это почти копия BackwardIterator, только с «заморозкой» элементов через ImmutableWrapper.
Идея: можно обойти коллекцию с конца и при этом не дать пользователю изменять объекты."""

from typing import TypeVar, Generic
from .BaseBidirectionalIterator import BaseBidirectionalIterator
from ImmutableWrapper import ImmutableWrapper

V = TypeVar("V")

class ImmutableBackwardIterator(BaseBidirectionalIterator[V], Generic[V]):
    def __init__(self, collection: list[V], start: int | None = None) -> None:
        self._collection: list[V] = collection
        self._position: int = start or len(collection)

    def __next__(self) -> ImmutableWrapper[V]:
        self._position -= 1
        if self._position < 0:
            raise StopIteration
        return ImmutableWrapper(self._collection[self._position])

    def previous(self) -> ImmutableWrapper[V]:
        self._position += 1
        if self._position >= len(self._collection):
            raise StopIteration
        return ImmutableWrapper(self._collection[self._position])