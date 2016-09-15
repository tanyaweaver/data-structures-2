#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""Implementation of a queue list"""


from dll import DoublyLL


class Queue(object):
    def __init__(self, iterable=None):
        """Initiate an instance of Queue using DoublyLL for composition."""
        self._doublyLL = DoublyLL(iterable)

    def enqueue(self, val):
        """Add val to the head of a queue."""
        self._doublyLL.push(val)
        return self

    def dequeue(self):
        """Remove and return val from the tail of a queue."""
        return self._doublyLL.shift()

    def peek(self):
        """Return next value in the queue."""
        try:
            return self._doublyLL.tail_node.value
        except AttributeError:
            return None

    def size(self):
        """Return size of the queue."""
        return self._doublyLL.__len__()
