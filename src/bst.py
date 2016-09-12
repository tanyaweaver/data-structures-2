#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals


class Node(object):
    """Define class for a node of a binary search tree."""
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def compare_self_to_a_node(self, n2):
        """Assume n1 and n2 are instances of Node."""
        if self.value > n2.value:
            if n2.right is None:
                n2.right = self
            else:
                n2 = n2.right
                self.compare_self_to_a_node(n2)
        elif self.value < n2.value:
            if n2.left is None:
                n2.left = self
            else:
                n2 = n2.left
                self.compare_self_to_a_node(n2)


class Bst(object):
    """Define binary search tree class."""
    def __init__(self, iterable=None):
        self._list = []
        self.head = None
        self.head.value = None
        self.head.left = None
        self.head.right = None

    def insert(self, value):
        new_node = Node(value)
        if new_node.value not in self._list:
            if self.head is None:
                self.head = new_node

                



