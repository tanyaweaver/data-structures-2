#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
from collections import deque
from math import log10


def _get_digit(num, position):
    """Find digit at particular decimal position in a number."""
    return num // 10 ** position % 10


def _put_nums_in_buckets(a_list, position):
    """
    Queue numbers into appropriate buckets based on the value
    at the particular decimal position.
    """
    q_list = []
    for x in range(10):
        queue_ = deque()
        q_list.append(queue_)
    for num in a_list:
        digit = _get_digit(num, position)
        q_list[digit].append(num)
    return q_list


def _find_num_of_iterations(a_list):
    """
    Find number of the sorting iterations to be performed
    (this equals number of digits in the biggest number in the list).
    """
    num_of_iterations = int(log10(max(a_list)) + 1)
    return num_of_iterations


def _dequeue_queues_into_list(q_list):
    """Dequeue all the buckets in the pending list into a list."""
    a_list = []
    for deque_ in q_list:
        while len(deque_) != 0:
            a_list.append(deque_.popleft())
    return a_list


def radixsort(a_list):
    """Sort a list using radix sort."""
    if len(a_list) != 0:
        num_of_iterations = _find_num_of_iterations(a_list)
        pos = 0
        while pos < num_of_iterations:
            for num in a_list:
                pending = _put_nums_in_buckets(a_list, pos)
                a_list = _dequeue_queues_into_list(pending)
                pos += 1
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
        radixsort(list_)
        end_time = time.time()
        t = (end_time - start_time) * 1000
        times.append(t)
    print('Radix sort is a non-comparative integer sorting algorithm')
    print('that sorts data with integer keys by grouping keys')
    print('by the individual digits which share the same significant')
    print('position and value. ')
    print('Radix sort best performs for short lists of small numbers.')
    print('Average run time for:')
    print('1) list with 1 small item: {} ms.'.format(times[0]))
    print('2) list with a few small items: {} ms.'.format(times[1]))
    print('3) list with 100 identical items: {} ms.'.format(times[2]))
    print('4) unsorted list with 100 items (range 0 - 10000):')
    print('{} ms.'.format(times[3]))
    print('5) sorted list with 100 items (range 0 - 10000):')
    print('{} ms.'.format(times[4]))
    print('6) unsorted list with 100 items (99 of 11\'s, and 100000000):')
    print('{} ms.'.format(times[5]))
