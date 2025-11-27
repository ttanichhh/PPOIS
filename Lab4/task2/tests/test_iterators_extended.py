import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from iterators import ForwardIterator, BackwardIterator, ImmutableForwardIterator, ImmutableBackwardIterator
from ImmutableWrapper import ImmutableWrapper


def test_forward_iterator_manual():
    """Тест ручного использования ForwardIterator"""
    items = [1, 2, 3]
    iterator = ForwardIterator(items)

    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3

    with pytest.raises(StopIteration):
        next(iterator)


def test_forward_iterator_prev():
    """Тест метода previous в ForwardIterator"""
    items = [1, 2, 3]
    iterator = ForwardIterator(items)

    next(iterator)  # 1
    next(iterator)  # 2
    assert iterator.previous() == 1
    assert next(iterator) == 2


def test_backward_iterator_manual():
    """Тест ручного использования BackwardIterator"""
    items = [1, 2, 3]
    iterator = BackwardIterator(items)

    assert next(iterator) == 3
    assert next(iterator) == 2
    assert next(iterator) == 1

    with pytest.raises(StopIteration):
        next(iterator)


def test_backward_iterator_prev():
    """Тест метода previous в BackwardIterator"""
    items = [1, 2, 3]
    iterator = BackwardIterator(items)

    next(iterator)  # 3
    next(iterator)  # 2
    assert iterator.previous() == 3
    assert next(iterator) == 2




def test_iterator_equality():
    """Тест сравнения итераторов"""
    items = [1, 2, 3]
    iter1 = ForwardIterator(items)
    iter2 = ForwardIterator(items)

    # Должны быть равны при одинаковых параметрах
    assert iter1 == iter2

    # После движения должны различаться
    next(iter1)
    assert iter1 != iter2
