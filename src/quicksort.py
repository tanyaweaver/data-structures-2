#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from random import choice


def _sort_relative_to_pivot(a_list, pivot_pos):
    """
    Sort items in the list relative to the pivot.
    Return position of the pivot after the sort completed.
    """
    pivot = a_list[pivot_pos]
    i = 0
    x = len(a_list) - 1
    while True:
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
    if len(a_list) <= 1:
        return a_list
    pivot_pos = choice(range(len(a_list)))
    divider = _sort_relative_to_pivot(a_list, pivot_pos)
    left_list = a_list[:divider]
    right_list = a_list[(divider + 1):]
    quicksort(left_list)
    quicksort(right_list)
    a_list[:divider] = left_list
    a_list[(divider + 1):] = right_list
    return a_list


if __name__ == '__main__':
    import time
    from random import sample
    LISTS = (
       [1],
       [1, 2, 6, 3, 4, 5, 0, 9, 8],
       [6851] * 100,
       sample(range(10000), 100),
       list(range(100)),
       [11] * 99 + [100000000]
    )
    times = []
    for list_ in LISTS:
        start_time = time.time()
        quicksort(list_)
        end_time = time.time()
        t = (end_time - start_time) * 1000
        times.append(t)
    print('Quicksort first divides a large array into smaller sub-arrays:')
    print('the low-elements and high-elements.')
    print('Quicksort can then recursively sort the sub-arrays.')
    print('Qucksort sort best performs for short lists of small numbers.')
    print('When the pivot is randomly chosen, average run time for:')
    print('1) list with 1 small item: {} ms.'.format(times[0]))
    print('2) list with a few small items: {} ms.'.format(times[1]))
    print('3) list with 100 identical items: {} ms.'.format(times[2]))
    print('4) unsorted list with 100 items (range 0 - 10000):')
    print('{} ms.'.format(times[3]))
    print('5) sorted list with 100 items (range 0 - 10000):')
    print('{} ms.'.format(times[4]))
    print('6) unsorted list with 100 items (99 of 11\'s, and 100000000):')
    print('{} ms.'.format(times[5]))
