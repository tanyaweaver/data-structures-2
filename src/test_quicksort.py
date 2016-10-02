#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
import pytest
from quicksort import (
    _sort_relative_to_pivot,
    quicksort
)

SORT_ONCE = [
    # ([4, 6, 3, 8, 1], 2, 1, [1, 3, 4, 6, 8]),
    # ([1], 0, 0, [1]),
    # ([1, 2, 3, 4, 5, 6], 0, 0, [1, 2, 3, 4, 5, 6]),
    # ([1, 2, 3, 4, 5, 6], 2, 2, [1, 2, 3, 4, 5, 6]),
    # ([1, 2, 3, 4, 5, 6], 5, 5, [1, 2, 3, 4, 5, 6]),
    # ([1, 1, 1, 1, 1, 1], 2, 5, [1, 1, 1, 1, 1, 1]),
    # ([1, 4, 1, 3, 1, 7], 2, 2, [1, 1, 1, 3, 4, 7]),
    # ([6, 5, 4, 3, 2, 1], 3, 2, [1, 2, 3, 4, 5, 6]),
    # ([6, 5, 4, 3, 2, 1], 0, 5, [1, 5, 4, 3, 2, 6]),
    # ([6, 5, 4, 3, 2, 1], 5, 0, [1, 5, 4, 3, 2, 6]),
    ([6, 5, 4, 3, 23, 2, 1], 0, 5, [1, 5, 4, 3, 2, 6, 23])
]

QUICK_SORT = [
    # ([3, 2, 1], [1, 2, 3]),
    ([6, 42, 5, 4, 234, 3, 23, 2, 77, 1], [1, 2, 3, 4, 5, 6, 23, 42, 77, 234]),
    ([6, 5.5, 22, 35, 4, 3, 2.24, 1], [1, 2.24, 3, 4, 5.5, 6, 22, 35])
]


@pytest.mark.parametrize('a_list, piv_pos, piv_pos_sorted, result', SORT_ONCE)
def test_sort_relative_to_pivot1(a_list, piv_pos, piv_pos_sorted, result):
    """Prove that _sort_relative_to_pivor() returns correct pivot position."""
    assert _sort_relative_to_pivot(a_list, piv_pos) == piv_pos_sorted


@pytest.mark.parametrize('a_list, piv_pos, piv_pos_sorted, result', SORT_ONCE)
def test_sort_relative_to_pivot2(a_list, piv_pos, piv_pos_sorted, result):
    """Prove that _sort_relative_to_pivor() results in a correct list."""
    _sort_relative_to_pivot(a_list, piv_pos)
    assert a_list == result


@pytest.mark.parametrize('a_list, result', QUICK_SORT)
def test_quicksort(a_list, result):
    assert quicksort(a_list) == result
