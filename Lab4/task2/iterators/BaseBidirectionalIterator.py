"""общая логика для всех итераторов."""


from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Self
from ImmutableWrapper import ImmutableWrapper

V = TypeVar("V") # тип элемента, по которому итерируемся (например, вершина или ребро)

"""Этот класс задаёт «скелет» для всех двунаправленных итераторов: 
он описывает, какие поля и методы должны быть у любого такого итератора, 
а конкретные детали (как двигаться вперёд/назад) реализуются в 
наследниках (ForwardIterator, BackwardIterator, Immutable*Iterator).
"""

class BaseBidirectionalIterator(ABC, Generic[V]):

    _collection: list[V] #  список элементов, по которым ходит итератор
    _position: int  # текущая позиция в этом списке (индекс)

    # Эти поля здесь только аннотированы типами; реальные значения задаются уже
    # в конструкторах наследников (ForwardIterator.__init__, BackwardIterator.__init__).

    @property # @property делает метод «как поле»: снаружи пишешь iterator.position,
    # а не iterator.position()

    def position(self) -> int: # Возвращает текущий индекс в коллекции.
        return self._position

    def __iter__(self) -> Self:
        return self

    @abstractmethod # у базового класса нет реализации, наследники ОБЯЗАНЫ её написать
    def previous(self) -> V: ...

    @abstractmethod
    def __next__(self) -> V: ...

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self._collection == other._collection and self._position == other._position