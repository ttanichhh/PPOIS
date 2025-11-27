from typing import Any, Generic, TypeVar
from GraphExceptions import ImmutableObjectException

T = TypeVar("T")

class ImmutableWrapper(Generic[T]):
    __slots__ = ("_content",)
    _content: T

    def __init__(self, content: T) -> None:
        object.__setattr__(self, "_content", content)

    def __getattribute__(self, name: str) -> Any:
        content_obj = object.__getattribute__(self, "_content")
        try:
            attr = getattr(content_obj, name)
        except AttributeError:
            raise ImmutableObjectException(f"Атрибут '{name}' не существует")

        return attr

    def __setattr__(self, name: str, value: Any) -> None:
        raise ImmutableObjectException("Изменение ImmutableWrapper запрещено")

    def __repr__(self) -> str:
        content_obj = object.__getattribute__(self, "_content")
        return f"Immutable({repr(content_obj)})"