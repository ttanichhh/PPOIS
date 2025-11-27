from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Self
from ImmutableWrapper import ImmutableWrapper

V = TypeVar("V")

class BaseBidirectionalIterator(ABC, Generic[V]):
    _position: int
    _collection: list[V]

    @property
    def position(self) -> int:
        return self._position

    def __iter__(self) -> Self:
        return self

    @abstractmethod
    def previous(self) -> V: ...

    @abstractmethod
    def __next__(self) -> V: ...

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self._collection == other._collection and self._position == other._position