#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from mergesort import mergesort, _random_list
import pytest


MERGE = [
    ([], []),
    ([1], [1]),
    (_random_list(100), list(range(100))),
    ([4, 3.999, 4.01], [3.999, 4, 4.01]),
    ([3, 6, 8, 6, 6], [3, 6, 6, 6, 8])
]


@pytest.mark.parametrize('a_list, result', MERGE)
def test_mergesort1(a_list, result):
    """Prove that mergesort returns an expected sorted list."""
    assert mergesort(a_list) == result


def test_mergesort2():
    """
    Prove that mergesort is a stable sort: the implementation preserves
    the input order of equal elements in the sorted output.
    """
    a_list = [3, 3, 3, 3, 3, 3, 3]
    result = mergesort(a_list)
    for i in range(len(a_list)):
        assert result[i] is a_list[i]
