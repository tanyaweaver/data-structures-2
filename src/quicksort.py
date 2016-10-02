#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from random import choice


def _sort_relative_to_pivot(a_list, pivot_pos):
    """
    Sort items in the list relative to the pivot.
    Return position of the pivot after the sort completed.
    """
    #import pdb; pdb.set_trace()
    pivot = a_list[pivot_pos]
    while True:
        i = 0
        x = len(a_list) - 1
        while a_list[i] < pivot or (a_list[i] == pivot and i != pivot_pos):
            i += 1
        while a_list[x] > pivot:
            x -= 1
        if i >= x:
            return x
        a_list[i], a_list[x] = a_list[x], a_list[i]
        if i == pivot_pos:
            pivot_pos = x
        elif x == pivot_pos:
            pivot_pos = i


def quicksort(a_list):
    """Return sorted list using quicksort algorithm."""
    #import pdb; pdb.set_trace()
    if len(a_list) <= 1:
        return a_list
    pivot_pos = choice(range(len(a_list)))
    devider = _sort_relative_to_pivot(a_list, pivot_pos)
    left_list = a_list[:devider]
    right_list = a_list[(devider + 1):]
    quicksort(left_list)
    quicksort(right_list)
    a_list[:devider] = left_list
    a_list[(devider + 1):] = right_list
    return a_list
