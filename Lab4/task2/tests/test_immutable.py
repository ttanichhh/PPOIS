import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ImmutableWrapper import ImmutableWrapper
from GraphExceptions import ImmutableObjectException


def test_immutable_wrapper_creation():
    """Тест создания ImmutableWrapper"""
    obj = {"key": "value"}
    wrapper = ImmutableWrapper(obj)

    # Вместо прямого доступа к _content, используем object.__getattribute__
    content = object.__getattribute__(wrapper, "_content")
    assert content == obj


def test_immutable_wrapper_access():
    """Тест доступа к атрибутам через ImmutableWrapper"""

    class TestClass:
        def __init__(self):
            self.value = "test"
            self.number = 42

        def method(self):
            return "method_result"

    test_obj = TestClass()
    wrapper = ImmutableWrapper(test_obj)

    # Доступ к атрибутам
    assert wrapper.value == "test"
    assert wrapper.number == 42
    assert wrapper.method() == "method_result"


def test_immutable_wrapper_modification():
    """Тест попытки модификации ImmutableWrapper"""
    obj = {"key": "value"}
    wrapper = ImmutableWrapper(obj)

    # Попытка изменить атрибут должна вызвать исключение
    with pytest.raises(ImmutableObjectException):
        wrapper.new_attr = "new_value"

    with pytest.raises(ImmutableObjectException):
        wrapper._content = "modified"


def test_immutable_wrapper_repr():
    """Тест строкового представления ImmutableWrapper"""
    obj = "test_object"
    wrapper = ImmutableWrapper(obj)
    repr_str = repr(wrapper)
    assert "Immutable" in repr_str
    assert "test_object" in repr_str


def test_immutable_wrapper_nonexistent_attribute():
    """Тест доступа к несуществующему атрибуту"""
    obj = {"key": "value"}
    wrapper = ImmutableWrapper(obj)

    with pytest.raises(ImmutableObjectException):
        _ = wrapper.nonexistent_attr