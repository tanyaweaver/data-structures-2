#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
from collections import deque
from math import log10


def get_digit(num, position):
    return num // 10 ** position % 10


def put_nums_in_buckets(a_list, position):
    q_list = []
    for x in range(10):
        queue_ = deque()
        q_list.append(queue_)
    # import pdb; pdb.set_trace()
    for num in a_list:
        digit = get_digit(num, position)
        q_list[digit].append(num)
    return q_list


def find_num_of_iterations(a_list):
    num_of_iterations = int(log10(max(a_list)) + 1)
    return num_of_iterations


def dequeue_queues_into_list(q_list):
    a_list = []
    for deque_ in q_list:
        while len(deque_) != 0:
            a_list.append(deque_.popleft())
    return a_list


def radixsort(a_list):
    num_of_iterations = find_num_of_iterations(a_list)
    pos = 0
    while pos < num_of_iterations:
        for num in a_list:
            pending = put_nums_in_buckets(a_list, pos)
            a_list = dequeue_queues_into_list(pending)
            pos += 1
    return a_list
