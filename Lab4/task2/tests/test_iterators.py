import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from iterators import ForwardIterator, BackwardIterator


def test_forward_iterator():
    """Тест прямого итератора"""
    items = [1, 2, 3, 4, 5]
    iterator = ForwardIterator(items)

    result = list(iterator)
    assert result == items


def test_backward_iterator():
    """Тест обратного итератора"""
    items = [1, 2, 3, 4, 5]
    iterator = BackwardIterator(items)

    result = list(iterator)
    assert result == list(reversed(items))