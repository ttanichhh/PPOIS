'''Это универсальная обёртка для любого объекта.
Запрещает менять содержимое (атрибуты) объекта после создания,
а при попытке изменить бросает специальное исключение.
'''

from typing import Any, Generic, TypeVar
from GraphExceptions import ImmutableObjectException

T = TypeVar("T")

class ImmutableWrapper(Generic[T]):
    __slots__ = ("_content",) # Задаёт, что у экземпляров будет только одно поле _content, что экономит память
    _content: T

    def __init__(self, content: T) -> None: # Конструктор записывает переданный объект (любой тип) в приватное поле _content

        object.__setattr__(self, "_content", content)


    #При попытке получить любой атрибут wrapper-а происходит перенаправление:
    # если обращаться к wrapper.attr, на самом деле происходит вызов getattr(self._content, attr).
    # Если у оригинального объекта атрибут не найден — вызывается исключение.
    def __getattribute__(self, name: str) -> Any:
        content_obj = object.__getattribute__(self, "_content")
        try:
            attr = getattr(content_obj, name)
        except AttributeError:
            raise ImmutableObjectException(f"Атрибут '{name}' не существует")

        return attr

    #Любая попытка установить или поменять атрибут wrapper-а приводит к выбросу ImmutableObjectException,
    # то есть объект нельзя модифицировать.
    def __setattr__(self, name: str, value: Any) -> None:
        raise ImmutableObjectException("Изменение ImmutableWrapper запрещено")

    #Отвечает за строковое представление: выводит строку вида Immutable(repr(content)),
    # чтобы было видно, что это именно immutable-обёртка.
    def __repr__(self) -> str:
        content_obj = object.__getattribute__(self, "_content")
        return f"Immutable({repr(content_obj)})"