#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
from collections import deque
from math import log10


def _get_digit(num, position):
    return num // 10 ** position % 10


def _put_nums_in_buckets(a_list, position):
    q_list = []
    for x in range(10):
        queue_ = deque()
        q_list.append(queue_)
    # import pdb; pdb.set_trace()
    for num in a_list:
        digit = _get_digit(num, position)
        q_list[digit].append(num)
    return q_list


def _find_num_of_iterations(a_list):
    num_of_iterations = int(log10(max(a_list)) + 1)
    return num_of_iterations


def _dequeue_queues_into_list(q_list):
    a_list = []
    for deque_ in q_list:
        while len(deque_) != 0:
            a_list.append(deque_.popleft())
    return a_list


def radixsort(a_list):
    if len(a_list) != 0:
        num_of_iterations = _find_num_of_iterations(a_list)
        pos = 0
        while pos < num_of_iterations:
            for num in a_list:
                pending = _put_nums_in_buckets(a_list, pos)
                a_list = _dequeue_queues_into_list(pending)
                pos += 1
    return a_list
