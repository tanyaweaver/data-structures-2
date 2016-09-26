# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from random import choice


def insertion_sort(my_list):
    """Simple sorting algorithm that builds a sorted list
       one item at a time.
    """
    for i in range(1, len(my_list)):
        current = my_list[i]
        position = i
        while((position > 0) and (my_list[position - 1] > current)):
            my_list[position] = my_list[position - 1]
            position = position - 1
        if position != i:
            my_list[position] = current


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
            insertion_sort(list_)
            end_time = time.time()
            t = (end_time - start_time) * 1000
            times.append(t)
