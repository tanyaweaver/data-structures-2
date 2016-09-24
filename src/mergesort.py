#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from random import choice


def mergesort(a_list):
    """Sort <a_list> using merge sort algorithm."""
    if len(a_list) <= 1:
        return a_list
    left = []
    right = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            left.append(a_list[i])
        else:
            right.append(a_list[i])
    left = mergesort(left)
    right = mergesort(right)
    return _merge(left, right)


def _merge(left, right):
    """Helper function. Merge 2 sorted lists into a list that is sorted."""
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while len(left) != 0:
        result.append(left[0])
        left.pop(0)
    while len(right) != 0:
        result.append(right[0])
        right.pop(0)
    return result


def _random_list(n):
    """Shuffle a list(range(n))."""
    result = []
    for i in range(n):
        while True:
            random_number = choice(range(n))
            if random_number not in result:
                break
        result.append(random_number)
    return result


if __name__ == '__main__':
        import time
        LISTS = (
            [1],
            _random_list(10),
            _random_list(100),
            _random_list(1000),
            list(range(1000))
        )
        times = []
        for list_ in LISTS:
            start_time = time.time()
            mergesort(list_)
            end_time = time.time()
            t = (end_time - start_time) * 1000
            times.append(t)
        print('Merge sort has 2 steps:')
        print(' 1) Divide the unsorted list into n sublists, ')
        print('     each containing 1 element.')
        print(' 2) Repeatedly merge sublists to produce new sorted sublists ')
        print('     until there is only 1 sublist remaining.')
        print('     This will be the sorted list.')
        print('Merge sort best performs for short lists.')
        print('Average run time for:')
        print('1) list with 1 item: {} ms.'.format(times[0]))
        print('2) unsorted list with 10 items: {} ms.'.format(times[1]))
        print('3) unsorted list with 100 items: {} ms.'.format(times[2]))
        print('4) unsorted list with 1000 items: {} ms.'.format(times[3]))
        print('5) sorted list with 1000 items: {} ms.'.format(times[4]))
