#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import division, unicode_literals
from collections import deque
from radixsort import (
    _get_digit,
    _put_nums_in_buckets,
    _find_num_of_iterations,
    _dequeue_queues_into_list,
    radixsort
)
import pytest

GET_DIGIT = [
    (11, 0, 1),
    (183, 2, 1),
    (968438, 4, 6),
    (9865987735468764, 11, 9),
    (6354935, 6, 6),
    (100, 1, 0),
    (15, 7, 0)
]


BUCKETS = [
    ([13, 8954, 4, 100, 2], 0,
     [deque([100]), deque([]), deque([2]), deque([13]), deque([8954, 4]),
      deque([]), deque([]), deque([]), deque([]), deque([])]),
    ([1, 6544, 4687, 100, 76542], 3,
     [deque([1, 100]), deque([]), deque([]), deque([]), deque([4687]),
      deque([]), deque([6544, 76542]), deque([]), deque([]), deque([])])
]


ITERS = [
    ([1, 6544, 4687, 100, 76542], 5),
    ([13, 8954, 4, 100, 2], 4),
    ([198563, 8954, 41, 0, 100, 2], 6),
    ([13, 8, 4, 100, 2], 3),
    ([1, 8, 4, 0, 2], 1),
    ([1, 84, 4, 10, 2], 2),
    ([13, 8954, 6198468734, 100, 2], 10)
]


DEQUES = [
    ([deque([100]), deque([]), deque([2]), deque([13]), deque([8954, 4]),
      deque([]), deque([]), deque([]), deque([]), deque([])],
     [100, 2, 13, 8954, 4]),
    ([deque([1, 100]), deque([]), deque([]), deque([]), deque([4687]),
      deque([]), deque([6544, 76542]), deque([]), deque([]), deque([])],
     [1, 100, 4687, 6544, 76542])
]

RADIX = [
    ([48, 1, 107], [1, 48, 107]),
    ([100, 2, 13, 8954, 4], [2, 4, 13, 100, 8954]),
    ([1, 6544, 4687, 100, 76542], [1, 100, 4687, 6544, 76542]),
    ([198563, 8954, 41, 0, 100, 2, 0], [0, 0, 2, 41, 100, 8954, 198563])
]


@pytest.mark.parametrize('num, position, digit', GET_DIGIT)
def test_get_digit(num, position, digit):
    """Prove that _get_digit() return an expected digit."""
    assert _get_digit(num, position) == digit


@pytest.mark.parametrize('a_list, position, q_list', BUCKETS)
def test_put_nums_in_buckets(a_list, position, q_list):
    """Prove that _put_nums_in_buckets() does so correctly."""
    assert _put_nums_in_buckets(a_list, position) == q_list


@pytest.mark.parametrize('a_list, result', ITERS)
def test_find_num_of_iterations(a_list, result):
    """
    Prove that _find_num_of_iterations() returns the correct number.
    """
    assert _find_num_of_iterations(a_list) == result


@pytest.mark.parametrize('q_list, result', DEQUES)
def test_dequeue_queues_into_list(q_list, result):
    """
    Prove that _dequeue_queues_into_list() returns the expected list.
    """
    assert _dequeue_queues_into_list(q_list) == result


@pytest.mark.parametrize('a_list, result', RADIX)
def test_radixsort(a_list, result):
    """Prove that radixsort() returns appropriately sorted list."""
    assert radixsort(a_list) == result


def test_radixsort_is_stable():
    """Prove that radix sort is stable."""
    a_list = [15, 15, 15, 15, 15]
    result = radixsort(a_list)
    for i in range(len(a_list)):
        assert a_list[i] is result[i]


def test_radixsort_empty_list():
    """Prove that radixsort([]) returns an empty list."""
    assert radixsort([]) == []
